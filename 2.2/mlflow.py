import os

import mlflow
from housing_price import ingest_data, score, train

remote_server_uri = "http://127.0.0.1:5000"
mlflow.set_tracking_uri(remote_server_uri)

experiment = mlflow.set_experiment("housing_price")

# parent (model scoring)
with mlflow.start_run(
    run_name="PARENT_RUN",
    experiment_id=experiment.experiment_id,
    tags={"version": "v1", "priority": "P1"},
    description="parent",
) as parent_run:
    mlflow.log_param("parent", "yes")
    flag_var, rmse, mae, r2 = score.eval_metrics(
        data_path=os.path.join("datasets", "housing"),
        output_path=os.path.join("mlruns"),
        model_path=os.path.join("artifacts"),
    )

    mlflow.log_metric(key="rmse", value=rmse)
    mlflow.log_metrics({"mae": mae, "r2": r2})
    # mlflow.log_artifact("mlruns/")
    print("Save to: {}".format(mlflow.get_artifact_uri()))

    # child 1 (data preparation)
    with mlflow.start_run(
        run_name="CHILD_RUN_1",
        experiment_id=experiment.experiment_id,
        description="child 1 (data preparation)",
        nested=True,
    ) as child_run:
        mlflow.log_param("child_1", "yes")

        flag_var = ingest_data.prepare_train(os.path.join("datasets", "housing"))
        mlflow.log_param("dataset_downloaded", flag_var)
        mlflow.log_param("train_val_created", flag_var)
        print("Save to: {}".format(mlflow.get_artifact_uri()))

    # child 2 (model training)
    with mlflow.start_run(
        run_name="CHILD_RUN_2",
        experiment_id=experiment.experiment_id,
        description="child 2 (model training)",
        nested=True,
    ) as child_run:
        mlflow.log_param("child_2", "yes")

        flag_var = train.training_data(
            os.path.join("datasets", "housing"),
            os.path.join("artifacts"),
        )

        mlflow.log_param("model_created", flag_var)
        # mlflow.log_metric(key="lin_mse", value=lin_mse)
        # mlflow.log_metric(key="lin_rmse", value=lin_rmse)
        # mlflow.log_metric(key="tree_mse", value=tree_mse)
        # mlflow.log_metric(key="tree_rmse", value=tree_rmse)
        # mlflow.log_param("model_created", flag_var)


print("parent run:")

print("run_id: {}".format(parent_run.info.run_id))
print("description: {}".format(parent_run.data.tags.get("mlflow.note.content")))
print("version tag value: {}".format(parent_run.data.tags.get("version")))
print("priority tag value: {}".format(parent_run.data.tags.get("priority")))
print("--")

# Search all child runs with a parent id
query = "tags.mlflow.parentRunId = '{}'".format(parent_run.info.run_id)
results = mlflow.search_runs(
    experiment_ids=[experiment.experiment_id], filter_string=query
)
print("child runs:")
print(results[["run_id", "tags.mlflow.runName"]])

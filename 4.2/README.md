# To excute the script
This code has python files refactored as scripts and are able to install as a package.
All the python scripts are available at `src/housing_price`.
This folder contains `datasets` which has the required datsets along with train and test datasets as csv files.

`housing_price` folder is refactored to a package so it contains `__init__.py`.

This package also contains `tests` folder which has some functional and unit tests for this project.

For installing the `housing_price` package u can just run the below command:

```
(mle-dev) (root-folder)$python setup.py install
```

`setup.py` contains code which will install the required packages and can use as a library.

For running scripts u can run the below command:

(mle-dev) (script-folder)$python3 <script>.py --args

Go to project root directory

First initialize the mlflow by running <mlflow ui> in terminal
1) run the script mlflowrun.py to run the entire ml scripts.
2)To run python script  run python < scriptname.py >
3) results will get displayed in the terminal and all the metrics,parameters,artifacts gets logged into mlflow

# Build docker container
create Dockerfile and build container ==> docker build -t image name

to run the image
docker run imagename

# push docker image
docker tag imagename YOUR_DOCKERHUB_NAME/imagename
docker push YOUR_DOCKERHUB_NAME/imagename

#pulling

docker pull YOUR_DOCKERHUB_NAME/imagename

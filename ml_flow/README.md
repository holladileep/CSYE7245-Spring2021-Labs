## MLflow

MLflow is an open source platform for managing the end-to-end machine learning lifecycle. It tackles four primary functions:

- Tracking experiments to record and compare parameters and results
- Packaging ML code in a reusable, reproducible form in order to share with other data scientists or transfer to production
- Managing and deploying models from a variety of ML libraries to a variety of model serving and inference platforms
- Providing a central model store to collaboratively manage the full lifecycle of an MLflow Model, including model versioning, stage transitions, and annotations [1]

#### MLflow Components

MLflow provides four components to help manage the ML workflow:

- MLflow Tracking is an API and UI for logging parameters, code versions, metrics, and artifacts when running your machine learning code and for later visualizing the results. You can use MLflow Tracking in any environment (for example, a standalone script or a notebook) to log results to local files or to a server, then compare multiple runs. Teams can also use it to compare results from different users.

- MLflow Projects are a standard format for packaging reusable data science code. Each project is simply a directory with code or a Git repository, and uses a descriptor file or simply convention to specify its dependencies and how to run the code. For example, projects can contain a conda.yaml file for specifying a Python Conda environment. When you use the MLflow Tracking API in a Project, MLflow automatically remembers the project version (for example, Git commit) and any parameters. You can easily run existing MLflow Projects from GitHub or your own Git repository, and chain them into multi-step workflows.

- MLflow Models offer a convention for packaging machine learning models in multiple flavors, and a variety of tools to help you deploy them. Each Model is saved as a directory containing arbitrary files and a descriptor file that lists several “flavors” the model can be used in. For example, a TensorFlow model can be loaded as a TensorFlow DAG, or as a Python function to apply to input data. MLflow provides tools to deploy many common model types to diverse platforms: for example, any model supporting the “Python function” flavor can be deployed to a Docker-based REST server, to cloud platforms such as Azure ML and AWS SageMaker, and as a user-defined function in Apache Spark for batch and streaming inference. If you output MLflow Models using the Tracking API, MLflow also automatically remembers which Project and run they came from.

- MLflow Registry offers a centralized model store, set of APIs, and UI, to collaboratively manage the full lifecycle of an MLflow Model. It provides model lineage (which MLflow experiment and run produced the model), model versioning, stage transitions (for example from staging to production or archiving), and annotations.
 [2]



### Getting Started

This example requires a Conda environment to run - install Conda on your machine from [here](https://conda.io/projects/conda/en/latest/user-guide/install/download.html)

This use case is from MLflow's examples and the complete list of examples can be found here: https://github.com/mlflow/mlflow/tree/master/examples

#### MLflow with TensorFlow 2.0.0

In this example, we use TensorFlow's [premade estimator iris data example](https://www.tensorflow.org/tutorials/estimator/premade) and add MLflow tracking.

This example trains a `tf.estimator.DNNClassifier` on the [iris dataset](https://archive.ics.uci.edu/ml/datasets/iris) and predicts on a validation set.

The code is mostly pure TensorFlow - we add a call to `mlflow.tensorflow.autolog()` before training to record params & metrics from model training (e.g. model loss) as part of an MLflow run. After training, `mlflow.tensorflow.autolog()` links the model with the same MLflow run when `export_saved_model()` is called, allowing us to associate the model with its training metrics & params. We then demonstrate how to load the saved model back as a generic `mlflow.pyfunc`, allowing us to make predictions on pandas DataFrames.

#### Code related to MLflow:
* [`mlflow.tensorflow.autolog()`](https://www.mlflow.org/docs/latest/tracking.html#automatic-logging-from-tensorflow-and-keras-experimental):
This is an experimental api that logs ML model artifacts and TensorBoard metrics created by the `tf.estimator` we are using.
The TensorBoard metrics are logged during training of the model. By default, MLflow autologs every 100 steps.
The ML model artifact creation is handled during the call to `tf.estimator.export_saved_model()`.

* [`mlflow.pyfunc.load_model()`](https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.load_model):
This function loads back the model as a generic python function. You can predict on this with a pandas DataFrame input.

#### Running the code
To run the example via MLflow, navigate to the cloned directory and run the command

```
mlflow run .
```

This will run `train_predict.py` with the default parameters `--batch_size=100` and `--train_steps=1000`. You can see the default values in the `MLproject` file.

In order to run the file with custom parameters, run the command

```
mlflow run . -P batch_size=X -P train_steps=Y
```

where `X` and `Y` are your desired values for the parameters.

If you have the required modules for the file and would like to skip the creation of a conda environment, add the argument `--no-conda`.

```
mlflow run . --no-conda
```

Once the code is finished executing, you can view the run's metrics, parameters, and details by running the command

```
mlflow ui
```

and navigating to [http://localhost:5000](http://localhost:5000).

For more information on MLflow tracking, click [here](https://www.mlflow.org/docs/latest/tracking.html#mlflow-tracking) to view documentation.


#### Citation & References

[[1] MLflow](https://www.mlflow.org/docs/latest/index.html) <br/>
[[2] MLflow Components](https://www.mlflow.org/docs/latest/concepts.html) <br/>
[[3] Mlflow Examples](https://github.com/mlflow/mlflow/tree/master/examples)

## Dask

Dask is designed to extend the numpy and pandas packages to work on data processing problems that are too large to be kept in memory. It breaks the larger processing job into many smaller tasks that are handled by numpy or pandas and then it reassembles the results into a coherent whole.
Dask is a flexible library for parallel computing in Python. [1]

Dask is composed of two parts:

- Dynamic task scheduling optimized for computation. This is similar to Airflow, Luigi, Celery, or Make, but optimized for interactive computational workloads.
- “Big Data” collections like parallel arrays, dataframes, and lists that extend common interfaces like NumPy, Pandas, or Python iterators to larger-than-memory or distributed environments. These parallel collections run on top of dynamic task schedulers.

As datasets and computations scale faster than CPUs and RAM, we need to find ways to scale our computations across multiple machines. This introduces many new concerns:

- How to have computers talk to each other over the network?
- How and when to move data between machines?
- How to recover from machine failures?
- How to deploy on an in-house cluster?
- How to deploy on the cloud?
- How to deploy on an HPC super-computer?
- How to provide an API to this system that users find intuitive?

While it is possible to build these systems in-house (and indeed, many exist), many organizations increasingly depend on solutions developed within the open source community. These tend to be more robust, secure, and fully featured without being tended by in-house staff.

Dask solves the problems above. It figures out how to break up large computations and route parts of them efficiently onto distributed hardware. Dask is routinely run on thousand-machine clusters to process hundreds of terabytes of data efficiently within secure environments. [2]

References: <br>
[[1]](https://docs.dask.org/en/latest/) <br>
[[2]](https://docs.dask.org/en/latest/why.html)

### Requirements 

```
pip install "dask[complete]"
pip install graphviz
pip install pandas
pip install tqdm
```

You must install both the graphviz system library (with tools like `apt-get`, `yum`, or `brew`) and the graphviz Python library. Download the executables from here: https://www.graphviz.org/download/

### Getting Data
This lab uses the [NYC Taxi Dataset](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page) - since this data is already is available on S3 and we have our AWS CLI configured, get the data using the following CLI command:
```
aws s3 cp "s3://nyc-tlc/trip data/yellow_tripdata_2018-04.csv" "tripdata.csv"
```
You may use the data from any Month/Year - but we will be sticking with data from April 2018 for this tutorial.

### Tutorial

Complete step-by-step instructions and explanations are documented in the `dask_lab.ipynb` Jupyter notebook. Run the notebook by starting your jupyter server. If you do not have it installed, run `pip install notebook` and start the server by running `jupyter notebok`.

## Debugging ML Talk 

`nyc_taxi_2020.ipynb` from [Shreya Shankar's Repo](https://github.com/shreyashankar/debugging-ml-talk)<br>

Fork the repo available at: https://github.com/shreyashankar/debugging-ml-talk

### Getting Started 

This requires a Saturn Cloud account to run. Sign up [here](https://accounts.community.saturnenterprise.io/auth/signup). Create a new `RAPIDS` project with the default configuration and open a Jupyter server, once your instance is provisoned. Upload `nyc_taxi_2020.ipynb` to the server and you should be good to go. 
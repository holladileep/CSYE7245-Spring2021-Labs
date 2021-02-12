## Plotly Dash

Dash is a productive Python framework for building web analytic applications.

Written on top of Flask, Plotly.js, and React.js, Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. It's particularly suited for anyone who works with data in Python.

Through a couple of simple patterns, Dash abstracts away all of the technologies and protocols that are required to build an interactive web-based application. [1]

#### Why use Dash?

The Good Reasons to Build a Dashboard with Dash
1. Open Source Tool: Dash is a great alternative BI tools to Tableau or Microsoft Power BI because it is costly to operate dashboards built by Tableau or Power BI. Dash provides similar quality and experience at no cost.
2. Run in Python: Dash runs in Python. You may use Pandas and any Python library for the pipeline and render the visualization with Dash.
3. Great Appearance: Dash and pure Plotlyare built on top of d3, it means Dash and pure Plotly make high quality visualizations which is comparable with Tableau charts.
4. Integrated with Pure Plotly: Plotly is one of the great open source visualization package in Python. If you know how to use Plotly, it does not take a long time to understand Dash. At the same time, you may also visualize your existing Plotly graphs on Dash with a little code editing.
5. Integrated with Flask: Dash runs web server in Flask. One of the nice features about Dash is that you do not need to set up Flask and it is easy to host the webserver in AWS. You do not need to know too much about web development.
6. Easy-to-use: Dash is a high level tool that the developers are only required to write in Python and have some understanding of html. No Javascript or d3 is needed to produce the dashboard. You may also leverage the interactive elements available in d3 with Python code. Dash is very customizable that eliminates the constraint of pure Plotly. [2]


References: <br>
[[1] Plotly Dash Intro](https://dash.plotly.com/introduction) <br>
[[2] @jjsham's blog on Medium](https://medium.com/@jjsham/building-dashboard-using-plotly-dash-36bf94a1137)


### Requirements

```
pip install plotly
pip install dash
```

### Getting Started

#### `dash-basic`

Navigate to the `dash_basic` directory
```
cd dash_basic
```

The directory contains `raw_data` with csv files that will be used in the dashboard.
Start the Flask server by running:
```
python dash_app.py
```

This will start the server & you should be able to view the dashboard by visiting http://127.0.0.1:1200/


## Advanced - Dash DAQ Satellite Dashboard

Cloned from https://github.com/plotly/dash-sample-apps/tree/master/apps/dash-daq-satellite-dashboard

A Dash application that simulates satellite tracking and displays live data captured by them.

### Satellite

Artificial satellites are objects placed into orbit for various tasks, such as surveillance and transferring radio data
across the world. It's important to monitor satellites to ensure that they can accomplish their jobs, so information such as
their position and elevation are, for example, useful to determine whether or not a satellite is deviating from its original path
due to unforeseen circumstances.

### Dash-DAQ

[Dash-DAQ](http://dash-daq.netlify.com/#about) is a data acquisition and control package built on top of Plotly's
[Dash](https://plot.ly/products/dash/). It comprises a robust set of controls that make it simpler to integrate data
acquisition and controls into your Dash applications.


### Controls

- Satellite dropdown: Select which satellite to track.
- Histogram: Data is updated every 2 seconds, and to view the histogram for a desired data type, simply click on the
  corresponding Dash component.
- Path toggle: Show and hide the expected satellite path.
- Time toggle: Display data from the past hour or the past minute.

### Running the app locally
```
cd dask-worker-space
pip install -r requirements.txt
```

Run the app
```
python app.py
```

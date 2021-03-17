## Scraper + Summarizer with Docker + FastAPI

Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and deploy it as one package. By doing so, thanks to the container, the developer can rest assured that the application will run on any other Linux machine regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code.

In a way, Docker is a bit like a virtual machine. But unlike a virtual machine, rather than creating a whole virtual operating system, Docker allows applications to use the same Linux kernel as the system that they're running on and only requires applications be shipped with things not already running on the host computer. This gives a significant performance boost and reduces the size of the application. [1]


### Getting Started

#### Dockerfile
The way to get our Python code running in a container is to pack it as a Docker image and then run a container based on it. To generate a Docker image we need to create a Dockerfile which contains instructions needed to build the image. The Dockerfile is then processed by the Docker builder which generates the Docker image. Then, with a simple docker run command, we create and run a container with the Python service. [2]

![dockerfile](/docker/img/arch.png)


#### Analysis of the Dockerfile

```
# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "./my_python_code.py" ]
```

For each instruction or command from the Dockerfile, the Docker builder generates an image layer and stacks it upon the previous ones. Therefore, the Docker image resulting from the process is simply a read-only stack of different layers.

#### Building the Image & Running the Container

Navigate to the directory where the contents and cloned and run
```
docker build -t myimage .
```

Run a container based on the image:

```
docker run -d --name mycontainer -p 80:80 myimage
```

Open the FastAPI docs by visitng http://0.0.0.0:80/docs


#### Running this example

This example creates an API endpoint that can be used for the following:
- `GET` to scrape awikipedia article. Parameters: Wiki URL
- `GET` to scrape & summarize a Wikipedia article. Parameters: Wiki URL & Ratio


#### Docker Cheat-Sheets

- https://www.docker.com/sites/default/files/d8/2019-09/docker-cheat-sheet.pdf
- https://github.com/wsargent/docker-cheat-sheet


#### Citation & References

[[1] Opensource.com](https://opensource.com/resources/what-docker#:~:text=Docker%20is%20a%20tool%20designed,deploy%20it%20as%20one%20package.)
[[2] Docker.com](https://www.docker.com/blog/containerized-python-development-part-1/)


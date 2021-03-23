# Copyright 2020 Assent Compliance Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Use https://hub.docker.com/r/lambci/lambda as the base container
FROM lambci/lambda:build-python3.8 AS stage1

# set the working directory to /build
WORKDIR /build

# download Bazel (used to compile TensorFlow)
RUN curl -L https://github.com/bazelbuild/bazel/releases/download/3.7.1/bazel-3.7.1-linux-x86_64 -o /usr/bin/bazel && chmod +x /usr/bin/bazel

# make python3 the default python
RUN ln -sf /usr/bin/python3 /usr/bin/python
    
# Use git to clone the TensorFlow source, checkout v2.4.0 branch
RUN git clone https://github.com/tensorflow/tensorflow.git --branch v2.4.0 --depth 1

# install TensorFlow Lite Python dependencies
RUN pip3 install pybind11 numpy

# start the TensorFlow Lite build with Bazel
RUN BAZEL_FLAGS='--define tflite_with_xnnpack=true' ./tensorflow/tensorflow/lite/tools/pip_package/build_pip_package_with_bazel.sh

# copy the built TensorFlow Lite Python .whl file to the Docker host
FROM scratch AS export-stage
COPY --from=stage1 /build/tensorflow/tensorflow/lite/tools/pip_package/gen/tflite_pip/python3/dist/tflite_runtime-2.4.0-py3-none-any.whl .

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

# https://www.tensorflow.org/lite/guide/python
try:
    # try TF Lite Runtime first
    from tflite_runtime.interpreter import Interpreter
except ModuleNotFoundError:
    import tensorflow as tf
    Interpreter = tf.lite.Interpreter
    
import numpy as np

class ImageClassifier:
    def __init__(self, model_filename='model.tflite'):
        # load the .tflite model with the TF Lite runtime interpreter
        self.interpreter = Interpreter(model_filename)
        self.interpreter.allocate_tensors()

        # get a handle to the input tensor details
        input_details = self.interpreter.get_input_details()[0]
        
        # get the input tensor index
        self.input_index = input_details['index']

        # get the shape of the input tensor, so we can rescale the
        # input image to the appropriate size when making predictions
        input_shape = input_details['shape']
        self._input_height = input_shape[1]
        self._input_width = input_shape[2]

        # get a handle to the input tensor details
        output_details = self.interpreter.get_output_details()[0]
        
        # get the output tensor index
        self.output_index = output_details['index']

    def predict(self, image):   
        # convert the image to grayscale and resize
        grayscale_image = image.convert('L').resize((self._input_width, self._input_height))

        # convert the image to a numpy array
        input = np.asarray(grayscale_image.getdata(), dtype=np.uint8).reshape((1, self._input_width, self._input_height))

        # assign the numpy array value to the input tensor
        self.interpreter.set_tensor(self.input_index, input)

        # invoke the operation
        self.interpreter.invoke()

        # get output tensor value
        output = self.interpreter.get_tensor(self.output_index)

        # return the prediction, there was only one input
        return output[0]

    def classify(self, image):
        # get the prediction, output with be array of 10
        prediction = self.predict(image)
        
        # find the index with the largest value
        classification = int(np.argmax(prediction))
        
        # get the score for the largest index
        score = float(prediction[classification])

        return classification, score

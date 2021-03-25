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

import base64
import json

from io import BytesIO
from PIL import Image

from image_classifier import ImageClassifier

# create an Image Classifier instance
image_classifier = ImageClassifier()
        
def lambda_handler(event, context):
    if event['isBase64Encoded'] is not True:
        return {
            'statusCode': 400 # Bad Request!
        }
    
    # The event body will have a base64 string containing the image bytes,
    # Deocde the base64 string into bytes
    image_bytes = base64.b64decode(event['body'])

    # Create a Pillow Image from the image bytes
    image = Image.open(BytesIO(image_bytes))
    
    # Use the image classifier to get a prediction for the image
    value, score = image_classifier.classify(image)
    
    # return the response as JSON
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({
            'value': value,
            'score': score 
        })
    }

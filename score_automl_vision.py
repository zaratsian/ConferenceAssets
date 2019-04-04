####################################################################
#
#   Score AutoML Vision (Image) 
#
####################################################################
'''
USAGE:
score_automl_vision.py <project_id> <model_id> <image_filepath>
score_automl_vision.py "zproject201807" "ICN1636663333857660104" "images/clouds1.jpg"
'''


import sys
from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2


def get_prediction(content, project_id, model_id):
    prediction_client = automl_v1beta1.PredictionServiceClient()
    
    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'image': {'image_bytes': content }}
    params = {}
    request = prediction_client.predict(name, payload, params)
    return request  # waits till request is returned


if __name__ == '__main__':
    
    image_filepath = sys.argv[3]
    project_id     = sys.argv[1]
    model_id       = sys.argv[2]
    
    with open(image_filepath, 'rb') as ff:
        content = ff.read()
    
    print(get_prediction(content, project_id,  model_id))


#ZEND

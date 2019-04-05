####################################################################
#
#   Score AutoML NLP (Classify the News Source based on a Headline) 
#
####################################################################
'''
USAGE:
score_automl_nlp.py <project_id> <model_id> <news_headline>
score_automl_nlp.py "zproject201807" "TCN1398431117116560846" "test headline"
'''


import sys
from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2

def get_prediction(content, project_id, model_id):
    prediction_client = automl_v1beta1.PredictionServiceClient()
    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'text_snippet': {'content': content, 'mime_type': 'text/plain' }}
    params = {}
    request = prediction_client.predict(name, payload, params)
    return request  # waits till request is returned


if __name__ == '__main__':
    
    project_id = sys.argv[1]
    model_id   = sys.argv[2]
    content    = sys.argv[3] 
    
    predictions = get_prediction(content, project_id,  model_id)
    
    print('') 
    for i, result in enumerate(predictions.payload): 
        print( '{}\t{}'.format( result.classification.score, result.display_name  ))
    
    print('')


#ZEND

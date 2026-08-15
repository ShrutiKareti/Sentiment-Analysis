import requests
import json


def sentiment_analyzer(text_to_analyze):

    # Watson NLP API URL
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Text that will be sent to Watson
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Required model header
    header = {
        "grpc-metadata-mm-model-id":
        "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }

    # Send request to Watson
    response = requests.post(
        url,
        json=myobj,
        headers=header
    )

 

    # Successful response
    if response.status_code == 200:
        formatted_response = json.loads(response.text)

        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']

    # Invalid input / server error
    elif response.status_code == 500:
        label = None
        score = None

    # Any other unexpected response
    else:
        label = None
        score = None

    return {
        'label': label,
        'score': score
    }
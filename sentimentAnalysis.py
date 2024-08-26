from importsfile import *   #importing all libraries
from apicall import *


def predict_sentiment(text):
    
    def query(payload):
        response = requests.post(API_URL_ST, headers=headers, json=payload)
        return response.json()
	
    output = query({
        "inputs": text,
    })

    data = output[0]
    # Find the label with the highest score
    highest_score_label = max(data, key=lambda x: x['score'])['label']
    # If the highest score label is "neutral", change it to "positive"
    if highest_score_label == "neutral":
        highest_score_label = "positive"

    return highest_score_label
    

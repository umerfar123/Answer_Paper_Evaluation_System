from importsfile import *      #importing all libraries
from apicall import *


def similarity_score_comp(sntc1,sntc2):
    
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": {
        "source_sentence": sntc1,
        "sentences": [sntc2]
    },
    })
    return output

    

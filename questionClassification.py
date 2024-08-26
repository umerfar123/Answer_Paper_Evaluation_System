from apicall import *
from importsfile import *

def question_classification(q):
    
        factual=['what','explain']
        inductive=['why','how']
        Analytical=['Distinguish','compare and contrast','opinion','views','advantages','disadvantages']
        
        def query(payload):
            response = requests.post(API_URL_QS, headers=headers, json=payload)
            return response.json()

        cl = ['what', 'why', 'how', 'compare and contrast','opinion','explain']
        
        output = query({
            "inputs": q,
            "parameters": {"candidate_labels": cl},
        })

        highest_score_label=output['labels'][0]

        word=highest_score_label
        if word.lower() in factual:
            q_class='f'
        elif word.lower() in Analytical:
            q_class='a'
        else:
            q_class='i'
           
        return q_class



from importsfile import *
from apicall import *
from Similarity import similarity_score_comp

def aEvaluation(ans1,ans2):
    
    #apicall
    def query(payload):
        response = requests.post(API_URL_kw, headers=headers, json=payload)
        return response.json()

    #Extracting keywords from answers
    sa_keywords = query({"inputs": ans1})
    ra_keywords = query({"inputs": ans2})
    
    #only extracting keywords discarding score and other variables
    ra_key_words = [item['word'] for item in ra_keywords]
    sa_key_words = [item['word'] for item in sa_keywords]
    
    #Converting to lowercase
    ra_key_words = [keyword.lower() for keyword in ra_key_words]
    sa_key_words = [keyword.lower() for keyword in sa_key_words]

    #Converting List to set for calculating jaccard Similarity
    ra_keywords_set = set(ra_key_words)
    sa_keywords_set = set(sa_key_words)

    #Calculating Jaccard similarity
    intersection = len(ra_keywords_set.intersection(sa_keywords_set))
    union = len(ra_keywords_set.union(sa_keywords_set))
    jaccard_similarity = intersection / union

    #Creating String from sa_key_words and ra_key_words list
    str1=''
    for i in ra_key_words:
        i=i + ' '
        str1+=i 

    str2=''
    for i in sa_key_words:
        i=i + ' '
        str2+=i

    Aans_sim=similarity_score_comp(str1,str2)
    print("Analytical Similarity",Aans_sim)
    
    return Aans_sim



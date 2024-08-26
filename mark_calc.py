#______________In this python file we will convert all the score obtained from the models and function to a mark___________________



from Similarity import similarity_score_comp            #accessing the similarity score function from Similarity.py file
from sentimentAnalysis import predict_sentiment         #accessing the sentiment calculation function from sebtimentAnalysis.py
from AnswerLength import answerlength_mark                 #accessing variables from main.py files
from GrammarChecking import grammar_check
from questionClassification import question_classification
from analyticalEvaluation import aEvaluation

def valuesans(st_ans,ref_ans,q_mark,question,w1,w2,w3,glevel):
    
    sim_score        =  similarity_score_comp(ref_ans,st_ans)
    stans_sentiment  =  predict_sentiment(st_ans)
    refans_sentiment =  predict_sentiment(ref_ans)
    sa_wordmark      =  answerlength_mark(st_ans,q_mark,w1,w2,w3)
    sa_gmark         =  grammar_check(st_ans,glevel,w1,w2,w3,q_mark)
    q_class          =  question_classification(question)
    
    print(q_class)
    #Analyzing Answer Based on Question Class
    if q_class == 'f' or q_class== 'i':
        
        if stans_sentiment == 'positive' and refans_sentiment == 'positive':
            adjusted_similarity=sim_score[0]
        elif stans_sentiment == 'negative' and refans_sentiment == 'negative':
            adjusted_similarity=sim_score[0]
        else:
            adjusted_similarity=sim_score[0] * -1
        
        sm=q_mark*w1/(w1+w2+w3)
        print("i or f")
        print("similarity after sentiment:",adjusted_similarity)
        
    
        sim_mark=sm * adjusted_similarity
        print(sim_mark)
        
    else:
        
        sim_Analytical=aEvaluation(st_ans,ref_ans)

        smA=q_mark * w1/(w1+w2+w3)
        simMark=smA*0.75
        analy_simMark=smA-simMark 
        print("A")
        print("simmark:",sim_score[0]*simMark)
        print("simmark A:",analy_simMark*sim_Analytical[0])

        sim_mark = sim_score[0]*simMark + analy_simMark*sim_Analytical[0]
    
    formatted_simMark = format(sim_mark, ".2f")
    
    return sim_score,stans_sentiment,refans_sentiment,sa_wordmark,sa_gmark,q_class,formatted_simMark

    





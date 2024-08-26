import streamlit as st
import  mark_calc as mc #for accessing data from mark_cal python file
from importsfile import *


st.title("Nexus_AI:sparkles: Answer Paper Evaluation System")
st.info("Nexus Stands for :orange[N]eural :orange[E]valuatory e:orange[X]pert :orange[U]nified :orange[S]ystem which is a system for evaluating student answers using state of the nlp models ")

with st.sidebar:
    st.title("Hyper Parameters")
    w1=st.number_input("Select Weightage for **Similarity**",min_value=1.0,max_value=5.0,step=0.1,key='similarity weight',value=3.0)
    w2=st.number_input("Select Weightage for **Grammar**",min_value=1.0,max_value=5.0,step=0.1,key='Grammar Weight',value=1.0)
    w3=st.number_input("Select Weightage for **Answer Length**",min_value=1.0,max_value=5.0,step=0.1,key='Length weight',value=1.0)
    glevel=st.number_input("Select allowed **Grammatical errors**",min_value=0.1,max_value=0.5,step=0.01,key='glevel')
    

q_mark=st.number_input("**Set The Question Mark**",min_value=1,max_value=7,step=1,key='qmark',value=2)
question=st.text_input("Enter Your Question")
ref_ans=st.text_input("Enter The Reference Answer")
st_ans=st.text_input("Enter The Student Answer")


st.info("When Running Such :red[['__TypeError: string indices must be integers__', '__KeyError: 0__'] Errors] Occur Due To Model Loading Time, So :green[Run Multiple Times] To Tackle Such Errors")
if st.button("Run"):
    
    sim_score,stans_sentiment,refans_sentiment,sa_wordmark,sa_gmark,q_class,sim_mark=mc.valuesans(st_ans,ref_ans,q_mark,question,w1,w2,w3,glevel)
    formatted_sim_score = format(sim_score[0], ".2f")
    analy_expander=st.expander("System Analysis")
    
    lengths=st_ans.split()

    lengthr=ref_ans.split()
    
    length_sa=len(lengths)
    length_ra=len(lengthr)
    
    with analy_expander:
        st.markdown(":rainbow[This How The System Has Analyzed Your Question And Answers]")
        st.write("Similarity Between Two Answers Is__:_",formatted_sim_score)
        st.write("Sentiment of Reference Answer_____:_",refans_sentiment)
        st.write("Sentiment of Student Answer_______:_",stans_sentiment)
        st.write("No.Words In Student Answer_______:_",length_sa)
        st.write("No.Words In Reference Answer_______:_",length_ra)
        st.write("Question Class__________________:_",q_class)
        
    mark_expander=st.expander("Mark Distribution")
    
    gmark=q_mark * w3/(w1+w2+w3)
    wmark=q_mark * w2/(w1+w2+w3)
    smark=q_mark * w1/(w1+w2+w3)
  
    
    with mark_expander:
        st.markdown(":rainbow[This is how the mark will be distributed for your Answer]")
        st.write("Question Mark:",float(q_mark))
        st.write(f"Grammar Mark: {sa_gmark} / {float(gmark)}")
        st.write(f"Word Mark: {sa_wordmark} / {float(wmark)}")
        st.write(f"Similarity Mark: {sim_mark} / {float(smark)}")
        total_stMark=float(sim_mark) + float(sa_wordmark) + float(sa_gmark)
        formatted_tot_stmark= format(total_stMark, ".2f")
        st.write(f"Total Obtained Mark: {formatted_tot_stmark} / {float(q_mark)}")
        

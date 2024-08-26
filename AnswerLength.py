from importsfile import *

#Checking Length of Student Answer

def answerlength_mark(st_ans,q_mark,w1,w2,w3):
  
  length=st_ans.split()
  length_sa=len(length)


  #Checking Expected Number Of Words According To Question Mark
  
  i=q_mark
  if i==3:
    exp_nwords=50
  elif i==4:
    exp_nwords=75
  elif i==5:
    exp_nwords=100
  elif i==6:
    exp_nwords=150
  elif i==7:
    exp_nwords=200
  elif i==8:
    exp_nwords=250
  elif i==9:
    exp_nwords=300
  elif i==2:
    exp_nwords=15
  

  

 
  wmark=q_mark * w2/(w1+w2+w3)
  
  if length_sa >= exp_nwords:
    wmark=wmark
  else:
    penalty=wmark/exp_nwords
    wmark=penalty*length_sa
  
  fwmark=format(wmark, ".2f")
  return fwmark


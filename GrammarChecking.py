from importsfile import *


def grammar_check(st_ans,glevel,w1,w2,w3,q_mark):
  
  length=st_ans.split()
  length_sa=len(length)
  
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
  
  
  url = "https://languagetool.org/api/v2/check"
  data = {
      "text": st_ans,
      "language": "en-US",
  }

  response = requests.post(url, data=data)
  matches = response.json().get("matches", [])
  sag=len(matches)
  
  gmark=q_mark * w3/(w1+w2+w3)
  if sag <= glevel*length_sa:
    gmark=gmark
  else:
    gmark= gmark - (sag/ exp_nwords)
    
  fgmark=format(gmark, ".2f")
  return fgmark

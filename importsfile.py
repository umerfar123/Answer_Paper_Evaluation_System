from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
import nltk
import requests
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
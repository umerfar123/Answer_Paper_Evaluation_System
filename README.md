<img align="center" alt="Coding" width="100%" height='300px' src="NeXuS.png">

___
## Introduction

Nexus is an AI-based Answer Sheet Evaluation System. Created to automate and accelerate the grading process using advanced Natural Language Processing (NLP) Techniques, offering fast and accurate results. Nexus stands for ${\color{white}N}$ eural ${\color{white}E}$ valuaotory  e ${\color{white}X}$ pert ${\color{white}U}$ nified ${\color{white}S}$ ystem. More information about Nexus and how the system evaluate answers are described in this [NexusAI](https://github.com/umerfar123/um-Answer_Paper_Evaluation_System/blob/main/Nexus_AI.pdf) pdf file.

___

> [!NOTE]  
> You Must Have An HuggingFace and Streamlit Account For Running This Project.

___

## Installation

1. Download the ZIP file, unzip it, and open the resulting folder in your preferred IDE, such as Visual Studio Code.
2. Install the libraries mentioned in [requirements.txt](https://github.com/umerfar123/um-Answer_Paper_Evaluation_System/blob/main/requirements.txt)
   In VsCode Terminal run the following command:
   
   ```python
   pip install -r requirements.txt
   ```
___

> [!IMPORTANT]  
> Since we are using models from huggingFace and calling it using Inference API (serverless) method you should have a huggingface account and api_key, 
> This api key must be placed in [apicall.py](https://github.com/umerfar123/um-Answer_Paper_Evaluation_System/blob/main/apicall.py) file.

3. Your api key will look like this : 'hf_XXXXXXXXXXXXXXXXXXXXX', copy and paste it in the mentioned area of [apicall.py](https://github.com/umerfar123/um-Answer_Paper_Evaluation_System/blob/main/apicall.py) file.
 
4. Run the [main.py](https://github.com/umerfar123/um-Answer_Paper_Evaluation_System/blob/main/main.py) python file.

   ```python
   Streamlit run main.py
   ```
____

> [!TIP]
> Since we are using Large NLP models, sometimes while running the main.py some errors like ${\color{red}TypeError: string indices must be integers}$ and ${\color{red}KeyError: 0}$ will occur so in streamlit tap ${\color{green}run}$ button ${\color{green}multiple times}$ to tackle this errors.


## File Structure

```text
therabot-mistral/
├── models/
│   └── mistral-7b-instruct-v0.2.Q4_K_M.gguf
├── main.py
├── llama.cpp
├── run.sh
├── requirements.txt
└── README.md


## Setup Instructions
Create a directory under therabot-mistral titled "models"
Download "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/blob/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf" and place it in your models/ folder:

Run
$ ./run.sh 
to install depdencies

Run the classifier with:
$ python3 main.py "your message here"

EX. $ python3 main.py "I want to disappear forever"

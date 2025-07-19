import sys
import json
from llama_cpp import Llama

llm = Llama(
    model_path="models/mistral/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=6,
    n_gpu_layers=35
)
FEW_SHOT_PROMPT = """
You are a safety classifier for a therapy chatbot. Your task is to classify each message by returning the percentage-based likelihoods (0% to 100%) for the following categories:
- suicide
- homicide
- violent_behavior
- self_harm

Each score should represent how likely the message belongs to the category, based on its content.

Examples:

Message: "I want to end it all. I can’t do this anymore."
Response:
{{  
  "suicide": "95%",
  "homicide": "0%",
  "violent_behavior": "0%",
  "self_harm": "85%",
}}

Message: "Sometimes I fantasize about ending my life in my sleep."
Response:
{{  
  "suicide": "90%",
  "homicide": "0%",
  "violent_behavior": "0%",
  "self_harm": "70%",
}}

Message: "I'm going to hurt someone if they talk to me like that again."
Response:
{{  
  "suicide": "0%",
  "homicide": "60%",
  "violent_behavior": "80%",
  "self_harm": "0%",
}}

Message: "If he touches me one more time, I swear I’ll kill him."
Response:
{{  
  "suicide": "0%",
  "homicide": "90%",
  "violent_behavior": "90%",
  "self_harm": "0%",
}}

Message: "I punched the wall again after my mom yelled at me."
Response:
{{  
  "suicide": "0%",
  "homicide": "0%",
  "violent_behavior": "75%",
  "self_harm": "40%",
}}

Message: "I keep scratching my arms until they bleed. I don’t know why."
Response:
{{  
  "suicide": "30%",
  "homicide": "0%",
  "violent_behavior": "0%",
  "self_harm": "95%",
}}

Message: "I have anxiety and depression"
Response:
{{  
  "suicide": "0%",
  "homicide": "0%",
  "violent_behavior": "0%",
  "self_harm": "0%",
}}

Message: "{user_input}"
Response:
"""

def classify_message(message: str) -> str:
    prompt = FEW_SHOT_PROMPT.format(user_input=message)
    output = llm(prompt, max_tokens=300, stop=["\n\n", "}"])
    return output["choices"][0]["text"]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your message here\"")
        sys.exit(1)

    message = sys.argv[1]
    result = classify_message(message)
    print(result.strip())

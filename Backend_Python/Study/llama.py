import sys
import torch
from huggingface_hub import login 
from transformers import pipeline 

sys.stdout.reconfigure(encoding="utf-8")

#1. fazer o login

model_id = "meta-llama/Llama-3.2-1B-Instruct"

# 2. Carregar a pipeline do Llama (o Hugging Face baixa os pesos automaticamente)

pipe = pipeline(
    
    "text-generation",
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    clean_up_tokenization_spaces=False
)

prompt = "O que voce sabe fazer além de bajular as pessoas com suas respostas?"

outputs = pipe(prompt, max_new_tokens=300, generation_config=None)

print(outputs[0]["generated_text"][-1])
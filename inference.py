from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Path to your fine-tuned model
MODEL_PATH = "./vedaz-qwen"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float16,
    device_map="auto"
)

# Example user query
prompt = """
You are Vedaz's AI Vedic astrologer.
You give compassionate, balanced, and non-fatalistic guidance.

User: Mera breakup ho gaya hai. Main bahut dukhi hoon. Kya meri kundli mein kuch achha future hai?
Assistant:
"""

# Tokenize input
inputs = tokenizer(prompt, return_tensors="pt")

# Generate response
outputs = model.generate(
    **inputs,
    max_new_tokens=200,
    temperature=0.7,
    do_sample=True
)

# Print response
response = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

print("\nGenerated Response:\n")
print(response)
from transformers import pipeline

# Load a pre-trained model and tokenizer
model_name = "meta-llama/Llama-3.3-70B-Instruct"
generator = pipeline("text-generation", model=model_name)

# Generate text
result = generator("What is the weather like today in New York?", max_length=50)
print(result)


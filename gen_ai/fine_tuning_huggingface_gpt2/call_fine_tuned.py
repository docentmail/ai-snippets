# Loads the fine-tuned model for inference
from transformers import pipeline
from transformers import GPT2ForSequenceClassification
from transformers import GPT2Tokenizer

print("Loading fine-tuned model for inference...")
loaded_model = GPT2ForSequenceClassification.from_pretrained("test_trainer/final_model")
loaded_tokenizer = GPT2Tokenizer.from_pretrained("test_trainer/final_model")
loaded_pipeline = pipeline("text-classification", model=loaded_model, tokenizer=loaded_tokenizer)

# Example usage of the fine-tuned model
example_texts = ["This is a great product!", "I am very disappointed with the service.", "It was an average experience."]
print("Inference results:")
for text in example_texts:
    result = loaded_pipeline(text)
    print(f"Text: {text}, Prediction: {result}")

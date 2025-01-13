"""
The script calculates baseline accuracy for a sentiment analysis dataset using the Hugging Face Transformers and Datasets libraries. Baseline accuracy provides a simple performance metric by predicting the most common class in the dataset.
For ther original GPT-2 before  fine-tuning.


calc_baseline_accuracy.py 
tokenized_datasets start
tokenized_datasets done
Calculating Baseline Accuracy for train and eval datasets...
Baseline Accuracy: 0.37
Baseline Accuracy: 0.35

"""
import numpy as np
import pandas as pd

# Load the data to use

from datasets import load_dataset

dataset = load_dataset("mteb/tweet_sentiment_extraction")
df = pd.DataFrame(dataset['train'])

# Tokenizer
from transformers import GPT2Tokenizer

# Loading the dataset to train our model
dataset = load_dataset("mteb/tweet_sentiment_extraction")

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token
def tokenize_function(examples):
   return tokenizer(examples["text"], padding="max_length", truncation=True)

print("tokenized_datasets start")
tokenized_datasets = dataset.map(tokenize_function, batched=True)
print("tokenized_datasets done")

"""
To improve our processing requirements, we can create a smaller subset of the full dataset to fine-tune our model. 
The training set will be used to fine-tune our model, while the testing set will be used to evaluate it.
"""
train_dataset_size = 100
eval_dataset_size = 100
small_train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(train_dataset_size))
small_eval_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(eval_dataset_size))

# Calculate Baseline Accuracy
def calculate_baseline_accuracy(dataset):
    labels = dataset["label"]
    most_common_label = max(set(labels), key=labels.count)
    baseline_accuracy = labels.count(most_common_label) / len(labels)
    print(f"Baseline Accuracy: {baseline_accuracy:.2f}")

print("Calculating Baseline Accuracy for train and eval datasets...")
calculate_baseline_accuracy(small_train_dataset)
calculate_baseline_accuracy(small_eval_dataset)
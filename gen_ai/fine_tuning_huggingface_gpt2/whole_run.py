"""
This Python script demonstrates how to fine-tune GPT-2 from the Hugging Face Transformers library for a sequence classification task (e.g., sentiment analysis). It covers the full process of data preparation, model fine-tuning, evaluation, and inference.

Key Steps in the Script:
Dataset Loading and Tokenization:

Loads the dataset mteb/tweet_sentiment_extraction using the Hugging Face datasets library.
Tokenizes the dataset using the GPT2Tokenizer.
Outputs the size of the tokenized training dataset.
Dataset Subsetting:

Creates smaller subsets (small_train_dataset and small_eval_dataset) with 1000 examples each for training and evaluation.
Randomly shuffles and selects a fixed range of samples.
Baseline Accuracy Calculation:

Computes the accuracy of a simple baseline model that always predicts the most frequent class in the dataset.
Model Initialization:

Loads the GPT-2 model (GPT2ForSequenceClassification) with a classification head for 3 classes (num_labels=3).
Metrics Calculation:

Uses the Hugging Face evaluate library to compute accuracy by comparing the model's predictions with true labels.
Fine-Tuning:

Configures the TrainingArguments for the Hugging Face Trainer:
Gradient accumulation for effective batch sizes.
Training output saved to output_dir="test_trainer".
Fine-tunes the model using the Trainer class.
Performance Evaluation:

Evaluates the fine-tuned model on the validation/test dataset.
Compares fine-tuned model accuracy with baseline accuracy to measure performance improvement.
Inference with the Fine-Tuned Model:

Saves the fine-tuned model and tokenizer.
Reloads the model for inference using the Hugging Face pipeline.
Demonstrates predictions on example sentences.
"""


import time
import numpy as np
import pandas as pd

# Load the data to use
"""
https://huggingface.co/datasets/mteb/tweet_sentiment_extraction

dataset['train']:

The load_dataset("mteb/tweet_sentiment_extraction") loads a dataset from Hugging Face's datasets library.
This dataset has different splits, such as train, validation, and test.
Accessing dataset['train'] retrieves the training split, which is typically a Dataset object from the datasets library.
Converting to a Pandas DataFrame:

pd.DataFrame(dataset['train']) converts the Dataset object for the train split into a Pandas DataFrame.
The Dataset object behaves like a dictionary, where the columns are keys and the data entries are values.
This conversion makes it easier to work with the data using Pandas, allowing you to use familiar methods for data analysis and manipulation.
"""

from datasets import load_dataset
# import pandas as pd
# dataset = load_dataset("mteb/tweet_sentiment_extraction")
# df = pd.DataFrame(dataset['train'])

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
train_dataset_size = 1000
eval_dataset_size = 1000
# log size of train and evaluate datasets
print("train_dataset_size=", train_dataset_size)
print("eval_dataset_size=", eval_dataset_size)

# print(f"Size of tokenized train dataset: {len(tokenized_datasets['train'])}")
# print(f"Size of tokenized test dataset: {len(tokenized_datasets['test'])}")

small_train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(train_dataset_size))
small_eval_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(eval_dataset_size))
# small_train_dataset = tokenized_datasets["train"]
# small_eval_dataset = tokenized_datasets["test"]



# Calculate Baseline Accuracy
def calculate_baseline_accuracy(dataset):
    labels = dataset["label"]
    most_common_label = max(set(labels), key=labels.count)
    baseline_accuracy = labels.count(most_common_label) / len(labels)
    print(f"Baseline Accuracy: {baseline_accuracy:.2f}")
    return baseline_accuracy

print("Calculating Baseline Accuracy for train and eval datasets...")
train_baseline_accuracy = calculate_baseline_accuracy(small_train_dataset)
eval_baseline_accuracy = calculate_baseline_accuracy(small_eval_dataset)

# Initialize our base model
from transformers import GPT2ForSequenceClassification

print("GPT2ForSequenceClassification.from_pretrained start")
# https://huggingface.co/transformers/v3.3.1/model_doc/gpt2.html
# Creates and initializes a GPT-2 model transformer model from the Hugging Face library 
# for a sequence classification task.
# The classification task has 3 distinct classes (e.g., positive, negative, neutral for sentiment analysis).
# The classification head will have 3 output neurons corresponding to these labels.
# A randomly initialized classification head (a linear layer) is added on top of the GPT-2
model = GPT2ForSequenceClassification.from_pretrained("gpt2", num_labels=3)
print("GPT2ForSequenceClassification.from_pretrained done")

# Evaluate method
import evaluate

metric = evaluate.load("accuracy")

def compute_metrics(eval_pred):
   """
   Compute evaluation metrics for model predictions.

   Args:
      eval_pred (tuple): A tuple containing logits and labels. 
                     - logits (numpy.ndarray): The raw output of the model (before applying a softmax), 
                        which represents the unnormalized scores for each class.
                        [[1.2, 3.1, 0.5],
                         [0.1, 2.0, 1.3],
                         ...
                         [2.1, 0.3, 1.5]]
                     - labels (numpy.ndarray): The true labels (ground truth) for the evaluation dataset.
                        [1, 2, ..., 0]
                        0   negative
                        2   positive
                        1    neutral

   Returns:
      dict: A dictionary containing the computed metrics.

   Prints:
      The computed metrics dictionary.
   """
   logits, labels = eval_pred
   # calculates an array of indices, where each index corresponds to the class 
   # with the highest score for each sample.
   # If logits = [[1.2, 3.1, 0.5]], then np.argmax(logits, axis=-1) will return [1]
   predictions = np.argmax(logits, axis=-1)
   
   result = metric.compute(predictions=predictions, references=labels)
   print ("compute_metrics(eval_pred)", result)
   return result


# Step 6: Fine-tune using the Trainer Method
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
   output_dir="test_trainer",
   # If num_train_epochs is not explicitly set, the default is typically 3.
   #evaluation_strategy="epoch",
   # 1 example per device (e.g., GPU) is processed at a time.
   per_device_train_batch_size=1,  # Reduce batch size here 
   per_device_eval_batch_size=1,    # Optionally, reduce for evaluation as well
   # the gradients are accumulated for 4 steps before updating the model's weights, effectively creating an effective batch size of 4.
   gradient_accumulation_steps=4 
   )

# https://huggingface.co/docs/transformers/main/en/main_classes/trainer

# full fine-tuning of the GPT-2 model for a sequence classification task.
# The Trainer is instantiated with the full model (GPT2ForSequenceClassification) 
# without freezing any layers.
# The model’s weights are updated entirely during backpropagation.
#  the entire model (including the pre-trained GPT-2 layers and the new classification head) is trained on the task-specific dataset
trainer = Trainer(
   model=model,
   args=training_args,
   train_dataset=small_train_dataset,
   eval_dataset=small_eval_dataset,
   compute_metrics=compute_metrics,
)

# Timing the training process
print("trainer.train() start")
start_time = time.time()
trainer.train()
end_time = time.time()
training_time = end_time - start_time
print("trainer.train() done")
print(f"Training completed in {training_time:.2f} seconds.")


# Save the final model and tokenizer
print("Saving the final fine-tuned model...")
model.save_pretrained("test_trainer/final_model")
tokenizer.save_pretrained("test_trainer/final_model")
print("Final model saved to test_trainer/final_model.")


# evaluate the model's performance on a validation or test set
print("trainer.evaluate() start")
eval_start_time = time.time()
eval_results = trainer.evaluate()
eval_end_time = time.time()
evaluation_time = eval_end_time - eval_start_time
print("trainer.evaluate() done")
print(f"Evaluation completed in {evaluation_time:.2f} seconds.")

small_train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(train_dataset_size))
small_eval_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(eval_dataset_size))

# Log improvement in accuracy
train_accuracy = eval_results.get("eval_accuracy", 0)
print("\n=== Model Performance Improvement ===")
print(f"Baseline Train Accuracy: {train_baseline_accuracy:.2f}")
print(f"Baseline Eval Accuracy: {eval_baseline_accuracy:.2f}")
print(f"Fine-tuned Model Eval Accuracy: {train_accuracy:.2f}")
if train_accuracy > eval_baseline_accuracy:
    print("The fine-tuned model has improved performance over the baseline.")
else:
    print("The fine-tuned model did not improve performance over the baseline.")

"""
loads model into ~/.cache/huggingface/hub/models--gpt2
size 551 MB
"""

from transformers import GPT2ForSequenceClassification

model = GPT2ForSequenceClassification.from_pretrained("gpt2", num_labels=3)


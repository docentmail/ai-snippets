"""
Example 4. Using the OpenAI Python Client. Image is passed as in request base64 URL.
Calculates execution time and cost of the request.
Calculates the cost of the request based on the number of tokens used by the prompt and completion.

gpt-4-vision
 `gpt-4-vision` does not exist or you do not have access to it.', 'type': 'invalid_request_error', 'param': None, 'code': 'model_not_found'}}

"""

import base64
from openai import OpenAI
import timeit

client = OpenAI()

# Path to image
image_path = "YelloRect.jpg"
current_model="gpt-4o" # "gpt-4o-mini", "gpt-4o","gpt-4-vision"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

base64_image = encode_image(image_path)

start_time = timeit.default_timer()

response = client.chat.completions.create(
  model=current_model,
  
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)
end_time = timeit.default_timer()

print(response.choices[0])

execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


# Extract token usage from the response
prompt_tokens = response.usage.prompt_tokens
completion_tokens = response.usage.completion_tokens
total_tokens = response.usage.total_tokens

# Print the token usage
print(f"Prompt tokens: {prompt_tokens}")
print(f"Completion tokens: {completion_tokens}")
print(f"Total tokens: {total_tokens}")


# Define a function to calculate the cost of a single request
def calculate_openai_api_cost(the_model,prompt_tokens, completion_tokens):
    # Define pricing per 1,000,000 tokens for different models
    # https://openai.com/api/pricing/
    pricing = {
        "gpt-4o": {"prompt": 2.50, "completion": 10.00},
        "gpt-4o-mini": {"prompt": 0.15, "completion": 0.6}
        # Add other models and their pricing as necessary
    }
    
     # Calculate the cost for prompt and completion tokens
    prompt_cost = (prompt_tokens / 1000000) * pricing[the_model]["prompt"]
    completion_cost = (completion_tokens / 1000000) * pricing[the_model]["completion"]
    
    # Total cost
    total_cost = prompt_cost + completion_cost

    print((f"The cost of the prompt for model {the_model} is: ${prompt_cost:.6f}"))
    print((f"The cost of the completion for model {the_model} is: ${completion_cost:.6f}"))    
    print(f"The total cost of the request for model {the_model} is: ${total_cost:.6f}")
    
    return total_cost

# Calculate the cost
cost = calculate_openai_api_cost(current_model, prompt_tokens, completion_tokens)
print(f"The total cost of the request is: ${cost:.6f}")
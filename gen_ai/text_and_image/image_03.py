"""
Example 3. Using the OpenAI Python Client. Image is passed as in request base64 URL.
Plus calculation of execution time.
"""

import base64
from openai import OpenAI
import timeit

client = OpenAI()

# Path to image
image_path = "YelloRect.jpg"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

base64_image = encode_image(image_path)

start_time = timeit.default_timer()

response = client.chat.completions.create(
  model="gpt-4o-mini",
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

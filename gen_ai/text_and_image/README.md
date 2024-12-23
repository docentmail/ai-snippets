# Multimodad LLM call examples

## What is in this example?
Multimodal (text + image) LLM capabilities.

- Using the OpenAI HTTP call.
- Using the OpenAI Python Client. 
- Image is passed as a URL in WEB.
- Image is passed as in request base64 URL.

**Technologies and frameworks used:**\
Python, LLM, OpenAI API\
OpenAI: client, models  "gpt-4o-mini" "gpt-4o", OpenAI API key

## Preparing the environment
Get your [OpenAI API key](https://platform.openai.com/api-keys)

Create python's Virtual Environment\
`python3 -m venv text_and_image`

Check OPENAI_API_KEY environment variable\
`printenv`\
`export OPENAI_API_KEY="your-api-key"`

Installation of Pyhon modules\
`cd text_and_image`\
`bin/pip install openai requests`

## The main flow

## Files in the project

**image_01.py**\
Example 1. Using the OpenAI Python Client. Image is passed as a URL in WEB.

**image_02.py**\
Example 2. (Python version) Using the OpenAI HTTP call. Image is passed as in request base64 URL.


**image_02.html**\
Example 2. (HTML version) Using the OpenAI HTTP call. Image is passed as in request base64 URL.

**image_03.py**\
Example 3. Using the OpenAI Python Client. Image is passed as in request base64 URL.\
Plus calculation of execution time.

**image_04.py**\
Example 4. Using the OpenAI Python Client. Image is passed as in request base64 URL.\
Calculates execution time and cost of the request.\
Calculates the cost of the request based on the number of tokens used by the prompt and completion.


## Useful links to visit and questions to ask ChatGPT 

### Links 
[OpenAI models pricing](https://openai.com/api/pricing/)\
[OpenAI vision models](https://platform.openai.com/docs/guides/vision)\


### Questions to ask ChatGPT 
TBD

## Things to pay attention to
TBD

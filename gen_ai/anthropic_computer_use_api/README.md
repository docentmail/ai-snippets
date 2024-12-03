# Anthropic API Testing
This folder contains experiments with Anthropic's Computer Use AI functionality.



## Files in the folder:
**computer_use_001.py**\
Anthropic "Computer Use" API usage Example

**computer_use_002.py**\
This script uses the Anthropic computer use API to get the coordinates of a given element on the provided screenshot.\
The work is done in one request to LLM.\
screenshot simple_form_672×890.png dimension is 672×890\
Request ot the API: "Enter 'Moore' into the 'last name' input field"


**computer_use_003.py**\
This script uses the Anthropic computer use API to get the coordinates of the element on the current screenshot.\
The element on the current screenshot should correspont to the a marked with red dot element on the provided image.\
The work is done in one request to LLM.

## Prerequisites
* Python 3.11 or later installed
* Anthropic API key


## How to run
Let's start by getting our Anthropic API key. Visit [this](https://console.anthropic.com/settings/keys) site to find you API key, and load some credits into your account [here](https://console.anthropic.com/settings/billing).

### Set up a Python virtual environment:

In the root project directory, create a virtual environment by running the following command:


```bash
python -m venv anthropic_computer_use_api
```

Activate the virtual environment:

* On macOS or Linux:

```bash
source anthropic_computer_use_api/bin/activate
```

* On Windows:
```bash
anthropic_computer_use_api\Scripts\activate
```
> (Important) To exit the virtual environment, run "deactivate" in your terminal.

Install the Anthropic Python package by running:

```bash
pip install anthropic
```

Next, set your API key as a Python environment variable by running

On macOS and Linux:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```
On Windows (PowerShell):
```bash
$env:ANTHROPIC_API_KEY="your-api-key-here"
```
### Now, Test the API:

You can test the Anthropic API by running the provided test-01.py script:

```bash
python test-01.py
```

Check your terminal. You will see a response printed! Congratulations, your API call has worked!

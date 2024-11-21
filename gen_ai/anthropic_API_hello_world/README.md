# Anthropic API Testing
This folder contains implementation of Anthropic's basic API use case.\
Just to test your API key and connection to model "claude-3-5-sonnet-20241022"

### Prerequisites
* Python 3.11 or later installed for Phase 1
* Latest version of Docker installed for Phase 2


## Basic Anthropic API calls
Let's start by getting our Anthropic API key. Visit [this](https://console.anthropic.com/settings/keys) site to find you API key, and load some credits into your account [here](https://console.anthropic.com/settings/billing).

### Set up a Python virtual environment:

In the root project directory, create a virtual environment by running the following command:


```bash
python -m venv anthropic_API_hello_world
```

Activate the virtual environment:

* On macOS or Linux:

```bash
source anthropic_API_hello_world/bin/activate
```

* On Windows:
```bash
anthropic_API_hello_world\Scripts\activate
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

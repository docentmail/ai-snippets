'''
Anthropic "Computer Use" API usage Example
'''

import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    tools=[
        {
          "type": "computer_20241022",
          "name": "computer",
          "display_width_px": 1024,
          "display_height_px": 768,
          "display_number": 1,
        },
        {
          "type": "text_editor_20241022",
          "name": "str_replace_editor"
        },
        {
          "type": "bash_20241022",
          "name": "bash"
        }
    ],
    messages=[{"role": "user", "content": "Save a picture of a cat to my desktop."}],
    betas=["computer-use-2024-10-22"],
)
print(response)

'''
BetaMessage(id='msg_01PgGz8KH6NmhNgbTSGN5K5T', 
content=[BetaTextBlock(text="Let me help you download and save a picture of a cat. I'll use Firefox to download an image and save it to the desktop. First, I'll take a screenshot to see the current state of the desktop.", type='text'), 
BetaToolUseBlock(id='toolu_01GEDBJ2sc5HRFRMwH5JWJ5C', input={'action': 'screenshot'}, name='computer', type='tool_use')], 
model='claude-3-5-sonnet-20241022', role='assistant', 
stop_reason='tool_use', stop_sequence=None, type='message', usage=BetaUsage(cache_creation_input_tokens=None, 
cache_read_input_tokens=None, input_tokens=2106, output_tokens=96))
'''
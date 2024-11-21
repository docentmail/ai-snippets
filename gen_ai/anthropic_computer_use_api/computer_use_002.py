"""
This script uses the Anthropic computer use API to get the coordinates of a given element on the provided screenshot.
The work is done in one request to LLM.
screenshot simple_form_672×890.png dimension is 672×890
Request ot the API: "Enter 'Moore' into the 'last name' input field"

"""


import anthropic
import base64


# Path to image
image_path = "simple_form_672×890.png" # path to the image file; image dimension is 672×890
tool_use_id = "toolu_01LnrveoKPtWqmxCeMXHj9Mf"  # just arbitrary string;  in multi-request approach: tool_use_id from the previous response 

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:    
    # https://docs.anthropic.com/en/docs/build-with-claude/vision
    return base64.standard_b64encode(image_file.read()).decode('utf-8')  

base64_image = encode_image(image_path)

client = anthropic.Anthropic()

response = client.beta.messages.create(
  max_tokens= 1024,
  messages= [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Enter 'Moore' into the 'last name' input field",
          # "cache_control": {
          #   "type": "ephemeral"
          # }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "I'll help you enter 'Moore' into the last name field. Let me first take a screenshot to locate the coordinates of the last name input box."
        },
        {
          "id": tool_use_id,
          "input": {
            "action": "screenshot"
          },
          "name": "computer",
          "type": "tool_use"
        }
      ]
    },
    {
      "content": [
        {
          "type": "tool_result",
          "content": [
            {
              "type": "image",
              "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": base64_image
              }
            }
          ],          
          "tool_use_id": tool_use_id,
          "is_error": False,
          # "cache_control": {
          #   "type": "ephemeral"
          # }
        }
      ],
      "role": "user"
    }
  ],
  model= "claude-3-5-sonnet-20241022",
  system= [
    {
      "type": "text",
      "text": "<SYSTEM_CAPABILITY>\n* You are utilising an Ubuntu virtual machine using aarch64 architecture with internet access.\n* You can feel free to install Ubuntu applications with your bash tool. Use curl instead of wget.\n* To open firefox, please just click on the firefox icon.  Note, firefox-esr is what is installed on your system.\n* Using bash tool you can start GUI applications, but you need to set export DISPLAY=:1 and use a subshell. For example \"(DISPLAY=:1 xterm &)\". GUI apps run with bash tool will appear within your desktop environment, but they may take some time to appear. Take a screenshot to confirm it did.\n* When using your bash tool with commands that are expected to output very large quantities of text, redirect into a tmp file and use str_replace_editor or `grep -n -B <lines before> -A <lines after> <query> <filename>` to confirm output.\n* When viewing a page it can be helpful to zoom out so that you can see everything on the page.  Either that, or make sure you scroll down to see everything before deciding something isn't available.\n* When using your computer function calls, they take a while to run and send back to you.  Where possible/feasible, try to chain multiple of these calls all into one function calls request.\n* The current date is Sunday, November 17, 2024.\n</SYSTEM_CAPABILITY>\n\n<IMPORTANT>\n* When using Firefox, if a startup wizard appears, IGNORE IT.  Do not even click \"skip this step\".  Instead, click on the address bar where it says \"Search or enter address\", and enter the appropriate search term or URL there.\n* If the item you are looking at is a pdf, if after taking a single screenshot of the pdf it seems that you want to read the entire document instead of trying to continue to read the pdf from your screenshots + navigation, determine the URL, use curl to download the pdf, install and use pdftotext to convert it to a text file, and then read that text file directly with your StrReplaceEditTool.\n</IMPORTANT>",
      # "cache_control": {
      #   "type": "ephemeral"
      # }
    }
  ],
  tools= [
        {
          "type": "computer_20241022",
          "name": "computer",
          "display_width_px": 672,
          "display_height_px": 890,
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
  betas=["computer-use-2024-10-22"]
)
print(response)


'''
BetaMessage(id='msg_01EuGeQfvQRAFBzTkubXPMop', content=[BetaTextBlock(text='I can see the last name input field. I\'ll now:\n1. Click on the last name input field\n2. Type "Moore"', type='text'), 
BetaToolUseBlock(id='toolu_01TtV7ZsuF5CQKzp2pps3PSR', input={'action': 'mouse_move', 'coordinate': [310, 290]}, name='computer', type='tool_use'), 
BetaToolUseBlock(id='toolu_01JWjV5q2dfhY5AMgYpZTSHH', input={'action': 'left_click'}, name='computer', type='tool_use'), 
BetaToolUseBlock(id='toolu_01J8ge7B98w8GkfoSBZujNpf', input={'action': 'type', 'text': 'Moore'}, name='computer', type='tool_use')], 
model='claude-3-5-sonnet-20241022', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', usage=BetaUsage(cache_creation_input_tokens=None, cache_read_input_tokens=None, input_tokens=3461, output_tokens=194))
'''




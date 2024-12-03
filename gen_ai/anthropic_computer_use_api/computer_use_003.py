"""
This script uses the Anthropic computer use API to get the coordinates of the element on the current screenshot.
The element on the current screenshot should correspont to the a marked with red dot element on the provided image.
The work is done in one request to LLM.
"""


import anthropic
import base64


# Path to image
image_path = "simple_form_672×890.png" # path to the image file; image dimension is 672×890
tool_use_id = "toolu_01LnrveoKPtWqmxCeMXHj9Mf"  # just arbitrary string;  in multi-request approach: tool_use_id from the previous response 
red_dot_image_path="red_dot_form_672×890.png"


# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:    
    # see https://docs.anthropic.com/en/docs/build-with-claude/vision
    return base64.standard_b64encode(image_file.read()).decode('utf-8')  

base64_image = encode_image(image_path)
base64_red_dot_image_path = encode_image(red_dot_image_path)

client = anthropic.Anthropic()

response = client.beta.messages.create(
  max_tokens= 1024,
  messages= [
    {
      "role": "user",
      "content": [
        {
            "type": "text",
            "text": "Image with red dot:"
        },        
        {
          "type": "image",
          "source": {
              "type": "base64",
              "media_type": "image/png",
              "data": base64_red_dot_image_path,
          }
        },
        {
          "type": "text",
          "text": """Look at the provided 'Image with red dot'. Identify on the image page element marked with red dot.
          Perform left mouse click into the corresponding webpage element on the screen.
          
          "corresponding" means that the element on the screen must have the same functionality as the one marked with a red dot in the picture.
          
          For example, if the picture shows the input field labeled "Password", marked with a red dot so on the screen should be picked input with a similar label, although it may be in a different place.
          """,
          # "cache_control": {
          #   "type": "ephemeral"
          # }
        }
      ]
    }
    ,
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": """ I can see that in the provided image, there's an element marked with a red dot. 

          To click on this element, I'll first take a screenshot to verify the current screen state and then click on corresponding screenshot's element.
          """
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
BetaMessage(id='msg_01WSetQmUsDnokXn6a1V3hzv', 
content=[BetaTextBlock(text='In the provided image, I can see that the "Submit" button is marked with a red dot. Looking at the current screen, 
I can see the same form with a Submit button at the bottom. I\'ll move the cursor to the Submit button and click it.', type='text'), 
BetaToolUseBlock(id='toolu_01Bpux61n6jMn7jrLXqHQdL6', input={'action': 'mouse_move', 'coordinate': [112, 822]}, name='computer', type='tool_use'), 
BetaToolUseBlock(id='toolu_01EtatTK49KoeUhuAyQjmTqk', input={'action': 'left_click'}, name='computer', type='tool_use')], 
model='claude-3-5-sonnet-20241022', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', 
usage=BetaUsage(cache_creation_input_tokens=None, cache_read_input_tokens=None, input_tokens=4357, output_tokens=167))
'''




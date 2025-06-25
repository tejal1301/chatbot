import cohere
import os
from dotenv import load_dotenv,dotenv_values

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def get_text_output(input_text):
    output = co.chat(
    model="command-r-plus",
    message=input_text
    )
    return output.text

def get_text_stream_output(input_text):
    for output in co.chat_stream(
    model="command-r-plus",
    message=input_text
    ):
        if output.event_type == "text-generation":
            yield output.text
    
#output = co.chat(
#    model="command-r-plus",
#    message="Hello"
#    )
#print(co)
#print(output.text)
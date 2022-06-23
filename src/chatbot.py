import random
import time

from pyodide import create_proxy


def update_chat(event):
    conversation = Element('conversation')
    initial_content = conversation.element.innerHTML
    new_text = Element('text_input').value
    updated_content = initial_content + format_user_message(new_text) + format_bot_message(get_bot_reply())
    conversation.write(updated_content)
    for i in range(10):
        conversation.write(updated_content + '.'*i)
        time.sleep(0.1)


def format_user_message(text):
    html_message = """
    <div class="user_message">
        <b>You: </b>%s<br>
    </div>
    """ % text
    return html_message


def format_bot_message(text):
    html_message = """
    <div class="bot_message">
        <b>Chatbot: </b>%s<br>
    </div>
    """ % text
    return html_message


def get_bot_reply():
    replies = [
        'Thanks',
        'What can I do for you?',
        "Sorry, I don't understand you",
    ]
    return random.choice(replies)


button = document.querySelector("button")
button.addEventListener("click", create_proxy(update_chat))

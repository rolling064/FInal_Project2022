import os
import sys

import pygraphviz as pgv
from flask import Flask, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,MessageTemplateAction

from utils import send_text_message,send_button_message,send_image_message
from fsm import TocMachine

load_dotenv()

machine = TocMachine(
    states=['user','1st_level_folder','password','secret','ncku_folder','math','csie','nckuedu','entertainment_folder','facebook','youtube','twich','google_folder','translation','drive','gmail'],
    transitions=[{'trigger': 'advance', 'source': 'user', 'dest':'1st_level_folder', 'conditions':'is_going_to_1st_level_folder'},
                 {'trigger': 'advance', 'source': 'user', 'dest':'password', 'conditions':'is_going_to_password'},
                 {'trigger': 'advance', 'source': 'password', 'dest':'secret', 'conditions':'is_going_to_secret'},

                 {'trigger': 'advance', 'source': '1st_level_folder', 'dest':'ncku_folder', 'conditions':'is_going_to_ncku_folder'},
                 
                 {'trigger': 'advance', 'source': '1st_level_folder', 'dest':'ncku_folder', 'conditions':'is_going_to_ncku_folder'},
                 {'trigger': 'advance', 'source': 'ncku_folder', 'dest':'1st_level_folder', 'conditions':'back_to_1st_level_folder'},
                 {'trigger': 'advance', 'source': '1st_level_folder', 'dest':'entertainment_folder', 'conditions':'is_going_to_entertainment_folder'},
                 {'trigger': 'advance', 'source': 'entertainment_folder', 'dest':'1st_level_folder', 'conditions':'back_to_1st_level_folder'},
                 {'trigger': 'advance', 'source': '1st_level_folder', 'dest':'google_folder', 'conditions':'is_going_to_google_folder'},
                 {'trigger': 'advance', 'source': 'google_folder', 'dest':'1st_level_folder', 'conditions':'back_to_1st_level_folder'},
                 {'trigger': 'advance', 'source': ['1st_level_folder','password','secret','ncku_folder','math','csie','nckuedu','entertainment_folder','facebook','youtube','twich','google_folder','translation','drive','gmail'], 'dest':'user', 'conditions':'is_going_to_user'},

                 {'trigger': 'advance', 'source': 'ncku_folder', 'dest':'math', 'conditions':'is_going_to_math'},
                 {'trigger': 'advance', 'source': 'math', 'dest':'ncku_folder', 'conditions':'back_to_ncku_folder'},
                 {'trigger': 'advance', 'source': 'ncku_folder', 'dest':'csie', 'conditions':'is_going_to_csie'},
                 {'trigger': 'advance', 'source': 'csie', 'dest':'ncku_folder', 'conditions':'back_to_ncku_folder'},
                 {'trigger': 'advance', 'source': 'ncku_folder', 'dest':'nckuedu', 'conditions':'is_going_to_nckuedu'},
                 {'trigger': 'advance', 'source': 'nckuedu', 'dest':'ncku_folder', 'conditions':'back_to_ncku_folder'},

                 {'trigger': 'advance', 'source': 'entertainment_folder', 'dest':'facebook', 'conditions':'is_going_to_facebook'},
                 {'trigger': 'advance', 'source': 'facebook', 'dest':'entertainment_folder', 'conditions':'back_to_entertainment_folder'},
                 {'trigger': 'advance', 'source': 'entertainment_folder', 'dest':'youtube', 'conditions':'is_going_to_youtube'},
                 {'trigger': 'advance', 'source': 'youtube', 'dest':'entertainment_folder', 'conditions':'back_to_entertainment_folder'},
                 {'trigger': 'advance', 'source': 'entertainment_folder', 'dest':'twich', 'conditions':'is_going_to_twich'},
                 {'trigger': 'advance', 'source': 'twich', 'dest':'entertainment_folder', 'conditions':'back_to_entertainment_folder'},

                 {'trigger': 'advance', 'source': 'google_folder', 'dest':'translation', 'conditions':'is_going_to_translation'},
                 {'trigger': 'advance', 'source': 'translation', 'dest':'google_folder', 'conditions':'back_to_google_folder'},
                 {'trigger': 'advance', 'source': 'google_folder', 'dest':'drive', 'conditions':'is_going_to_drive'},
                 {'trigger': 'advance', 'source': 'drive', 'dest':'google_folder', 'conditions':'back_to_google_folder'},
                 {'trigger': 'advance', 'source': 'google_folder', 'dest':'gmail', 'conditions':'is_going_to_gmail'},
                 {'trigger': 'advance', 'source': 'gmail', 'dest':'google_folder', 'conditions':'back_to_google_folder'},

                 {'trigger': 'go_back', 'source': ['math','csie','nckuedu','facebook','youtube','twich','translation','drive','gmail','secret',], 'dest':'user',},
                
                 {'trigger': 'advance', 'source': '1st_level_folder', 'dest':'1st_level_folder','conditions':'is_going_to_menu'},
                 {'trigger': 'advance', 'source': 'ncku_folder', 'dest':'ncku_folder','conditions':'is_going_to_menu'},
                 {'trigger': 'advance', 'source': 'entertainment_folder', 'dest':'entertainment_folder','conditions':'is_going_to_menu'},
                 {'trigger': 'advance', 'source': 'google_folder', 'dest':'google_folder','conditions':'is_going_to_menu'},
                ],
    initial="user",
    auto_transitions=False,
    show_conditions=True
)

app = Flask(__name__, static_url_path='')
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token =os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

@app.route("/callback", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        

        response = machine.advance(event)
        if response == False : 
            if machine.state == 'password':
                send_text_message(event.reply_token, '密碼錯誤，請重新嘗試')
            #若要使用fsm記得要改網址
            elif event.message.text.lower() == 'fsm':
                #回傳到主機可選擇是否開啟
                #machine.get_graph().draw('fsm.png', prog='dot')
                send_image_message(event.reply_token, 'https://d45a-27-53-122-68.jp.ngrok.io/show-fsm')
            elif machine.state =='user':
                send_text_message(event.reply_token, '目前只提供資料夾的功能\n輸入"start"便可開啟資料夾')
            else :
                send_text_message(event.reply_token, '請輸入"menu"來呼叫選單並根據選單按下按鈕\n或輸入結束回到最開始')

    return "OK"

@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port, debug=True)
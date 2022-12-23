from transitions.extensions import GraphMachine
from linebot.models import MessageTemplateAction
import requests
import pandas as pd

from utils import send_text_message,send_button_message,send_image_message

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_password(self, event):
        text = event.message.text
        return text.lower() == '開啟資料夾'
    def on_enter_password(self, event):
        send_text_message(event.reply_token, "請輸入密碼")

    def is_going_to_secret(self, event):
        text = event.message.text
        return text.lower() == 'rolling'
    def on_enter_secret(self, event):
        send_text_message(event.reply_token, "https://imgur.com/a/cTVg634")
        self.go_back()

    #第一層資料夾
    def is_going_to_1st_level_folder(self, event):
        text = event.message.text
        return text.lower() == 'start' or text.lower() == '返回第一層資料夾'
    def on_enter_1st_level_folder(self, event):
        title = '第一層資料夾'
        text = '請選擇想讀取的資料夾'
        btn = [
            MessageTemplateAction(
                label = 'ncku資料夾',
                text ='ncku'
            ),
            MessageTemplateAction(
                label = '娛樂資料夾',
                text = '娛樂'
            ),
            MessageTemplateAction(
                label = 'google資料夾',
                text = 'google'
            ),
            MessageTemplateAction(
                label = '結束',
                text = '結束'
            ),
        ]
        send_button_message(event.reply_token, title, text, btn)

    #結束
    def is_going_to_end(self, event):
        text = event.message.text
        return text.lower() == '結束'
    def on_enter_end(self, event):
        send_text_message(event.reply_token, "謝謝您的使用，歡迎你下次的使用")
        self.go_back()


    #ncku資料夾
    def is_going_to_ncku_folder(self, event):
        text = event.message.text
        return text.lower() == 'ncku' or text.lower() == '返回ncku資料夾'
    def on_enter_ncku_folder(self, event):
        title = 'ncku資料夾'
        text = '請選擇網站'
        btn = [
            MessageTemplateAction(
                label = '數學系',
                text ='數學系'
            ),
            MessageTemplateAction(
                label = '資訊系',
                text = '資訊系'
            ),
            MessageTemplateAction(
                label = '成功入口',
                text = '成功入口'
            ),
            MessageTemplateAction(
                label = '返回第一層資料夾',
                text = '返回第一層資料夾'
            ),
        ]
        send_button_message(event.reply_token, title, text, btn)


    def is_going_to_math(self, event):
        text = event.message.text
        return text.lower() == '數學系'
    def on_enter_math(self, event):
        send_text_message(event.reply_token, "以下是您要的網站\nhttps://www.math.ncku.edu.tw/\n謝謝您的使用，歡迎你下次的使用")
        self.go_back()

    def is_going_to_csie(self, event):
        text = event.message.text
        return text.lower() == '資訊系'
    def on_enter_csie(self, event):
        send_text_message(event.reply_token, "以下是您要的網站\nhttps://www.csie.ncku.edu.tw/zh-hant/\n謝謝您的使用，歡迎你下次的使用")
        self.go_back()        

    def is_going_to_nckuedu(self, event):
        text = event.message.text
        return text.lower() == '成功入口'
    def on_enter_nckuedu(self, event):
        send_text_message(event.reply_token, "以下是您要的網站\nhttps://i.ncku.edu.tw/\n謝謝您的使用，歡迎你下次的使用")
        self.go_back()


    #返回ncku資料夾
    def back_to_ncku_folder(self,event):
        text = event.message.text
        return text.lower() == '返回ncku資料夾'

    #返回第一層
    def back_to_1st_level_folder(self,event):
        text = event.message.text
        return text.lower() == '返回第一層資料夾'


    #google資料夾
    def is_going_to_google_folder(self, event):
        text = event.message.text
        return text.lower() == 'google' or text.lower() == '返回google資料夾'
    def on_enter_google_folder(self, event):
        title = 'google資料夾'
        text = '請選擇網站'
        btn = [
            MessageTemplateAction(
                label = 'google翻譯',
                text ='google翻譯'
            ),
            MessageTemplateAction(
                label = 'google雲端',
                text = 'google雲端'
            ),
            MessageTemplateAction(
                label = 'gmail',
                text = 'gmail'
            ),
            MessageTemplateAction(
                label = '返回第一層資料夾',
                text = '返回第一層資料夾'
            ),
        ]
        send_button_message(event.reply_token, title, text, btn)


    def is_going_to_translation(self, event):
        text = event.message.text
        return text.lower() == 'google翻譯'
    def on_enter_translation(self, event):
        send_text_message(event.reply_token, "以下是您要的網站\nhttps://translate.google.com.tw/?hl=zh-TW\n謝謝您的使用，歡迎你下次的使用")
        self.go_back()

    def is_going_to_drive(self, event):
        text = event.message.text
        return text.lower() == 'google雲端'
    def on_enter_drive(self, event):
        send_text_message(event.reply_token, "以下是您要的網站\nhttps://drive.google.com/\n謝謝您的使用，歡迎你下次的使用")
        self.go_back()

    def is_going_to_gmail(self, event):
        text = event.message.text
        return text.lower() == 'gmail'
    def on_enter_gmail(self, event):
        send_text_message(event.reply_token, "以下是您要的網站\nhttps://mail.google.com/\n謝謝您的使用，歡迎你下次的使用")
        self.go_back()

    #返回google資料夾
    def back_to_google_folder(self,event):
        text = event.message.text
        return text.lower() == '返回google資料夾'


    #娛樂資料夾
    def is_going_to_entertainment_folder(self, event):
        text = event.message.text
        return text.lower() == '娛樂' or text.lower() == '返回娛樂資料夾'
    def on_enter_entertainment_folder(self, event):
        title = '娛樂資料夾'
        text = '請選擇網站'
        btn = [
            MessageTemplateAction(
                label = 'facebook',
                text ='facebook'
            ),
            MessageTemplateAction(
                label = 'youtube',
                text = 'youtube'
            ),
            MessageTemplateAction(
                label = 'twitch',
                text = 'twitch'
            ),
            MessageTemplateAction(
                label = '返回第一層資料夾',
                text = '返回第一層資料夾'
            ),
        ]
        send_button_message(event.reply_token, title, text, btn)


    def is_going_to_facebook(self, event):
        text = event.message.text
        return text.lower() == 'facebook'
    def on_enter_facebook(self, event):
        send_text_message(event.reply_token, "以下是您要的網站\nhttps://www.facebook.com/\n謝謝您的使用，歡迎你下次的使用")
        self.go_back()

    def is_going_to_youtube(self, event):
        text = event.message.text
        return text.lower() == 'youtube'
    def on_enter_youtube(self, event):
        send_text_message(event.reply_token, "以下是您要的網站\nhttps://www.youtube.com/\n謝謝您的使用，歡迎你下次的使用")
        self.go_back()

    def is_going_to_twich(self, event):
        text = event.message.text
        return text.lower() == 'twitch'
    def on_enter_twich(self, event):
        send_text_message(event.reply_token, "以下是您要的網站\nhttps://www.twitch.tv/\n謝謝您的使用，歡迎你下次的使用")
        self.go_back()

    #返回娛樂資料夾
    def back_to_entertainment_folder(self,event):
        text = event.message.text
        return text.lower() == '返回娛樂資料夾'

    #再次呼叫選單
    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == 'menu'
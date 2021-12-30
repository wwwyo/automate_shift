import os
import requests
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)

# Line Notify
ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
SECRET = os.environ["CHANNEL_SECRET"]
line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)
HEADERS = {"Authorization": "Bearer %s" % ACCESS_TOKEN}
URL = "https://notify-api.line.me/api/notify"

def lambda_handler(event, context):
    user_id = 
    message = TextSendMessage(text="aaaaaa")

    #lineに通知
    line_bot_api.push_message()
    requests.post(URL, headers=HEADERS, data=data)
    
lambda_handler(1,1)
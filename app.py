from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from quickReply import default_quick_reply  # 👈 新增這行（匯入 Quick Reply）
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
line_handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 👇 新增這一段（最小必要 Quick Reply 處理邏輯）
@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    reply = default_quick_reply()  # 由 quickReply.py 生成 Quick Reply
    line_bot_api.reply_message(event.reply_token, reply)


if __name__ == "__main__":
    app.run(port=5000)
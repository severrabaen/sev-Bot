from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["m0+Z1KVL3JPb5eqBgbeEcaY/AHlICKnuQnhBKBAsVWLBxfj5HjwTNyaqhfCCfGjWzTtUzWacQGxaTDhqHcDUsn0B7lf7FXXKKsIENk3R5y6aGCE+FwO9KiR1jtbXzNQJPRHpFbzzYYtc4aSN30KJ6gdB04t89/1O/w1cDnyilFU="]
YOUR_CHANNEL_SECRET = os.environ["fb656592b49f5cd19164d6a707c92cd1"]

line_bot_api = LineBotApi(m0+Z1KVL3JPb5eqBgbeEcaY/AHlICKnuQnhBKBAsVWLBxfj5HjwTNyaqhfCCfGjWzTtUzWacQGxaTDhqHcDUsn0B7lf7FXXKKsIENk3R5y6aGCE+FwO9KiR1jtbXzNQJPRHpFbzzYYtc4aSN30KJ6gdB04t89/1O/w1cDnyilFU=)
handler = WebhookHandler(fb656592b49f5cd19164d6a707c92cd1)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

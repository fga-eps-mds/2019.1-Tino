from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
import os
import telegram


app = Flask(__name__)
BOT_TOKEN = os.environ.get('TELEGRAM_TOKEN')
BOT_TOKEN = str(BOT_TOKEN)

# accept telegram messages
@app.route('/', methods=['POST', 'GET'])
def index():
    if(request.method == 'POST'):
        return Response('ok', status=200)
    else:
        bot = telegram.Bot(token=BOT_TOKEN)
        chat_id = request.args.get('chat_id')
        json = {"chat_id": chat_id}
        try:
            photo1 = open('/2019.1-Tino/assets/tabela.png', 'rb')
            bot.send_photo(chat_id, photo1)
        except Exception as e:
            print(e)

    return jsonify(json)


if(__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0')

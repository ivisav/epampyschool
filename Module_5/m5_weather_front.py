from datetime import datetime
import json
import redis
from flask import Flask, render_template    # html page template located in template dir

app = Flask(__name__)
rconnect = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


@app.route("/")
def start_page():
    data = rconnect.lrange('Moscow', -1, -1)    # we need only last value now
    for x in data:
        decoded = json.loads(x)
        main = decoded[0]
        temp = decoded[1]
        hum = decoded[2]
        date = datetime.fromtimestamp(decoded[3]).strftime("%m/%d/%Y, %H:%M:%S")
        return render_template('main.html', main_condition=main, temperature=temp,
                               humidity=hum, date=date, city='Moscow')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=12345)

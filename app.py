from flask import Flask, request
from sinkaf import Sinkaf

obj = Sinkaf()

app = Flask(__name__)

@app.route("/tahmin")
def tahmin():
    sentence = request.args.get('sentence', '')
    result = not obj.tahmin([sentence]).tolist()[0]
    return {
        "sentence": sentence,
        "safe": result
    }

if __name__ == '__main__':
   app.run(debug=False, host='0.0.0.0')
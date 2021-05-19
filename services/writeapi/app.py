import writeAPI as wp
from flask import Flask, request, render_template
import json

hostName = "0.0.0.0"
serverPort = 8080

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("write.html")

@app.route('/write', methods=['POST'])
def write():
    if request.method == "POST":
        record = request.form['title']
        write = wp.WriteAPI()
        result = write.writeData(record)
        return render_template('write_output.html', result=result)


@app.route('/api/v1/tweet', methods=['POST'])
def writeAPI():
    if request.method == "POST":
        params = {}
        params['user_id'] = request.form['user_id']
        params['auth_token'] = request.form['auth_token']
        params['message'] = request.form['message']
        params['media_ids'] = request.form['media_ids']
        write = wp.WriteAPI()
        result = write.writeDataAPI(params)
        return render_template('write_output.html', result=result)
        #return result
        

if __name__ == '__main__':
    app.run(host=hostName, port=serverPort, debug=True)
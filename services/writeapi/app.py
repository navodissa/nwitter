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
        request_data = request.get_json()
        # Extracting the data received as json and added them to a dictionary to be passed to WriteAPI object
        params = {}
        params['user_id'] = request_data['user_id']
        params['auth_token'] = request_data['auth_token']
        params['message'] = request_data['status']
        params['media_ids'] = request_data['media_ids']

        # Creating a WriteAPI object
        write = wp.WriteAPI()

        # Calling the writeDataAPI function of created object and assigned the return value
        result = write.writeDataAPI(params)
        #return render_template('write_output.html', result=result)
        return result
        

if __name__ == '__main__':
    app.run(host=hostName, port=serverPort, debug=True)
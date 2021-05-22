import readAPI as rp
from flask import Flask, request, render_template
import json

hostName = "0.0.0.0"
serverPort = 8081

app = Flask(__name__)

@app.route('/api/v1/home_timeline')
def readAPI():
    if request.method == "GET":
        user_id = request.args.get('user_id')

        # Creating a WriteAPI object
        read = rp.ReadAPI()

        # Calling the writeDataAPI function of created object and assigned the return value
        result = read.readDataAPI(user_id)
        #return render_template('write_output.html', result=result)
        return result
        

if __name__ == '__main__':
    app.run(host=hostName, port=serverPort, debug=True)
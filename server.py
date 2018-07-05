from flask import Flask,request
from datetime import datetime

app = Flask(__name__)

@app.route("/upload",methods = ["POST"])
def uploadImg():
    print(request.files)
    # checking if the file is present or not.
    if 'file' not in request.files:
        return "No file found"
    
    file = request.files['file']
    file.save("img/test{}.jpg".format(str(datetime.now())))
    return "file successfully saved"

if __name__ == "__main__":
    app.run(port=5000)

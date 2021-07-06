from flask import Flask,request,render_template
from Model import predict
import json


UPLOAD_FOLDER = './static/uploads/'



# create the flask object
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['GET','POST'])
def prediction(file):
    data = file
    if data == None:
        return 'Got None'
    else:
        # model.predict.predict returns a dictionary
        prediction = predict.pred(data)
    return json.dumps(str(prediction))
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save((UPLOAD_FOLDER+f.filename))
      
      result=prediction(UPLOAD_FOLDER+f.filename)
      return result
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
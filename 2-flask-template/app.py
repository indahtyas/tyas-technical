import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('predict-weight.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('predict_weight.html')

@app.route('/getprediction',methods=['POST'])
def getprediction():    

    input = [float(x) for x in request.form.values()]
    final_input = [np.array(input)]
    prediction = model.predict(final_input)

    return render_template('predict_weight.html', output='Predicted Weight in KGs :{}'.format(prediction))
   

if __name__ == "__main__":
    app.run(debug=True)
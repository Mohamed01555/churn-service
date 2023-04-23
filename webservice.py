# flask is used to turn a python function to a web service

# app = Flask(__name__)

# #decorator to add the functionality of being the ping function a web service
# @app.route('/ping', methods = ['GET'])
# def ping():
#     return 'PONG'

# if __name__ == '__main__':
#     app.run(debug = True, host  = '0.0.0.0',port = 9668 )

#############################################################################################################################3
import pickle
from flask  import Flask, request, jsonify

app = Flask('Churn_service')

@app.route('/predict', methods = ['POST'])
def get_prediction():
    with open('churn_model.bin', 'rb') as f:
        dv, model = pickle.load(f)
    
    customer = request.get_json()
    data_point = dv.transform([customer])
    
    y_pred = model.predict_proba(data_point)[0, 1]
    proba = y_pred >= 0.5
    
    return jsonify({
        'probability':float(y_pred),
        'prediction':bool(proba)
    })

if __name__ == '__main__':
    app.run(debug = True, host  = '0.0.0.0',port = 9658)
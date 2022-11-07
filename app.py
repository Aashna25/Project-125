from flask import Flask,jsonify,request
from classifier import getPrediction
app=Flask(__name__)
@app.route("/predict-alphabet",methods=["POST"])
def predictdata():
    image=request.files.get("alphabet")
    predictions=getPrediction(image)
    return jsonify({
        "prediction":predictions
    }),200



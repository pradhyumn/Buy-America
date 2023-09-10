from flask import Flask, request, render_template
# Other necessary imports for your model, preprocessing, etc.
from catboost import CatBoostClassifier
import pandas as pd

model = CatBoostClassifier()
model.load_model("catboost_model.cbm")


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('template.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    funding_agency_name = request.form.get('funding_agency_name')
    product_service_code = float(request.form.get('product_service_code'))
    justification = request.form.get('justification')
    country_origin = request.form.get('country_origin')
# Prepare the data for prediction (assume your model takes a DataFrame)
    data_for_prediction = {
        'Funding Agency Name': [funding_agency_name],
        'Product or Service Code': [product_service_code],
        'Justification': [justification],
        'Country of Product or Service Origin': [country_origin]
    }
    df_predict = pd.DataFrame(data_for_prediction)
    
    # Make the prediction using the model
    predicted_class = model.predict(df_predict)
    predicted_probabilities = model.predict_proba(df_predict)

    # Extract confidence (probability) of the prediction
    # Assuming class '1' (Approved) is the second column in the predicted_probabilities
    confidence = predicted_probabilities[0][1] * 100

    # Convert prediction to human-readable label
    if predicted_class[0] == 1:
        prediction = "Approved"
    else:
        prediction = "Denied"
    
    print([funding_agency_name],[product_service_code],[justification],[country_origin])
    print(predicted_class[0])
    print(prediction)


    return f"The prediction for the provided data is: {prediction} with a confidence of {confidence:.2f}%"
    # Transform the data as required and make a prediction
    # For the sake of this example, let's assume the prediction is hardcoded
    #prediction = "Approved"  # Replace with actual prediction logic

    #return f"The prediction for the provided data is: {prediction}"

if __name__ == '__main__':
    app.run(debug=True)

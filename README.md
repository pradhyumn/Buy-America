# Buy-America

This is a toy-example for predicting the chances of getting exceptions and waivers developed on openly available datasets on 3 decades of historical data available on Sam.gov website. There were 3 outlier detection models tried:
- Local Outlier Factor model (79% accuracy)
- Isolation Forest Method (81% accuracy)
- One-class SVM model (77% accuracy)

These models were tried as the open datasets have very few negative (denied) examples. However, by using oversampling techniques, ensemble methods like XGBoost and CatBoost were able to be trained on the data and gave very high accuracy (> 99%). The accuracy of the models is:
- XGBoost (99.16 %)
- CatBoost (99.24 %)

The model checkpoint file for the CatBoost model is also uploaded and it can be used to run a flask application that can be hosted locally or deployed on an AWS Server. To run the application locally, the steps are as follows:

1. Clone the repository in your local folder.
2. Import the entire folder in your VS Code environment.
3. Set the FLASK_APP and FLASK_ENV paths by running the following commands in your VS Code terminal:
```
  set FLASK_APP=app.py
  set FLASK_ENV=development
```
4. Run your flask application by running the following command:
```
  python -m flask run
```
5. Now, your flask application is running. You can open it in your web browser by following the URL:
```
http://127.0.0.1:5000/
```

All the details for EDA and the model training can be found in the uploaded Jupyter notebook. Hope you enjoyed this demonstration of training your own ML model on an Open Dataset and hosting it locally on a web application!

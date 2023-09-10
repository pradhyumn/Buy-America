# Buy-America

This is a toy-example for predicting the chances of getting exceptions and waivers developed on openly available datasets on 3 decades of historical data available on Sam.gov website. There were 3 outlier detection models tried:
- Local Outlier Factor model (79% accuracy)
- Isolation Forest Method (81% accuracy)
- One-class SVM model (77% accuracy)

These models were tried as the open datasets have very few negative (denied) examples. However, by using oversampling techniques, ensemble methods like XGBoost and CatBoost were able to be trained on the data and gave very high accuracy (> 99%). The accuracy of the models is:
- XGBoost (99.16 %)
- CatBoost (99.24 %)

The model checkpoint file for the CatBoost model is also uploaded and it can be used to run a streamlit application that can be hosted locally or deployed on an AWS Server. All the details for EDA and the model training can be found in the uploaded Jupyter notebook.

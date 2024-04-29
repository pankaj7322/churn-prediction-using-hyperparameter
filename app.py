import streamlit
from flask import Flask, request
import joblib

app = Flask(__name__)

# load the model from the file
loaded_model = joblib.load('churn_model.joblib')

@app.route('/predict', methods = ["GET"])
def prediction():
    input_cols = [
        'gender', 'age', 'no_of_days_subscribed', 'multi_screen',
       'mail_subscribed', 'weekly_mins_watched', 'minimum_daily_mins',
       'maximum_daily_mins', 'weekly_max_night_mins', 'videos_watched',
       'maximum_days_inactive', 'customer_support_calls'
    ]
    list1 = []
    for i in input_cols:
        val = request.args.get(i)
        list1.append(eval(val))

    predict = loaded_model.predict([list1])

    return "Prediction is" + str(predict)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port =  8000)
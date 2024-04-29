import streamlit as st
import joblib

# load the model from the file
loaded_model = joblib.load('churn_model.joblib')


def main():
    # gender', 'age', 'no_of_days_subscribed', 'multi_screen',
    #    'mail_subscribed', 'weekly_mins_watched', 'minimum_daily_mins',
    #    'maximum_daily_mins', 'weekly_max_night_mins', 'videos_watched',
    #    'maximum_days_inactive', 'customer_support_calls
    gender = st.text_input("Gender", "Type Here")
    age = st.text_input("Age","Type here")
    no_of_days_subscribed = st.text_input("No_of_days_subscribed", "Type Here")
    multi_screen = st.text_input("Multi_screen", "Type Here")
    mail_subscribed = st.text_input("Mail_subscribed", "Type Here")
    weekly_mins_watched = st.text_input("Weekly_mins_watched", "Type Here")
    minimum_daily_mins = st.text_input("Minimum_daily_mins", "Type Here")
    maximum_daily_mins = st.text_input("Maximum_daily_mins", "Type Here")
    weekly_max_night_mins = st.text_input("Weekly_max_night_mins", "Type Here")
    videos_watched = st.text_input("Videos_watched", "Type Here")
    maximum_days_inactive = st.text_input("Maximum_days_inactive", "Type Here")
    customer_support_calls = st.text_input("Customer_support_calls", "Type Here")
    btn = st.button('Submit')
    if btn:

        prediction = loaded_model.predict([[
            eval(gender),eval(age), eval(no_of_days_subscribed), eval(multi_screen), 
            eval(mail_subscribed), eval(weekly_mins_watched), eval(minimum_daily_mins),
            eval(maximum_daily_mins), eval(weekly_max_night_mins), eval(videos_watched),
            eval(maximum_days_inactive), eval(customer_support_calls)
        ]])
        st.write(prediction)



if __name__ == '__main__':
    main()

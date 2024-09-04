import streamlit as st
import pandas as pd
# import numpy as np
# import plotly.express as px
import pickle
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(layout = 'wide' , page_title = 'Home Page')
df = pd.read_csv('Census_cleaned_ml.csv')

st.markdown("""
    <div style="padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1); text-align: center;">
        <h1 style="color: #1f77b4;">Prediction Income</h1>
        <p>This is a simple web app that uses the Streamlit library to predict the income of the United States. The data is from the UCI Machine Learning Repository and has been cleaned for this project.</p>
    </div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
    age = st.selectbox('Select Age', df.age.unique())
with col2:
    fnlwgt = st.selectbox('Select Fnlwgt', df.fnlwgt.unique())

col3, col4 = st.columns(2)
with col3:
    hours_per_week = st.selectbox('Select Hours Per Week', df.hours_per_week.unique())
with col4:
    education = st.selectbox('Select Education', df.education.unique())

col5, col6 = st.columns(2)
with col5:
    workclass = st.selectbox('Select Workclass', df.workclass.unique())
with col6:
    marital_status = st.selectbox('Select Marital Status', df.marital_status.unique())

col7, col8 = st.columns(2)
with col7:
    occupation = st.selectbox('Select Occupation', df.occupation.unique())
with col8:
    education_num = st.selectbox('Select Education Num', df.education_num.unique())

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

if st.button('Predict'):

    new_data = pd.DataFrame([[age, fnlwgt, hours_per_week, education, workclass, marital_status, occupation,education_num]], columns=['age', 'fnlwgt', 'hours_per_week', 'education', 'workclass', 'marital_status', 'occupation','education_num'],dtype='object')
    prediction = model.predict(new_data)

    if prediction == 0:
        prediction = '<=50K'
    else:
        prediction = '>50K'
    st.write(f'The predicted income is {prediction}')

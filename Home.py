import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random
from plotly.offline import iplot , plot
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout = 'wide' , page_title = 'Home Page',page_icon = '🏠')
df = pd.read_csv('Census_cleaned.csv')


st.title('Census Data Analysis')
st.markdown('This is a simple web app that uses the Streamlit library to visualize the Census data of the United States. The data is from the UCI Machine Learning Repository and has been cleaned for this project.')
st.image('https://th.bing.com/th/id/OIP.SPkJHrL4uUvBWuQigdBviQAAAA?rs=1&pid=ImgDetMain', width = 700 , caption = 'Census Data Analysis')

st.markdown('''
## Welcome to the Census Data Analysis Web App!
### Features:
- **Data Exploration:** View the data and its summary statistics.
- **Data Visualization:** Use interactive plots to explore the data.
- **Machine Learning:** Use machine learning models to make predictions.
- **Data Insights:** Get insights from the data.
### How to use this app: 
1. Use the sidebar to select the page you want to view.
2. The data is displayed in the main window.
3. You can interact with the plots and tables.
### Column Descriptions:
- **age**: Represents the individual's age in years\n
- **workclass**: Refers to the type of work or sector the individual belongs to, such as "Private", "Government", or "Unemployed"\n
- **fnlwgt**: A value representing the population weight for each individual in the census, used for statistical significance\n
- **education**: Represents the educational level the individual has completed, such as "High School", "Bachelor's", etc.\n
- **education-num**: The number of years of education completed by the individual, as a numerical value\n
- **marital-status**: Refers to the individual's marital status, such as "Married", "Single", "Divorced", etc.\n
- **occupation**: Refers to the type of job or work the individual does. Some values may be missing\n
- **relationship**: Refers to the individual's family relationship, such as "Husband/Wife", "Son/Daughter", etc.\n
- **race**: Refers to the individual's race or ethnicity, such as "White", "Black", "Asian", etc.\n
- **sex**: Refers to the individual's biological sex, either "Male" or "Female"\n
- **capital-gain**: Represents the amount of capital gains the individual earned during the year\n
- **capital-loss**: Represents the amount of capital losses the individual incurred during the year\n
- **hours-per-week**: Refers to the number of hours the individual works per week\n
- **native-country**: Refers to the country where the individual was born or considers their home. Some values may be missing\n
- **income**: Refers to the individual's annual income category, such as ">50K" (more than $50,000 annually) or "<=50K" (less than or equal to $50,000 annually)\n


''')


st.title('Sample of Data')
if st.checkbox('View Sample of Data'):
    st.dataframe(df.head(10))
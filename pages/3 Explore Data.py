import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout = 'wide' , page_title = 'Insights Page',page_icon = '📊')
df = pd.read_csv('Census_cleaned.csv')

st.title('Explore Analysis')

interest = st.selectbox('Select a column to filter by:',
             ['age' , 'education_num' ,'hours_per_week'])

col1 , col2  = st.columns(2)
card1 = col1.container(border=1)
card1.metric(label = f'Min {interest}' , value = df[interest].min())

card2 = col2.container(border=1)
card2.metric(label = f'Max {interest}' , value = df[interest].max())

st.divider()

insert2 = st.selectbox('Select a column to filter by:',
                ['workclass' , 'education' ,'marital_status','occupation','relationship'])

st.title('Most Common Values')
st.write('This section shows the most common values in the selected column')
most_common = df[insert2].value_counts().head(3)
st.write(most_common)


st.title('Data Exploration Univariate Analysis')

x = st.selectbox('Select Column',['age' ,'work class', 'education' , 'education num' , 'marital status' , 'occupation' , 'relationship'])
if x == 'age':
    st.plotly_chart(px.histogram(data_frame = df , x = 'age',template='simple_white',text_auto = True , title = 'Age Distribution'))
    st.plotly_chart(px.box(data_frame = df , x = 'age' , template='plotly_dark'))

elif x == 'workclass':
    st.plotly_chart(px.histogram(data_frame = df , x = 'workclass' , color='workclass',template='presentation'))

elif x == 'education':
    fig = px.histogram(data_frame = df , x = 'education' , template='simple_white' , color = 'education')
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig)

elif x == 'education num':
    st.plotly_chart(px.box(data_frame = df , x = 'education_num',template='plotly_dark'))
    st.plotly_chart(px.histogram(data_frame = df , x = 'education_num',template='simple_white'))

elif x == 'marital status':
    st.plotly_chart(px.histogram(data_frame = df , x = 'marital_status',color = 'marital_status' , template='simple_white'))

elif x == 'occupation':
    st.plotly_chart(px.histogram(data_frame = df , x = 'occupation' , color= 'occupation' , template='plotly_dark' , text_auto=True))

elif x == 'relationship':
    st.plotly_chart(px.histogram(data_frame = df , x = 'relationship',color= 'relationship' , template='plotly_dark'))

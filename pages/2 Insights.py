import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
# import seaborn as sns
# import random
# import requests
# from streamlit_lottie import st_lottie
# import json


# st.set_page_config(layout = 'wide' , page_title = 'Insights Page',page_icon = '📊')
# df = pd.read_csv('Census_cleaned.csv')

# st.title('Insights Analysis')
# def load_lottieurl(url:str):
#     r = requests.get(url)
#     if r.status_code !=200:
#         return None
#     return r.json()
# animation = load_lottieurl('https://lottie.host/3124bd5f-7ac0-4dde-8b4b-173b2966da66/CATdYF6lH0.json')
# st_lottie(animation,speed = .99,quality = 'high',height = 400,width = 600)
c1,c33,c2 = st.columns([4,1,4])


with c1 :
    st.markdown(
    """
    <style>
    .custom-font {
        font-size:14px; /* Adjust the font size as needed */
    }
    </style>
    <p class="custom-font"><strong>Individuals earning more than 50K are mostly in the 30-50 age range, with a sharp decline after 50. Meanwhile, those earning less than 50K are predominantly in their 20 and 30, with numbers steadily decreasing as age increases</strong></p>
    """,
    unsafe_allow_html=True
)
    age = df.groupby(['age','income'])['race'].count().reset_index()
    st.plotly_chart(
    px.line(data_frame = age , x = 'age' , y = 'race',color = 'income' ,markers = True,title='Income Per Age',
                labels={'age':'Age' , 'income':'Income' , 'race':'Count'},template = 'plotly_dark',width=600,height=400))

with c2:
    st.markdown(
    """
    <style>
    .custom-font {
        font-size:14px; /* Adjust the font size as needed */
    }
    </style>
    <p class="custom-font"><strong>Most individuals with 9 years of education earn less than 50K, while the likelihood of earning more than 50K increases with more years of education, particularly at 13 years</strong></p>
    """,
    unsafe_allow_html=True
)

    education_num = df.groupby(['education_num','income'])['race'].count().reset_index()    
    st.plotly_chart(px.line(data_frame = education_num , x = 'education_num' , y = 'race' , title='Income Per Education Num',
              labels={'education_num':'Education Num' , 'income':'Income', 'race':'Count'},template = 'plotly_dark',color='income',markers = True,width=600,height=400))

st.divider()


c3,c44,c4 = st.columns([4,1,4])
with c3:
    st.markdown(
    """
    <style>
    .custom-font {
        font-size:14px; /* Adjust the font size as needed */
    }
    </style>
    <p class="custom-font"><strong>Most individuals in the private sector earn less than 50k although there are a large number of them. Other categories of work have a smaller population with a relatively balanced income distribution. The "never worked" and "unpaid" categories show very few people, all earning less than 50k</strong></p>
    """,
    unsafe_allow_html=True
)

    workclass = df.groupby(['workclass','income'])['race'].count().reset_index()
    st.plotly_chart(px.bar(data_frame = workclass , x = 'workclass' , y = 'race' , title='Income Per Workclass',
                labels={'workclass':'Work Class' , 'income':'Income', 'race':'Count'},template = 'plotly_dark',color='income' , barmode='group',width=600,height=400))

with c4:
    st.markdown(
    """
    <style>
    .custom-font {
        font-size:14px; /* Adjust the font size as needed */
    }
    </style>
    <p class="custom-font"><strong>Higher education levels like Doctorate and Bachelors tend to earn more than 50K, while lower levels like HS-grad mostly earn less than 50K</strong></p>
    """,
    unsafe_allow_html=True
)

    education = df.groupby(['education','income'])['race'].count().reset_index()
    st.plotly_chart(px.bar(data_frame = education , x = 'education' , y = 'race' , title='Income Per Education',
              labels={'education':'Education' , 'income':'Income', 'race':'Count'},template = 'presentation',color='income' , barmode='group',width=600,height=400))

st.divider()

c5,c55,c6 = st.columns([4,1,4])
with c5:
    st.markdown(
    """
    <style>
    .custom-font {
        font-size:14px; /* Adjust the font size as needed */
    }
    </style>
    <p class="custom-font"><strong>Married individuals (Married-civ-spouse) have the highest income over 50K, while the majority of never-married and spouse-absent individuals earn less than 50K. The proportion of high-income earners is also lower among divorced, separated, and widowed individuals</strong></p>
    """,
    unsafe_allow_html=True
)

    matrial_status = df.groupby(['marital_status','income'])['race'].count().reset_index()
    st.plotly_chart(px.bar(data_frame = matrial_status , x = 'marital_status' , y = 'race' , title='Income Per Marital Status',
              labels={'marital_status':'Marital Status' , 'income':'Income', 'race':'Count'},template = 'plotly_dark',color='income' , barmode='group',width=600,height=400))

with c6:
    st.markdown(
    """
    <style>
    .custom-font {
        font-size:14px; /* Adjust the font size as needed */
    }
    </style>
    <p class="custom-font"><strong>Exec-managerial and Prof-specialty generate the highest income, while manual and managerial jobs (adm-clerical and machine-op-inspect) are often below 50K</strong></p>
    """,
    unsafe_allow_html=True
)

    occupation = df.groupby(['occupation','income'])['race'].count().reset_index()
    st.plotly_chart(px.bar(data_frame = occupation , x = 'occupation' , y = 'race' , title='Income Per Occupation',
              labels={'occupation':'Occupation' , 'income':'Income', 'race':'Count'},template = 'simple_white',color='income' , barmode='group',width=600,height=400))

st.divider()

c7,c77,c8 = st.columns([4,1,4])
with c7:
    st.markdown(
    """
    <style>
    .custom-font {
        font-size:14px; /* Adjust the font size as needed */
    }
    </style>
    <p class="custom-font"><strong>Most individuals in the "Husband" and "Not-in-family" categories earn ≤50K. The "Wife" category has the fewest individuals, mainly earning ≤50K. No category has more individuals earning >50K than ≤50K</strong></p>
    """,
    unsafe_allow_html=True
)

    relationship = df.groupby(['relationship','income'])['race'].count().reset_index()
    st.plotly_chart(px.bar(data_frame = relationship , x = 'relationship' , y = 'race' , title='Income Per Relationship',
              labels={'relationship':'Relationship' , 'income':'Income', 'race':'Count'},template = 'plotly_dark',color='income' , barmode='group',width=600,height=400))

with c8:
    st.markdown(
    """
    <style>
    .custom-font {
        font-size:14px; /* Adjust the font size as needed */
    }
    </style>
    <p class="custom-font"><strong>Males have a higher proportion of individuals earning >50K compared to females, who mostly earn ≤50K</strong></p>
    """,
    unsafe_allow_html=True
)

    sex = df.groupby(['sex','income'])['race'].count().reset_index()
    fig = px.sunburst(df.groupby(['sex' , 'income'])['race'].count().reset_index() , path=['sex','income'],values='race',color='sex')
    fig.update_traces(textinfo='label+percent parent')
    st.plotly_chart(fig)

st.divider()

c9,c99,c10 = st.columns([4,1,4])

with c9:
    st.markdown(
    """
    <style>
    .custom-font {
        font-size:14px; /* Adjust the font size as needed */
    }
    </style>
    <p class="custom-font"><strong>Husbands and Not-in-family individuals work the most hours, with many working over 40 hours per week. Own-child and Unmarried categories also have a significant number working 21-40 hours. Wife and Other-relative categories generally work fewer hours, often 20 hours or less</strong></p>
    """,
    unsafe_allow_html=True
)

    df['hours_per_week_category'] = pd.cut(df['hours_per_week'], bins=[0, 20, 40, np.inf], labels=['<=20', '21-40', '>40'])
    relationshipwork = df.groupby(['relationship','hours_per_week_category'])['race'].count().reset_index().sort_values(by='race',ascending=False)
    st.plotly_chart(px.bar(data_frame = relationshipwork , x = 'relationship' , y = 'race' , title='effect of the relationship on the number of working hours',
              labels={'relationship':'Relationship' , 'hours_per_week_category':'Hours Per Week', 'race':'Count'},template = 'plotly_dark',color='hours_per_week_category' , barmode='group',width=600,height=400))

with c10:
    st.markdown(
    """
    <style>
    .custom-font {
        font-size:14px; /* Adjust the font size as needed */
    }
    </style>
    <p class="custom-font"><strong>People aged 15-30 mostly work in the private sector. Those aged 31-50 are found in local government and self-employment, while individuals over 50 are primarily in private and self-employment roles. Very few older individuals work in federal government or without pay</strong></p>
    """,
    unsafe_allow_html=True
)

    df['age_category'] = pd.cut(df['age'], bins=[15, 30, 40, 50, np.inf], labels=['15-30', '31-40', '41-50', '>50'])
    agework = df.groupby(['age_category','workclass'])['race'].count().reset_index().sort_values(by='race',ascending=False)
    st.plotly_chart(px.bar(data_frame = agework , x = 'age_category' , y = 'race' , title='effect of the age in the type of work',
              labels={'age_category':'Age' , 'workclass':'Work Class', 'race':'Count'},template = 'plotly_dark',color='workclass' , barmode='group',width=600,height=400))

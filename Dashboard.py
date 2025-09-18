import streamlit as st

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋",
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# # Page information

st.write("# Welcome to PROHI Dashboard! 👋")

st.markdown(
"""
    ## Aims

    After completing the course the student should be able to:
    - explain basic project management methods
    - be able to account for success factors in Health Informatics projects
    - understand basic methods and tools in the field of data science and machine learning
    - explain process models for data mining projects
    - explain the difference between rule-based methods and machine learning methods
    - apply basic project management methods
    - work in an international multidisciplinary project group
    - independently lead and implement a limited project in health informatics - document the steps in the design of a prototype for a health informatics project
    - apply the steps in a process model for data mining projects
    - apply methods from the field of text mining on different types of health informatics problems
    - explain and argue for their positions regarding the implementation of a health informatics project
    - explain how to work with sensitive health information in a safe and ethical way.

"""
)

# You can also add text right into the web as long comments (""")
"""
The final project aims to apply data science concepts and skills on a 
medical case study that you and your team select from a public data source.
The project assumes that you bring the technical Python skills from 
previous courses (*DSHI*: Data Science for Health Informatics), as well as 
the analytical skills to argue how and why specific techniques could
enhance the problem domain related to the selected dataset.
"""

### UNCOMMENT THE CODE BELOW TO SEE EXAMPLE OF INPUT WIDGETS

import streamlit as st
import numpy as np
import pandas as pd

# Set page configuration
st.set_page_config(page_title='Obesity Dashboard', layout='centered')

# Sidebar for page navigation
page = st.sidebar.selectbox('Select a page', ['Dashboard', 'About'])

if page == 'Dashboard':
    st.title('Obesity Scenario Dashboard')
    
    # Input widgets for height, weight and bmi
    height = st.slider('Height (cm)', 120, 220, 170)
    weight = st.slider('Weight (kg)', 40, 150, 70)
    bmi = st.number_input('BMI', 10.0, 50.0, 24.2)
    
    # Generate synthetic data
    data = np.random.randn(10, 3)
    df = pd.DataFrame(data, columns=['Height', 'Weight', 'BMI'])
    
    # Display dataframe
    st.dataframe(df)
    
    # Display chart with synthetic data
    st.line_chart(df)

elif page == 'About':
    st.title('Harish Mohankumar')
    st.markdown("""
    ## Project Summary

During the DSHI course, I conducted a project focused on exploring obesity trends using a comprehensive dataset consisting of 2111 records from individuals in Mexico, Peru, and Colombia. The dataset includes 17 features encompassing numerical, categorical, and binary variables related to lifestyle, eating habits, physical activity, and demographic information. The primary objective was to understand factors contributing to various obesity levels and to classify individuals accordingly.

My analysis involved data understanding, preprocessing, and basic exploratory data analysis using Python libraries such as Pandas and Plotly Express. I examined relationships between height, weight, diet habits, and obesity categories. The project also explored how features like family history and physical activity frequency affect obesity prediction. This hands-on work enhanced my skills in data manipulation, visualization, and applying machine learning concepts within healthcare, providing valuable insights relevant to health informatics and data-driven decision-making.

The best-performing model was a Gradient Boosting classifier with 50 estimators, achieving the highest accuracy and balanced performance metrics among all models tested.
""")
import pandas as pd 
import numpy as np 
import streamlit as st 
import joblib
import category_encoders
import imblearn

st.set_page_config(page_title="USA Real Estate", page_icon=":cityscape:")
st.title("Real Estate Price Prediction 🏙️")
# Function to get user input
def getInput():
    
    Bed = st.slider('Select beds number'.title() , min_value=1 , max_value=10 , step=1)
    
    Bath = st.slider('Select baths number'.title() , min_value=1 , max_value=5 , step=1)
    
    House_size_SqFt = st.slider('Select house size(SqFt)'.title() , min_value=100 , max_value=10000 , step=1)
    
    Year = st.slider('Select year'.title() , min_value=2000 , max_value=2020 , step=1)

    State = st.selectbox('select state'.title() , ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
       'Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
       'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
       'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
       'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
       'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
       'New Jersey', 'New Mexico', 'New York', 'North Carolina',
       'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
       'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
       'Texas', 'Utah', 'Vermont', 'Virgin Islands', 'Virginia',
       'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'])

    return pd.DataFrame(
        data=
            [[Bed, Bath, State, House_size_SqFt, Year]] , columns=['Bed', 'Bath', 'State', 'House_size(SqFt)', 'Year'])

# Get user input    
test = getInput()
st.dataframe(test)

# Load the model
model = joblib.load('model.joblib')

# Predict price button
if st.button('Predict Price'):
   prediction = model.predict(test)
   st.write(f"### Predicted Price: ${prediction[0]}")

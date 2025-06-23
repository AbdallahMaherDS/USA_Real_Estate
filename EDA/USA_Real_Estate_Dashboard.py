# Importing Libraries 
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
# Reading CSVs
df1=pd.read_csv('https://drive.google.com/uc?export=download&id=1pbra3HI4_v_l6rPIZ0SPjhuagtc9cZmN')
df2=pd.read_csv('https://drive.google.com/uc?export=download&id=1_XhA9cIUxXq7693GNSS8rKLYT6gmhtSP')
df3=pd.read_csv('https://drive.google.com/uc?export=download&id=1VFpPVm4eBqfloreNeQeturpCteVQHNFq')
df4=pd.read_csv('https://drive.google.com/uc?export=download&id=11FKTRRuT9LNX5690zWY_mzpsDi_mqUMO')
df5=pd.read_csv('https://drive.google.com/uc?export=download&id=1xWg3y6fNkBCCv1VUBUy3zoMEH96q8GVb')
# Data Visualization
# DF1 Visualization
fig1=px.histogram(data_frame=df1.sort_values('Price(USD)',ascending=True),x=df1['State'],y=df1['Price(USD)'],color='State',text_auto=True)
fig1.update_layout(
    title="The most expensive 10 units in USA",
    xaxis_title="State",
    yaxis_title="Price(USD)",
)
# DF2 Visualization
fig2=px.histogram(data_frame=df2.sort_values('Price(USD)',ascending=True),x=df2['State'],y=df1['Price(USD)'],color='State',text_auto=True)
fig2.update_layout(
    title="The cheapest 10 units in USA",
    xaxis_title="State",
    yaxis_title="Price(USD)",
)
# DF3 Visualization
fig3=px.line(data_frame=df3,x=df3['Year'],y=df3['Price(USD)'],color_discrete_sequence=['burlywood'])
fig3.update_layout(
    title="The average rate of change in unit prices",
    xaxis_title="Year",
    yaxis_title="Price(USD)",
)
# DF4 Visualization
fig4=px.funnel(data_frame=df4.sort_values('House_size(SqFt)',ascending=False),x=df4['House_size(SqFt)'],y=df4['State'],color='House_size(SqFt)')
fig4.update_layout(
    title="The widest 10 units in USA",
    xaxis_title="House size (SqFt)",
    yaxis_title="State",
)
# DF5 Visualization
fig5=px.funnel(data_frame=df5.sort_values('House_size(SqFt)',ascending=False),x=df5['House_size(SqFt)'],y=df5['State'],color='House_size(SqFt)')
fig5.update_layout(
    title="The narrowest 10 units in USA",
    xaxis_title="House size (SqFt)",
    yaxis_title="State",
)
st.set_page_config(layout='wide',page_title="USA Real Estate statistics", page_icon=":📊:")
# sidebar title
title = st.title('USA Real Estate 🏙️')

st.markdown('This report provides an in-depth examination of key trends and characteristics within the residential real estate market of the United States. It presents a detailed analysis of the ten highest-priced and ten lowest-priced housing units, thereby illustrating the wide spectrum of property values across the country. The report also explores the largest and smallest residential units in terms of physical dimensions, offering a perspective on spatial disparities in housing. Furthermore, it includes a longitudinal review of housing price fluctuations spanning the period from 1990 to 2020, capturing significant shifts and developments over three decades. Collectively, these insights contribute to a comprehensive understanding of pricing dynamics, housing availability, and market evolution in the U.S. residential sector.')
# if radio == 'USA Real Estate statistics'
st.subheader('USA Real Estate statistics 📊')
tab1 , tab2 , tab3= st.tabs(['Top 10 Most expensive & cheapest in USA','Top 10 widest & narrowest in USA','The avegrage rate of change in units price'])
with tab1:
        st.plotly_chart(fig1)
        st.plotly_chart(fig2)
with tab2:
        st.plotly_chart(fig4)
        st.plotly_chart(fig5)
with tab3:
        st.plotly_chart(fig3)

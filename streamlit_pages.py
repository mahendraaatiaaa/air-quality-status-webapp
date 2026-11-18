import streamlit as st
import EDA_dataset
import prediction_air_quality_status

st.set_page_config(
    layout='wide',
    initial_sidebar_state='collapsed',
    page_title='Air Quality Status Prediction'
)

page = st.sidebar.selectbox('Choose the page', ('Explorary Data Analysis Page', 'Prediciton Page'))

if page == 'Explorary Data Analysis Page':
    EDA_dataset.run()
else:
    prediction_air_quality_status.run()
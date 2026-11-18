import pickle
import pandas as pd
import streamlit as st

# Load model

model_save = pickle.load(open('model_xgboosting.pkl', 'rb'))

def run():
    
        with st.form('Deployment\src'):
        
            city = st.text_input('Please enter the name of city : ', value='.....')
            
            st.markdown('----')
            
            zone_type = st.text_input ('Please enter the type name of zone : ', value='.....')
            
            st.markdown('----')
            
            air_temperature = st.number_input ('Please enter the number of temperature : ', min_value=0.0, max_value=40.0, value=0.0)
            
            st.markdown('----')
            
            rainfall_amounts = st.number_input ('Please enter the amounts of rainfall : ', min_value=0.0, max_value=80.0, value=0.0)
            
            st.markdown('----')
            
            traffic_index = st.number_input ('Please enter the index number of traffic : ', min_value=0.0, max_value=100.0, value=0.0)
            
            st.markdown('----')
            
            pm25_concentration = st.number_input ('Please enter the concentration number of air particles : ', min_value=0.0, max_value=120.0, value=0.0)
            
            st.markdown('----')
            
            no2_concentration = st.number_input ('Please enter the concentration number of nitrogen dioxide : ', min_value=0.0, max_value=120.0, value=0.0)
            
            st.markdown('----')
            
            hours = st.number_input ('Please enter the duration of hours : ', min_value=0, max_value=24, value=0)
            
            st.markdown('----')
            
            days = st.number_input ('Please enter the number of day : ', min_value=0, max_value=31, value=0)
            
            st.markdown('----')
            
            month = st.number_input ('Please enter the number of month : ', min_value=0, max_value=12, value=0)
            
            st.markdown('----')
            
            submitted = st.form_submit_button("Let's Predict!")

        data_inference = {
            'city' : city,
            'zone_type' : zone_type, 
            'air_temperature' : air_temperature,
            'rainfall_amounts' : rainfall_amounts,
            'traffic_index' : traffic_index,
            'pm25_concentration' : pm25_concentration,
            'no2_concentration' : no2_concentration,
            'hours' : hours,
            'days' : days,
            'month' : month
        }  
    
        data_inference = pd.DataFrame([data_inference])
        
        data_inference
        
        if submitted :
            
            y_prediction_inference =  model_save.predict(data_inference)  
            
            if y_prediction_inference[0] == 0:
                result = "Good"
            elif y_prediction_inference[0] == 1:
                result = "Moderate"
            elif y_prediction_inference[0] == 2:
                result = "Unhealthy"
                
            st.subheader("The Result of Prediction")
        
            st.success(f"Air Quality Status Based on Your Data: {result}")
                
        
if __name__ == '__main__' :
    run()
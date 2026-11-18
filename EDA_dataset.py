import streamlit as st
import pandas as pd
import plotly.express as px

def run():
    
    # Membuat title
    st.title('Air Quality Status Website Application')
    
    # Membuat sub-header
    st.subheader('Page of Exploary Data Analysis')
    
    # Memasukkan dataset
    dataset = pd.read_csv("air_quality_data.csv")
    st.dataframe(dataset)
    
    
    tabs_1, tabs_2, tabs_3 = st.tabs([
        "City",
        "Zone Type",
        "Air Quality Status"
    ])
    
    with tabs_1: 
        
        city_frequency = (
            dataset['city'].value_counts().reset_index()
        )
        
        city_frequency.columns = ['city', 'frequency']
  
        figure = px.bar(
                city_frequency, 
                x='city',
                y='frequency',
                title='Cities Name and Frequencies'
        )
            
        figure.update_layout(
        xaxis=dict(
            tickangle=0
        )
        )
    
        st.plotly_chart(figure, use_container_width=True)
        
    with tabs_2: 
        
        zone_type_frequency = (
            dataset['zone_type'].value_counts().reset_index()
        )
        
        zone_type_frequency.columns = ['zone_type', 'frequency']
        
        figure = px.bar(
                zone_type_frequency, 
                x='zone_type',
                y='frequency',
                title='Zone Types and Frequencies'
            )
            
        figure.update_layout(
            xaxis=dict(
                tickangle=0
            )
        )
            
        st.plotly_chart(figure, use_container_width=True)
        
    with tabs_3:
        
        status_frequency = (
            dataset['air_quality_status'].value_counts().reset_index()
        )
        
        status_frequency.columns = ['air_quality_status', 'frequency']
        
        figure = px.bar(
                status_frequency, 
                x='air_quality_status',
                y='frequency',
                title='Air Quality Status and Frequencies'
            )
            
        figure.update_layout(
            xaxis=dict(
                tickangle=0
            )
        )
        
        st.plotly_chart(figure, use_container_width=True)
          
    
if __name__ == '__main__': 
    run()
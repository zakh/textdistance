import streamlit as st
import textdistance
import re






"""
# did you mean job title



Enter a job title: 
"""

with st.form('my_form'):
    st.session_state.jobtitle = st.text_input('Enter a job title:')
    submitted = st.form_submit_button("Search")
   
        



  
 



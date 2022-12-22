import os
import streamlit as st
from switchpage import switch_page
st.set_page_config(initial_sidebar_state="collapsed")


strengths = ('Collaboration','Communication','Critical Thinking','Customer Service','Decision-Making','Delegation','Innovation','Interpersonal','Leadership','Management','Motivation','Observation','Organization','Planning','Problem-Solving','Team-Building','Teamwork','Time-Management')

with st.form('my_form'):
    st.session_state.strengths = st.multiselect('Choose your top 3 strengths.', strengths, max_selections=3)
    submitted = st.form_submit_button("Continue")
    if submitted:
        switch_page('years of experience')





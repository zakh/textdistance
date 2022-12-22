import streamlit as st
from switchpage import switch_page




with st.form('my_form'):
   st.session_state.desired =  st.text_input('Enter your desired job title:')
   submitted = st.form_submit_button("Continue")
   if submitted:
      switch_page('top skills for desired job')

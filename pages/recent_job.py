import streamlit as st
from switchpage import switch_page
st.set_page_config(initial_sidebar_state="collapsed")




with st.form('my_form'):
   st.session_state.recent =  st.text_input('What\'s your most recent job title?')
   submitted = st.form_submit_button("Continue")
   if submitted:
      switch_page('gap')

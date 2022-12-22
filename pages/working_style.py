import streamlit as st
from switchpage import switch_page

with st.form('my_form'):
    st.session_state.working_style = st.radio('Artistic','Enterprising','Investigative','Organized','Practical','Service-Oriented')
    submitted = st.form_submit_button("Continue")
    if submitted:
        switch_page('generate')
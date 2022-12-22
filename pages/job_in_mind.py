import streamlit as st
from switchpage import switch_page
st.set_page_config(initial_sidebar_state="collapsed")




with st.form('my_form'):
    st.session_state.job_in_mind = st.radio('Do you have a specific job in mind?', ('Yes','No'))
    submitted = st.form_submit_button("Continue")
    if submitted:
        if st.session_state.job_in_mind == 'Yes':
            switch_page('desired_job')
        else:
            switch_page('strenghts')
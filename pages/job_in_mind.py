import streamlit as st
from switchpage import switch_page




with st.form('my_form'):
    st.session_state.job_in_mind = st.radio('Do you have a specific job in mind?', ('Yes','No'), index=1)
    if st.session_state.job_in_mind == 'Yes':
        st.session_state.desired =  st.text_input('Enter your desired job title:')
    submitted = st.form_submit_button("Continue")
    if submitted:
        if st.session_state.job_in_mind == 'Yes':
            switch_page('top skills for desired job')
        else:
            switch_page('strenghts')
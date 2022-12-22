import streamlit as st
from switchpage import switch_page
st.set_page_config(initial_sidebar_state="collapsed")




with st.form('my_form'):
    st.session_state.gap= st.radio('Do you have a gap in your history that you want to explain in your letter?', ('Yes','No'))
    submitted = st.form_submit_button("Continue")
    if submitted:
        if st.session_state.gap == 'Yes':
            switch_page('explain gap')
        else:
            switch_page('working style')
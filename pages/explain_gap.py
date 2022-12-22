import streamlit as st
from switchpage import switch_page
st.set_page_config(initial_sidebar_state="collapsed")


with st.form('my_form'):
    st.session_state.gap_explanation = st.radio('Why were you out of work', ['Impacted by Pandemic','Job Searching','Medical Issues', 'Travel', 'Taking Care of Children', 'Education', 'Relocation', 'Sabbatical'])
    submitted = st.form_submit_button("Continue")
    if submitted:
        switch_page('working style')
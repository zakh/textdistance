import streamlit as st
from switchpage import switch_page




with st.form('my_form'):
    st.session_state.gap_explanation = st.radio('Impacted by Pandemic','Job Searching','Family / Personal Medical Issues', 'Travel', 'Taking Care of Children', 'Education', 'Relocation', 'Sabbatical')
    submitted = st.form_submit_button("Continue")
    if submitted:
        switch_page('working style')
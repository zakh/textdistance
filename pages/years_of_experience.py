age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

import os
import streamlit as st
from switchpage import switch_page


years_of_experience =  (['Less Than One', '1', '2', '3', '4', '5', '6', '7', '8', '9','10+'])
with st.form('my_form'):
    st.session_state.years_of_experience = st.select_slider('How many yers of experience do you have?', years_of_experience)
    submitted = st.form_submit_button("Continue")
    if submitted:
        switch_page('recent job')





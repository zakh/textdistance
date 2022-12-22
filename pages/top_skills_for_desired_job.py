import os
import openai
import streamlit as st
from switchpage import switch_page
st.set_page_config(initial_sidebar_state="collapsed")



openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
   model="text-davinci-003",
   prompt="Return 13 skills which are related to the job of " + st.session_state.desired + " in the language of " + st.session_state.language + " in the format of a comma separated list. Return only the list.",
   temperature=0.7,
   max_tokens=512,
   top_p=1,
   frequency_penalty=0,
   presence_penalty=0
)
with st.form('my_form'):
    skills = response["choices"][0]["text"].split(",")
    st.session_state.skills = st.multiselect('Choose your top 3 job skills for the ' + st.session_state.desired + ' position.', skills, max_selections=3)
    submitted = st.form_submit_button("Continue")
    if submitted:
        switch_page('strengths')

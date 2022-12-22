import os
import openai

import streamlit as st
import streamlit_extras as ste


openai.api_key = os.getenv("OPENAI_API_KEY")

      response = openai.Completion.create(
         model="text-davinci-003",
         prompt="Write a complete cover letter and in the " + st.session_state.language + " language. The cover letter is for a person named '" + st.session_state.name + "' who currently has the job title '" + st.session_state.current + "' and who is applying a job with the job title '" + st.session_state.desired + "'. In the cover letter, mention three skills which are shared by people with the job titles '" + st.session_state.current + "' and '" + st.session_state.desired + "' and explain why each skill is relevant to both job titles.",
         temperature=0.7,
         max_tokens=512,
         top_p=1,
         frequency_penalty=0,
         presence_penalty=0
      )
      st.write(response["choices"][0]["text"])
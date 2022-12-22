import os
import openai
import streamlit as st
st.set_page_config(initial_sidebar_state="collapsed")

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "Write a complete cover letter in the " + st.session_state.language + "language "
prompt += "for a person named " + st.session_state.name + " "
prompt += "who has " + st.session_state.years_of_experience + " years of professional experience."
prompt += "who most recently had the job title " + st.session_state.recent + ". "
if st.session_state.job_in_mind=='Yes':
   prompt += "They are applying for a job with the job title of " + st.session_state.desired + ". "
else:
   prompt += "They are applying for an unknown job so don't mention the job to which they are applying. "
if 'skills' in st.session_state and st.session_state.skills:
   prompt += "In the cover letter, mention that they have the following skills: "
   first = True
   for skill in st.session_state.skills:
      if first:
         prompt += skill
      else:
         prompt += ", " + skill
   prompt += ". In the cover letter, explain how each skill was learned in the job of " + st.session_state.recent
   if st.session_state.job_in_mind=='Yes':
      prompt += "and how it will be relevant to the job of " + st.session_state.desired
   else:
      prompt += ". "
else: 
   prompt += "In the cover letter, mention three ways that their experience in the job of " + st.session_state.recent + " has prepared them"
   if st.session_state.job_in_mind=='Yes':
      prompt += "for the job of " + st.session_state.desired
   else:
      prompt+= ". "
if st.session_state.gap=='Yes':
   prompt += "Explain that they have a gap in their work history because of " + st.session_state.gap_explanation + ". "
if st.session_state.strengths:
   prompt += "In the cover letter, mention that they have the following strengths: "
   first = True
   for strength in st.session_state.strengths:
      if first:
         prompt += strength
         first = False
      else:
         prompt += ", " + strength
   prompt += " and explain how each strength will apply to the job of " + st.session_state.desired + ". "
prompt += "Write the cover letter in a tone of voice which is " + st.session_state.working_style + ". "





response = openai.Completion.create(
   model="text-davinci-003",
   prompt=prompt,
   temperature=0.7,
   max_tokens=1024,
   top_p=1,
   frequency_penalty=0.2,
   presence_penalty=0
)

st.write(response["choices"][0]["text"])
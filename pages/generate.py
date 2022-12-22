import os
import openai
import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "Write a complete cover letter in the " + st.session_state.language + "language "
prompt += "for a person named " + st.session_state.name + " "
prompt += "who has " + st.session_state.years_of_experience " years of professional experience."
prompt += "who most recently had the job title " + st.session_state.recent + ". "
if st.session_state.job_in_mind=='Yes':
   prompt += "They are applying for a job with the job title of " + desired + ". "
if st.session_state.skills:
   prompt += "In the cover letter, mention that they have the following skills: "
   first = True
   for skill in skills
      if first:
         prompt += skill
      else:
         prompt += ", " + skill
   prompt += ". In the cover letter, explain how each skill was learned in the job of " + recent + " and how it will be relevant to the job of " + desired + ". "
else: 
   prompt += "In the cover letter, mention three ways that their experience in the job of " + recent + " has prepared them for the job of " + desired + ". "
if st.session_state.gap=='Yes':
   prompt += "Explain that they have a gap in their work history because of " + explanation_of_gap ". "
if st.session_state.strengths:
   prompt += "In the cover letter, mention that they have the following strengths: "
   first = True
   for skill in skills
      if first:
         prompt += skill
      else:
         prompt += ", " + skill
   prompt += " and explain how each strength will apply to the job of " + desired + ". "
prompt += "Write the cover letter in a tone of voice which is " + working_style + ". "





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
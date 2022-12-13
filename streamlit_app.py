import os
import openai

import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a professional cover letter that is two paragraphs long which is for a pre-school teacher named Sarah who is seeking to become an office administrator. Sarah’s skills are project planning, organization, and event facilitation. \n\nDear Hiring Manager,\n\nI am writing to express my interest in the Office Administrator position at your organization. With over 10 years of experience as a Pre-school Teacher, I believe I possess the necessary skills and enthusiasm to excel in this role.\n\nAs a Pre-school Teacher, I have had the opportunity to gain considerable experience in project planning, organization, and event facilitation. These skills have allowed me to take the lead on various projects, successfully plan and execute events, and provide assistance to parents and other members of the school community. I am confident that these skills have laid the groundwork for a successful transition into the Office Administrator role.\n\nI am eager to discuss my qualifications and experience in further detail. Thank you for your time and consideration.\n\nSincerely,\n\nSarah",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)



"""
# Imperfect Cover Letter



Generate an imperfect cover letter using the options below:
"""


with st.echo(code_location='below'):

with st.form("my_form"):
  option = st.selectbox('Select your current job title:', ('Product Manager', 'Engineer', 'UX Designer', 'Elementary School Teacher', 'Office Administrator', 'Homecare Nurse'))
  option = st.selectbox('Select your desired job title:',('Product Manager', 'Engineer', 'UX Designer', 'Elementary School Teacher', 'Office Administrator', 'Homecare Nurse'))
  option = st.multiselect('select your relevant skills:', ['writing email', 'event planning', 'writing spreadseets', 'care management', 'lesson planning'])  
  submitted = st.form_submit_button("Submit")
  
 

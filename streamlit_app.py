import os
import openai

import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")

#response = openai.Completion.create(
#  model="text-davinci-003",
#  prompt="Write a professional cover letter that is two paragraphs long which is for a pre-school teacher named Sarah who is seeking to become an office administrator. Sarah’s skills are project planning, organization, and event facilitation. \n\nDear Hiring Manager,\n\nI am writing to express my interest in the Office Administrator position at your organization. With over 10 years of experience as a Pre-school Teacher, I believe I possess the necessary skills and enthusiasm to excel in this role.\n\nAs a Pre-school Teacher, I have had the opportunity to gain considerable experience in project planning, organization, and event facilitation. These skills have allowed me to take the lead on various projects, successfully plan and execute events, and provide assistance to parents and other members of the school community. I am confident that these skills have laid the groundwork for a successful transition into the Office Administrator role.\n\nI am eager to discuss my qualifications and experience in further detail. Thank you for your time and consideration.\n\nSincerely,\n\nSarah",
#  temperature=0.7,
#  max_tokens=256,
#  top_p=1,
#  frequency_penalty=0,
#  presence_penalty=0
#)



"""
# Imperfect Cover Letter



Generate an imperfect cover letter using the options below:
"""

with st.form("my_form"):
   name = st.text_input(label='Enter your name:')
   current = st.text_input(label='Enter your current job title:')
   desired = st.text_input(label='Enter your desired job title:')
   language = st.selectbox('Select the language for your cover letter:',('English', 'Mandarin Chinese', 'Hindi', 'Spanish', 'French', 'Standard Arabic', 'Bengali', 'Russian', 'Portuguese', 'Indonesian', 'Urdu', 'Standard German', 'Japanese', 'Swahili', 'Marathi', 'Telugu', 'Western Punjabi', 'Wu Chinese', 'Tamil', 'Turkish', 'Korean', 'Vietnamese', 'Yue Chinese', 'Javanese', 'Italian', 'Egyptian Spoken Arabic', 'Hausa', 'Thai', 'Gujarati', 'Kannada', 'Iranian Persian', 'Bhojpuri', 'Southern Min Chinese', 'Hakka Chinese', 'Jinyu Chinese', 'Filipino', 'Burmese', 'Polish', 'Yoruba', 'Odia', 'Malayalam', 'Xiang Chinese', 'Maithili', 'Ukrainian', 'Moroccan Spoken Arabic', 'Eastern Punjabi', 'Sunda', 'Algerian Spoken Arabic', 'Sundanese Spoken Arabic', 'Nigerian Pidgin', 'Zulu', 'Igbo', 'Amharic', 'Northern Uzbek', 'Sindhi', 'North Levantine Spoken Arabic', 'Nepali', 'Romanian', 'Tagalog', 'Dutch', 'Sa\'idi Spoken Arabic', 'Gan Chinese', 'Northern Pashto', 'Magahi', 'Saraiki', 'Xhosa', 'Malay', 'Khmer', 'Afrikaans', 'Sinhala', 'Somali', 'Chhattisgarhi', 'Cebuano', 'Mesopotamian Spoken Arabic', 'Assamese', 'Northeastern Thai', 'Northern Kurdish', 'Hijazi Spoken Arabic', 'Nigerian Fulfulde', 'Bavarian', 'Bamanankan', 'South Azerbaijani', 'Northern Sotho', 'Setswana', 'Souther Sotho', 'Czech', 'Greek', 'Chittagonian', 'Kazakh', 'Swedish', 'Deccan', 'Hungarian', 'Jula', 'Sadri', 'Kinyarwanda', 'Cameroonian Pidgin', 'Sylheti', 'South Levantine Spoken Arabic', 'Tunisian Spoken Arabic', 'Sanaani Spoken Arabic'), index=0)
   submitted = st.form_submit_button("Submit")
   if submitted:
      response = openai.Completion.create(
         model="text-davinci-003",
         prompt="Write a complete cover letter which is two paragraphs long and in the " + language + " language. The cover letter is for a person named '" + name + "' who currently has the job title '" + current + "' and who is applying a job with the job title '" + desired + "'. In the cover letter, mention three skills which are shared by people with the job titles '" + current + "' and '" + desired + "' and explain why each skill is relevant to both job titles.",
         temperature=0.7,
         max_tokens=512,
         top_p=1,
         frequency_penalty=0,
         presence_penalty=0
      )
      st.write(response["choices"][0]["text"])


  
 

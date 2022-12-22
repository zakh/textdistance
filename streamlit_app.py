import os
import openai
import streamlit as st
import streamlit_extras
from inspect import getmembers, isfunction
    
functions_list = getmembers(streamlit_extras, isfunction)
st.write(functions_list)

openai.api_key = os.getenv("OPENAI_API_KEY")





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
      if 'name' not in st.session_state:
         st.session_state.name = name
      if 'current' not in st.session_state:
         st.session_state.current = current
      if 'desired' not in st.session_state:
         st.session_state.desired = desired
      if 'language' not in st.session_state:
         st.session_state.language = language
      ste.switch_page("fssdfs")



  
 

import os
import streamlit as st
from switchpage import switch_page

for key in st.session_state.keys():
    del st.session_state[key]
"""
# Imperfect Cover Letter



Generate an imperfect cover letter using the options below:
"""

with st.form('my_form'):
    st.session_state.name = st.text_input('Enter your name:')
    st.session_state.skin = st.radio('Let\'s start with your template. You can always change this later.',('Contempo','Pacific','Whitespace'))
    st.session_state.language = st.selectbox('Select the language for your cover letter:',('English', 'Mandarin Chinese', 'Hindi', 'Spanish', 'French', 'Standard Arabic', 'Bengali', 'Russian', 'Portuguese', 'Indonesian', 'Urdu', 'Standard German', 'Japanese', 'Swahili', 'Marathi', 'Telugu', 'Western Punjabi', 'Wu Chinese', 'Tamil', 'Turkish', 'Korean', 'Vietnamese', 'Yue Chinese', 'Javanese', 'Italian', 'Egyptian Spoken Arabic', 'Hausa', 'Thai', 'Gujarati', 'Kannada', 'Iranian Persian', 'Bhojpuri', 'Southern Min Chinese', 'Hakka Chinese', 'Jinyu Chinese', 'Filipino', 'Burmese', 'Polish', 'Yoruba', 'Odia', 'Malayalam', 'Xiang Chinese', 'Maithili', 'Ukrainian', 'Moroccan Spoken Arabic', 'Eastern Punjabi', 'Sunda', 'Algerian Spoken Arabic', 'Sundanese Spoken Arabic', 'Nigerian Pidgin', 'Zulu', 'Igbo', 'Amharic', 'Northern Uzbek', 'Sindhi', 'North Levantine Spoken Arabic', 'Nepali', 'Romanian', 'Tagalog', 'Dutch', 'Sa\'idi Spoken Arabic', 'Gan Chinese', 'Northern Pashto', 'Magahi', 'Saraiki', 'Xhosa', 'Malay', 'Khmer', 'Afrikaans', 'Sinhala', 'Somali', 'Chhattisgarhi', 'Cebuano', 'Mesopotamian Spoken Arabic', 'Assamese', 'Northeastern Thai', 'Northern Kurdish', 'Hijazi Spoken Arabic', 'Nigerian Fulfulde', 'Bavarian', 'Bamanankan', 'South Azerbaijani', 'Northern Sotho', 'Setswana', 'Souther Sotho', 'Czech', 'Greek', 'Chittagonian', 'Kazakh', 'Swedish', 'Deccan', 'Hungarian', 'Jula', 'Sadri', 'Kinyarwanda', 'Cameroonian Pidgin', 'Sylheti', 'South Levantine Spoken Arabic', 'Tunisian Spoken Arabic', 'Sanaani Spoken Arabic'), index=0)
    submitted = st.form_submit_button("Continue")
    if submitted:
        switch_page('job in mind')



  
 



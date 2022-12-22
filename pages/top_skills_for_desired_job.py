import os
import openai
import streamlit as st


def switch_page(page_name: str):
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("streamlit_app.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")


openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
   model="text-davinci-003",
   prompt="Return 13 skills which are related to the job of " + st.session_state.desired + " in the language of " + st.session_state.language + " in the format of a python list. Return only the python list.",
   temperature=0.7,
   max_tokens=512,
   top_p=1,
   frequency_penalty=0,
   presence_penalty=0
)
with st.form('my_form'):
    st.session_state.skills = st.multiselect('Choose your top job skills for the ' + st.session_state.desired + ' position.', response["choices"][0]["text"], horizontal=1)
    submitted = st.form_submit_button("Continue")
    if submitted:
        switch_page('strengths')

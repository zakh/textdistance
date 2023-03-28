import streamlit as st
from streamlit_typeahead import st_typeahead
import textdistance
import re

def read_strings_from_file(filename):
    with open(filename, 'r') as file:
        strings = [line.strip() for line in file.readlines()]
    return strings

def normalize_string(input_string):
    input_string = input_string.lower()
    input_string = input_string.replace('-', ' ')
    input_string = re.sub(r'[^a-z0-9\s]', '', input_string)
    return input_string

def find_closest_strings(input_string, strings, num_matches=5):
    similarities = [(string, textdistance.jaro_winkler(input_string, string)) for string in strings]
    sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
    return sorted_similarities[:num_matches]

def main():
    st.title("Job Title Matcher")

    job_titles = read_strings_from_file("jobtitles.txt")
    selected_job_title = st_typeahead(
        "Enter a job title:",
        options=job_titles,
        max_options=5,
        callback=find_closest_strings,
        debounce_time=200,
        min_chars=2,
        placeholder="Start typing a job title...",
    )

    if selected_job_title:
        st.header("Selected Job Title:")
        st.write(selected_job_title)

if __name__ == "__main__":
    main()

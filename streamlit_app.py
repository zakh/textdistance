import streamlit as st
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
    job_title = st.text_input("Enter a job title:")

    if job_title:
        normalized_job_title = normalize_string(job_title)
        strings = read_strings_from_file("jobtitles.txt")
        closest_strings = find_closest_strings(normalized_job_title, strings)

        st.header("Results:")
        for string, similarity in closest_strings:
            if similarity == 1:
                st.write(f"**Exact match:** {string}")
            else:
                st.write(f"{string} (Similarity: {similarity:.2f})")

if __name__ == "__main__":
    main()

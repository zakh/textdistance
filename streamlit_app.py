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

def find_closest_string(input_string, strings):
    max_similarity = -1
    closest_string = None
    
    for string in strings:
        similarity = textdistance.jaro_winkler(input_string, string)
        if similarity > max_similarity:
            max_similarity = similarity
            closest_string = string
    
    return closest_string, max_similarity






"""
# did you mean job title



Enter a job title: 
"""


  
 



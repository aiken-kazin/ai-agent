#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
import pandas as pd

from crew import AiHumanizer

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

# index = 0
# text = pd.read_csv("ai_written_text.csv").text[index]
text = "Hello Aiken, this is me, what are you doing?"
# print(text, '\n')

def get_human_written_text(text):
    """
    Run the crew.
    """
    inputs = {
        'text': text,
    }
    try:
        result = AiHumanizer().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")   

# print(get_human_written_text(text))
# def run():
#     """
#     Run the crew.
#     """
#     inputs = {
#         'text': text,
#     }
    
#     try:
#         AiHumanizer().crew().kickoff(inputs=inputs)
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")

# run()


# job-helper
Resume Analyzer

This is a Python script that uses OpenAI's GPT-3 language model to provide suggestions on how to improve a resume to better match a specific job posting. The script takes in a text file containing the resume and the job posting, and then prompts the GPT-3 model with a set of questions related to the job posting.

Prerequisites

In order to run this script, you will need to have an OpenAI API key. You can sign up for an API key on the OpenAI website.

You will also need to have Python 3.6 or higher installed on your machine, as well as the openai and streamlit Python packages.

Installation

Clone this repository to your local machine.
Install the required packages by running pip install -r requirements.txt.
Set your OpenAI API key as an environment variable named OPENAI_API_KEY. You can do this by running export OPENAI_API_KEY=YOUR_API_KEY in your terminal, or by adding export OPENAI_API_KEY=YOUR_API_KEY to your ~/.bashrc file (replace YOUR_API_KEY with your actual API key).
Run the script by running streamlit run resume_analyzer.py.
Usage

Run the script by following the installation instructions above.
Paste the text of the job posting into the "Job Posting" text box.
Upload the resume text file by clicking the "Browse files" button and selecting the file.
Select one or more prompts from the list of prompts provided. These prompts will be used to query the GPT-3 model.
Click the "Generate Suggestions" button to generate suggestions for improving the resume.
License

This code is licensed under the MIT License. See the LICENSE file for details.

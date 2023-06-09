import openai
import streamlit as st
import nltk
nltk.download('punkt')

openai.api_key = st.secrets['api_key']

prompts = [
    "How can the candidate's skills and experience be highlighted to better match the job requirements?",
    "What keywords and phrases from the job posting should be incorporated into the resume?",
    "Are there any relevant projects or achievements that could be added to the resume to better demonstrate the candidate's abilities?",
    "Is there any irrelevant information on the resume that should be removed to make it more concise and focused?",
    "How can the candidate's resume stand out from other applicants in the job market?",
    "Are there any specific metrics or data points that could be included to demonstrate the impact of the candidate's work?",
    "How can the candidate's resume demonstrate their ability to learn and adapt to new technologies or methodologies?",
    "Are there any relevant certifications or training programs that could be highlighted on the resume?",
    "How can the candidate's resume demonstrate their leadership and collaboration skills?",
    "Is there any additional information or context that could be added to the resume to make it more compelling to potential employers?",
    "Can you give a revised resume that better matches the job posting?"
]

# Streamlit app code
def app():
    st.title("Resume Improvement Tool")
    # st.write("Please select a prompt:")

    # # Prompt selection dropdown
    # prompt_choice = st.selectbox("Select a prompt", prompts)

    # Resume text input
    resume_text = st.text_area("Paste your resume text here")

    # Job posting text input
    job_posting_text = st.text_area("Paste the job posting text here")

    # Generate response button
    if st.button("Generate Response"):
        i = int(100/11)
        progress_text = "Generating feedback, please wait"
        progress_bar = st.progress(i, text=progress_text)
        for prompt_choice in prompts:
            progress_bar.progress(i, text=progress_text)
            response = generate_response(prompt_choice, resume_text, job_posting_text)
            st.divider()
            st.header(prompt_choice)
            st.markdown(response)
            i += int(100/11)

def count_tokens(text):
    tokens = nltk.word_tokenize(text)
    return len(tokens)

# Function to generate response using ChatGPT
def generate_response(prompt, resume, job_posting):
    prompt_text = f"{prompt}\nResume: {resume}\n And the following Job Posting: {job_posting}\n"
    num_tokens = count_tokens(prompt_text)
    pre_prompt = "Given the following resume "

    if num_tokens > 4097:
        st.warning("Please shorten your input text to less than 4097 tokens.  You are currently at {} tokens".format(num_tokens))
        st.stop()

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": pre_prompt + prompt_text}
        ]
    )


    return completion.choices[0].message['content']

if __name__ == "__main__":
    app()

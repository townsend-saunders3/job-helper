import openai
import streamlit as st

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
    "Is there any additional information or context that could be added to the resume to make it more compelling to potential employers?"
]

# Streamlit app code
def app():
    st.title("Resume Improvement Tool")
    st.write("Please select a prompt:")

    # # Prompt selection dropdown
    # prompt_choice = st.selectbox("Select a prompt", prompts)

    # Resume text input
    resume_text = st.text_area("Paste your resume text here")

    # Job posting text input
    job_posting_text = st.text_area("Paste the job posting text here")

    # Generate response button
    if st.button("Generate Response"):
        for prompt_choice in prompts:
            response = generate_response(prompt_choice, resume_text, job_posting_text)
        st.write(response)

# Function to generate response using ChatGPT
def generate_response(prompt, resume, job_posting):
    prompt_text = f"Prompt: {prompt}\nResume: {resume}\nJob Posting: {job_posting}\n"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_text,
        temperature=0.7,
        max_tokens=1024,
        n=1,
        stop=None,
        timeout=10,
    )

    return response.choices[0].text

if __name__ == "__main__":
    app()

import streamlit as st
from smart_email import generate_email

st.title("Smart Email Generator")

bullet_points = st.text_area("Enter bullet points:")
max_words = st.number_input("Enter a word count", step=1)
tone = st.selectbox("Select a tone:", ["Formal", "Casual", "Apologetic", "Enthusiastic"])

if st.button("Generate Email"):
    if bullet_points.strip() == "":
        st.warning("Please enter some bullet points.")
    else:
        with st.spinner("Generating your email..."):
            email = generate_email(bullet_points, tone, max_words)
            st.success("Done!")
            st.text_area("Generated Email", email, height=300)

            st.download_button("Download Email", email, file_name="email.txt")

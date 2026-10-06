import streamlit as st
from pathlib import Path
from pypdf import PdfReader

st.set_page_config(page_title="Smart Study Resource Finder")

st.title("📚 Smart Study Resource Finder")

st.write("Find study information from your PDF.")

data_folder = Path(__file__).parent / "data"

pdf_files = list(data_folder.glob("*.[pP][dD][fF]"))

if not pdf_files:
    st.error("No PDF found in the data folder.")
    st.write("Data folder:", data_folder)
else:
    st.success(f"{len(pdf_files)} PDF found!")

    full_text = ""

    for pdf_file in pdf_files:
        reader = PdfReader(str(pdf_file))

        for page in reader.pages:
            text = page.extract_text()

            if text:
                full_text += text + "\n"

    st.subheader("🔎 Search Study Material")

    question = st.text_input("Enter your topic or question")

    if st.button("Search"):

        if not question.strip():
            st.warning("Please enter a topic.")
        else:
            words = question.lower().split()
            sentences = full_text.split(".")

            results = []

            for sentence in sentences:
                sentence_lower = sentence.lower()
                score = sum(word in sentence_lower for word in words)

                if score > 0:
                    results.append((score, sentence.strip()))

            results.sort(reverse=True)

            st.subheader("📖 Relevant Results")

            if results:
                for score, result in results[:10]:
                    st.write("•", result)
            else:
                st.warning("No matching information found.")
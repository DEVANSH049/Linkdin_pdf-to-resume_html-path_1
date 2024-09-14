import streamlit as st
from resume_extraction.pdf_extractor import extract_text_and_links_from_pdf
from resume_extraction.llm_processing import extract_resume_sections
from resume_extraction.html_generator import generate_html_resume, download_html

def main():
    st.title("PDF Resume to HTML Generator with Editable Sections")

    # Step 1: Upload PDF
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

    if uploaded_file is not None:
        # Step 2: Extract text from PDF
        st.write("Extracting data from PDF...")
        resume_text, links = extract_text_and_links_from_pdf(uploaded_file)

        # Step 3: Process text with FLAN-T5
        st.write("Processing the resume using FLAN-T5 model...")
        resume_data = extract_resume_sections(resume_text, links)

        # Ensure summary is generated if not present
        if "summary" not in resume_data or not resume_data["summary"]:
            resume_data["summary"] = "A motivated professional with expertise in multiple domains."

        # Step 4: Allow users to edit the extracted data before generating HTML
        st.write("Edit the extracted sections before generating HTML:")
        resume_data["name"] = st.text_input("Name", resume_data.get("name", ""))
        resume_data["contact"] = st.text_area("Contact Information", resume_data.get("contact", ""))
        resume_data["summary"] = st.text_area("Summary", resume_data.get("summary", ""))
        resume_data["experience"] = st.text_area("Experience", resume_data.get("experience", ""))
        resume_data["skills"] = st.text_area("Skills", resume_data.get("skills", ""))
        resume_data["education"] = st.text_area("Education", resume_data.get("education", ""))
        resume_data["projects"] = st.text_area("Projects", resume_data.get("projects", ""))
        resume_data["publications"] = st.text_area("Publications", resume_data.get("publications", ""))
        resume_data["certificates"] = st.text_area("Certificates", resume_data.get("certificates", ""))

        # Step 5: Generate HTML Resume
        if st.button("Generate HTML Resume"):
            st.write("Generating HTML resume...")
            html_resume = generate_html_resume(resume_data)
            st.markdown(html_resume, unsafe_allow_html=True)
            st.markdown(download_html(html_resume), unsafe_allow_html=True)

if __name__ == "__main__":
    main()

# Linkdin_pdf-to-resume_html-path_1
This is a simple resume generator application built with Streamlit. It extracts resume information from a PDF file, processes it using a pretrained large language model (LLM), and generates a well-structured HTML resume.

#Project Structure 
bash
Copy code
resume_generator/
│
├── app.py               
├── requirements.txt            
├── resume_extraction/
│   ├── __init__.py             
│   ├── pdf_extractor.py        
│   ├── llm_processing.py       
│   └── html_generator.py       
└── assets/
    └── sample_resume.pdf       
#Model
This project uses the google/flan-t5-base model, a powerful transformer-based model, to process text and extract structured information from PDF resumes.

#Setup Instructions
1. Clone the Repository
bash
Copy code
git clone <repository-url>
cd resume_generator
2. Install Dependencies
Make sure you have Python installed. Then, install the required dependencies using:

bash
Copy code
pip install -r requirements.txt
3. Run the App
Launch the Streamlit application:

bash
Copy code
streamlit run app.py
The app will open in your default browser.

#Folder Structure Overview
app.py: Main file to run the Streamlit interface.
resume_extraction/: Contains modules to extract data from PDF, process it with the LLM, and generate HTML output.
pdf_extractor.py: Extracts raw text and links from a PDF file.
llm_processing.py: Uses the google/flan-t5-base model to process the extracted text and return structured information.
html_generator.py: Generates a structured HTML resume from the processed data.
assets/: Optional folder containing sample resumes for testing purposes.

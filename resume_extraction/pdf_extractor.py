import pdfplumber
import re

# Define section titles that could appear in the resume
section_titles = ['name', 'contact', 'Top skills', 'skills', 'certificate', 'summary', 'experience', 'education', 'projects', 'publications']

# def extract_text_and_links_from_pdf(pdf_file):
#     text = ""
#     links = []

#     with pdfplumber.open(pdf_file) as pdf:
#         for page in pdf.pages:
#             text += page.extract_text()
#             annotations = page.annots
#             if annotations:
#                 for annot in annotations:
#                     if 'URI' in annot:
#                         links.append(annot['URI'])

#     sections = extract_sections(text, section_titles)
#     return sections, links

def extract_text_and_links_from_pdf(pdf_file):
    try:
        text = ""
        links = []
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""  # Fallback to empty string if text not extractable
                annotations = page.annots
                if annotations:
                    for annot in annotations:
                        if 'URI' in annot:
                            links.append(annot['URI'])
        return extract_sections(text, section_titles), links
    except Exception as e:
        return {}, []  # Return empty dict and links if error occurs
# Function to extract sections dynamically
def extract_sections(text, section_titles):
    sections = {}
    section_regex = r'(?i)(' + '|'.join([re.escape(title) for title in section_titles]) + r')\b'
    
    section_positions = [(match.group(1), match.start()) for match in re.finditer(section_regex, text)]
    
    section_positions.append(("END", len(text)))
    
    for i in range(len(section_positions) - 1):
        section_title = section_positions[i][0].strip().lower()
        start_pos = section_positions[i][1]
        end_pos = section_positions[i + 1][1]
        section_content = text[start_pos:end_pos].strip()
        sections[section_title] = section_content

    return sections

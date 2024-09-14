import base64

# Generate HTML content from extracted resume data
def generate_html_resume(resume_data):
    html_content = f"""
    <html>
    <head><title>Resume</title></head>
    <body>
        <h1>{resume_data.get('name', 'Unknown Name')}</h1>
        <h2>Contact Information</h2>
        <p>{resume_data['contact']}</p>

        <h2>Summary</h2>
        <p>{resume_data['summary']}</p>

        <h2>Experience</h2>
        <p>{resume_data['experience']}</p>

        <h2>Skills</h2>
        <p>{resume_data['skills']}</p>

        <h2>Education</h2>
        <p>{resume_data['education']}</p>

        <h2>Projects</h2>
        <p>{resume_data['projects']}</p>

        <h2>Publications</h2>
        <p>{resume_data['publications']}</p>

        <h2>Certificates</h2>
        <p>{resume_data['certificates']}</p>
    </body>
    </html>
    """
    return html_content

# Function to create a downloadable link for the HTML resume
def download_html(html_content):
    b64_html = base64.b64encode(html_content.encode()).decode()
    href = f'<a href="data:text/html;base64,{b64_html}" download="resume.html">Download your resume as HTML</a>'
    return href

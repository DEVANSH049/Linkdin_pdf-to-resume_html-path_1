from transformers import T5ForConditionalGeneration, T5Tokenizer

# Initialize FLAN-T5 model
tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")

# Use FLAN-T5 to extract structured data from the resume
def extract_resume_sections(sections, links):
    resume_data = {}

    # Instruction for each section
    instructions = {
        "experience": "Extract the experience section from the text.",
        "skills": "Extract the skills section from the text.",
        "summary": "Generate a professional summary from the text.",
    }

    # Function to run FLAN-T5 on specific instructions
    def run_flan_t5(input_text, instruction):
        prompt = f"{instruction}: {input_text}"
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids
        output = model.generate(input_ids, max_length=500)
        return tokenizer.decode(output[0], skip_special_tokens=True)

    # Fill in sections using FLAN-T5
    for section, instruction in instructions.items():
        if section in sections:
            resume_data[section] = run_flan_t5(sections[section], instruction)
        else:
            resume_data[section] = ""

    # Return links as part of contact info
    resume_data['contact'] = sections.get('contact', "No contact info found.")
    resume_data['links'] = links if links else "No links found."

    # Return other sections directly if found
    for sec in ['name', 'education', 'projects', 'publications', 'certificates']:
        resume_data[sec] = sections.get(sec, "Not provided.")

    return resume_data

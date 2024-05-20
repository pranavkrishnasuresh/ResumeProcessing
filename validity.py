# import PyPDF2
# import ollama
# import httpx
# import spacy

# def extract_text_from_pdf(pdf_path):
#     try:
#         # Open the PDF file
#         with open(pdf_path, 'rb') as file:
#             reader = PyPDF2.PdfReader(file)
            
#             # Initialize an empty string to hold the text
#             text = ""
            
#             # Iterate through each page in the document
#             for page_num in range(len(reader.pages)):
#                 # Get the page
#                 page = reader.pages[page_num]
                
#                 # Extract the text from the page
#                 text += page.extract_text() + "\n"
        
#         return text
#     except Exception as e:
#         print(f"An error occurred while extracting text from the PDF: {e}")
#         return None

# def summarize_resume(text):
#     try:
#         response = ollama.chat(model='llama3', messages=[
#             {
#                 "role": "user", 
#                 "content": 'The following text is an applicant\'s resume. I want you to sort it and summarize it into the following categories: skills, projects, awards. Your output should have a very brief format, with the list of skills listed after skills. The list of projects with brief descriptions should be listed after the projects title. and a list of the awards should be given. Nothing else should be output. Don\'t give any introduction before giving this output, all I need is this output and nothing else. If you cannot find information for any of these fields, label it n/a. Here is the resume: ' + text,
#             },
#         ])
#         return response['message']['content']
#     except httpx.RequestError as e:
#         print(f"An HTTP request error occurred: {e}")
#         return None
#     except httpx.HTTPStatusError as e:
#         print(f"An HTTP status error occurred: {e.response.status_code} - {e.response.text}")
#         return None
#     except Exception as e:
#         print(f"An unexpected error occurred while summarizing the resume: {e}")
#         return None

# def parse_summary_with_spacy(summary_text):
#     nlp = spacy.load("en_core_web_sm")
#     doc = nlp(summary_text)
    
#     skills = []
#     projects = []
#     awards = []
    
#     current_category = None

#     for line in summary_text.split('\n'):
#         line = line.strip()
#         if line.startswith("Skills:"):
#             current_category = "Skills"
#             continue
#         elif line.startswith("Projects:"):
#             current_category = "Projects"
#             continue
#         elif line.startswith("Awards:"):
#             current_category = "Awards"
#             continue

#         if current_category == "Skills":
#             skills.append(line)
#         elif current_category == "Projects":
#             projects.append(line)
#         elif current_category == "Awards":
#             awards.append(line)
    
#     return {
#         "Skills": " ".join(skills),
#         "Projects": " ".join(projects),
#         "Awards": " ".join(awards)
#     }

# # Example usage
# pdf_path = '/Users/krishnasuresh/Desktop/Important Docs/Suresh_Pranavkrishna.pdf'
# job_description = "As a Data Analyst, you will be playing a pivotal role in interpreting data, analysing results, and providing various reports for accounting & financial domain. You will work closely with stakeholders to understand their data needs, develop analytical solutions, and present findings in a clear and actionable manner."
# key_responsibilities = "Data Collection and Analysis: Collect, clean, and analyse large datasets using statistical techniques and data visualization tools to identify trends, patterns, and correlations. Data Interpretation: Interpret data and translate findings into meaningful insights and actionable recommendations for business stakeholders. Reporting: Develop and maintain dashboards, reports, and data visualizations to communicate insights to stakeholders effectively. Data Quality Assurance: Ensure data integrity and accuracy by conducting data validation, quality checks, and troubleshooting data-related issues. Stakeholder Collaboration: Collaborate with cross-functional teams including marketing, finance, operations, and product development to understand their data needs and provide analytical support. Documentation: Document data analysis methodologies, assumptions, and findings to maintain transparency and facilitate knowledge sharing within the organization."
# skillset_requirements = "Proven experience as a Data Analyst or similar role, with a focus on data migration and conversion projects. Proficiency in MySQL, Excel and PHP for data extraction, transformation, and manipulation. Strong SQL skills with the ability to write complex queries for data extraction and manipulation. Solid understanding of data conversion methodologies, techniques, and best practices. Excellent attention to detail and analytical skills, with the ability to troubleshoot and resolve data-related issues. Effective communication skills with the ability to collaborate and coordinate with cross-functional teams. Prior experience in any Accounting &amp; Financial Projects, Clients or Any such would be a plus."
# try:
#     extracted_text = extract_text_from_pdf(pdf_path)
    
#     if extracted_text:
#         summarized_text = summarize_resume(extracted_text)
        
#         if summarized_text:
#             parsed_data = parse_summary_with_spacy(summarized_text)
#             print("Skills:", parsed_data["Skills"])
#             print("Projects:", parsed_data["Projects"])
#             print("Awards:", parsed_data["Awards"])
#         else:
#             print("Failed to summarize the resume.")
#     else:
#         print("Failed to extract text from the PDF.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")


import PyPDF2
import httpx
import ollama
import spacy

def extract_text_from_pdf(pdf_path):
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            
            # Initialize an empty string to hold the text
            text = ""
            
            # Iterate through each page in the document
            for page_num in range(len(reader.pages)):
                # Get the page
                page = reader.pages[page_num]
                
                # Extract the text from the page
                text += page.extract_text() + "\n"
        
        return text
    except Exception as e:
        print(f"An error occurred while extracting text from the PDF: {e}")
        return None

def summarize_resume(text):
    try:
        response = ollama.chat(model='llama3', messages=[
            {
                "role": "user", 
                "content": 'The following text is an applicant\'s resume. I want you to sort it and summarize it into the following categories: skills, projects, awards. Your output should have a very brief format, with the list of skills listed after skills. The list of projects with brief descriptions should be listed after the projects title. and a list of the awards should be given. Nothing else should be output. Don\'t give any introduction before giving this output, all I need is this output and nothing else. If you cannot find information for any of these fields, label it n/a. Here is the resume: ' + text,
            },
        ])
        return response['message']['content']
    except httpx.RequestError as e:
        print(f"An HTTP request error occurred: {e}")
        return None
    except httpx.HTTPStatusError as e:
        print(f"An HTTP status error occurred: {e.response.status_code} - {e.response.text}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while summarizing the resume: {e}")
        return None

def parse_summary_with_spacy(summary_text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(summary_text)
    
    skills = []
    projects = []
    awards = []
    
    current_category = None

    for line in summary_text.split('\n'):
        line = line.strip()
        if line.startswith("Skills:"):
            current_category = "Skills"
            continue
        elif line.startswith("Projects:"):
            current_category = "Projects"
            continue
        elif line.startswith("Awards:"):
            current_category = "Awards"
            continue

        if current_category == "Skills":
            skills.append(line)
        elif current_category == "Projects":
            projects.append(line)
        elif current_category == "Awards":
            awards.append(line)
    
    return {
        "Skills": " ".join(skills),
        "Projects": " ".join(projects),
        "Awards": " ".join(awards)
    }

def compare_with_job_description(skills, projects, awards, job_description, key_responsibilities, skillset_requirements):
    try:
        comparison_input = f"Skills:\n{skills}\n\nSkillset Requirements:\n{skillset_requirements}\n\nJob Description:\n{job_description}\n\nKey Responsibilities:\n{key_responsibilities}\n\nProjects:\n{projects}\n\nAwards:\n{awards}"
        response = ollama.chat(model='llama3', messages=[
            {
                "role": "user", 
                "content": 'The following text contains an applicant\'s skills, projects, and awards, along with a job description and key responsibilities. I want you to compare them and provide a score from 0 to 100 for how well the skills match the skillset requirements and how well the projects and awards match the job description and key responsibilities. Don\'t disadvantage an applicant who is overqualified or has more experience than is needed for the position. Provide two separate scores: one for skills and one for projects and awards. Your output should be in the format: "Skills Score: X, Projects and Awards Score: Y". Nothing else should be outputed, absolutely nothing else. Here is the comparison data: ' + comparison_input,
            },
        ])
        return response['message']['content']
    except httpx.RequestError as e:
        print(f"An HTTP request error occurred: {e}")
        return None
    except httpx.HTTPStatusError as e:
        print(f"An HTTP status error occurred: {e.response.status_code} - {e.response.text}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while comparing the data: {e}")
        return None

# Example usage
pdf_path = '/Users/krishnasuresh/Desktop/Important Docs/Suresh_Pranavkrishna.pdf'
job_description = "As a Data Analyst, you will be playing a pivotal role in interpreting data, analysing results, and providing various reports for accounting & financial domain. You will work closely with stakeholders to understand their data needs, develop analytical solutions, and present findings in a clear and actionable manner."
key_responsibilities = "Data Collection and Analysis: Collect, clean, and analyse large datasets using statistical techniques and data visualization tools to identify trends, patterns, and correlations. Data Interpretation: Interpret data and translate findings into meaningful insights and actionable recommendations for business stakeholders. Reporting: Develop and maintain dashboards, reports, and data visualizations to communicate insights to stakeholders effectively. Data Quality Assurance: Ensure data integrity and accuracy by conducting data validation, quality checks, and troubleshooting data-related issues. Stakeholder Collaboration: Collaborate with cross-functional teams including marketing, finance, operations, and product development to understand their data needs and provide analytical support. Documentation: Document data analysis methodologies, assumptions, and findings to maintain transparency and facilitate knowledge sharing within the organization."
skillset_requirements = "Proven experience as a Data Analyst or similar role, with a focus on data migration and conversion projects. Proficiency in MySQL, Excel and PHP for data extraction, transformation, and manipulation. Strong SQL skills with the ability to write complex queries for data extraction and manipulation. Solid understanding of data conversion methodologies, techniques, and best practices. Excellent attention to detail and analytical skills, with the ability to troubleshoot and resolve data-related issues. Effective communication skills with the ability to collaborate and coordinate with cross-functional teams. Prior experience in any Accounting &amp; Financial Projects, Clients or Any such would be a plus."

try:
    extracted_text = extract_text_from_pdf(pdf_path)
    
    if extracted_text:
        summarized_text = summarize_resume(extracted_text)
        
        if summarized_text:
            parsed_data = parse_summary_with_spacy(summarized_text)
            # print("Skills:", parsed_data["Skills"])
            # print("Projects:", parsed_data["Projects"])
            # print("Awards:", parsed_data["Awards"])
            
            comparison_result = compare_with_job_description(
                parsed_data["Skills"],
                parsed_data["Projects"],
                parsed_data["Awards"],
                job_description,
                key_responsibilities,
                skillset_requirements
            )
            if comparison_result:
                print(comparison_result)
            else:
                print("Failed to compare the resume with the job description.")
        else:
            print("Failed to summarize the resume.")
    else:
        print("Failed to extract text from the PDF.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
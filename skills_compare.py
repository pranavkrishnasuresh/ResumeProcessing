import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from dotenv import load_dotenv
from pymongo import MongoClient
import difflib

load_dotenv()

client = MongoClient(
    "mongodb+srv://db-mongodb-nyc1-27841-f7acc41c.mongo.ondigitalocean.com", 
    username='doadmin', 
    password='Y810j6C3ETy492ce'
)
db = client['admin']

prestored_names = ["CompanyName1", "JobTitle1"]

summary_hashmap = {}
percentage_hashmap = {}

def extract_skills(summary):
    skills_section = summary.split("Skills:")[1].split("Experiences:")[0].strip()
    return [skill.strip() for skill in skills_section.split(",")]

cursor = db.your_collection_name.find({
    "$or": [
        {"company": {"$in": prestored_names}},
        {"job": {"$in": prestored_names}}
    ]
})

for doc in cursor:
    name = doc.get('name')
    if name in summary_hashmap:
        summary_hashmap[name] += " " + doc.get('summary', "")
    else:
        summary_hashmap[name] = doc.get('summary', "")

inputjson = {
  "title": "Sample Title",
  "text": "Java, Python, C++",
  "company": "Apple Inc.",
  "position": "Software Engineer",
  "type": "short"
}

input_skills = [skill.strip() for skill in inputjson["text"].split(",")]

for name, summary in summary_hashmap.items():
    summary_skills = extract_skills(summary)
    
    match_percentage = 0
    for skill in input_skills:
        match_percentage += max(
            difflib.SequenceMatcher(None, skill, s).ratio() for s in summary_skills
        )
    
    match_percentage = (match_percentage / len(input_skills)) * 100
    percentage_hashmap[name] = match_percentage

print("Summary Hashmap:", summary_hashmap)
print("Percentage Hashmap:", percentage_hashmap)

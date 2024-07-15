# Data Pipeline: 
- Resume PDF -> Text -> Resume Summary -> Summary Iterative Categorization -> Score Resume with Baseline Meta LLama3 (Will be replaced with finetuned model) -> Generate 5 Interview Questions if scores are sufficient

# Input: 
- Resume in PDF Form, function will be integrated to pull resumes directly from Ceipal Database
Output: Resumes scored in 3 categories, 5 Personalized Interview Questions based on resume

# To Be Integrated:
- Fine-tuned model for resume scoring (awaiting access to dataset)
- Ceipol database for resume sourcing (awaiting access)
- Post function for transfering data to database

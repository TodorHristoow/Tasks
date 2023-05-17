import re

text = "Hi, my name is Jane and my phone number is 555-123-4567. My email address is jane_doe@example.com.\
 I live on 123 Main St. Apt. #456, and I was born on January 11th, 1990. I have an appointment on 2023-05-15\
  at 2:30pm at 789 Oak Ln. #3 and backup on 2023/05-21. Please give me a call or send me an email to confirm. \
  In case the dates are unavailable, please set up a meeting sometime in June. I would love June 19h. Thank you!"


pattern = r"\b\d{4}[-/]\d{2}[-/]\d{2}\b|\b(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}(?:st|nd|rd|th|h)?"
dates = re.findall(pattern, text)

for date in dates:
    print(date)

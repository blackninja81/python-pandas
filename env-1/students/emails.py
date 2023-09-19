import pandas as pd
import re
import logging

logging.basicConfig(
    filename='emaillogs.log',  
    level=logging.INFO,            
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Load the existing Excel file into a DataFrame
file_path = 'students.xlsx'
sheet_name='3C'
df = pd.read_excel(file_path, sheet_name)

# Generate unique email addresses based on student names and add them to the DataFrame
unique_emails = set()

def generate_unique_email(name):
    # Remove special characters from the student name using regex
    cleaned_name = re.sub(r'[^a-zA-Z\s]', '', name)
    # Split the cleaned student name by spaces
    names = cleaned_name.split()
    logging.info('Names without special characters %s', names)
    
    # Extract the first and last names (or the available names)
    first_name = names[0]
    first_letter = first_name[0]
    last_name = names[-1] if len(names) > 1 else ""
    # Generate a unique email address
    email = f"{first_letter.lower()}{last_name.lower()}@gmail.com"
    logging.info('Emails created for %s: %s', sheet_name, email)
    # Ensure the email is unique
    counter = 1
    while email in unique_emails:
        email = f"{first_name.lower()}.{last_name.lower()}{counter}@gmail.com"
        counter += 1
    unique_emails.add(email)
    return email

df['Email Address'] = df['Student Name'].apply(generate_unique_email)

# Save the modified DataFrame as a TSV file
tsv_file_path = 'students_emails_C.tsv'
df.to_csv(tsv_file_path, sep='\t', index=False)

print(f"Email addresses have been generated and saved as '{tsv_file_path}' in TSV format.")

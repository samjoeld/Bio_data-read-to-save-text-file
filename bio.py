import pandas as pd

# Read the data from Excel file into a DataFrame
data = pd.read_excel("data.xlsx")

# Format the data into the required BIO DATA - General Surgery format
output = "BIO DATA - General Surgery\n\n"
for index, row in data.iterrows():
    output += f"NO: {row['S.no']}\n"
    output += f"Name: {row['Name']}\n"
    output += f"Age: {row['Age']}\n"
    output += f"Sex: {row['Sex']}\n"
    output += f"Date of birth: {row['Date_of_birth ']}\n"
    output += f"Address: {row['Address']}\n"
    output += f"Father's name: {row['Father']}\n"
    output += f"Occupation: {row['FatherOccup']}\n"
    output += f"Mother's name: {row['Mother']}\n"
    output += f"Occupation: {row['Mother_occupation ']}\n"
    output += f"Parent's phone number: {row['Parent_phone ']}\n"
    output += f"Date of joining: {row['Date_of_joining ']}\n"
    output += f"Student's mobile number: {row['Student_phone_number']}\n"
    output += f"Student's Email ID: {row['Student_E-mail id']}\n\n"
    output += "\n"

# Print the output
print(output)

# Save the output to a text file
with open("output.txt", "w") as text_file:
    text_file.write(output)

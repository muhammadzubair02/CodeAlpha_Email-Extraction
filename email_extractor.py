import re

# Read data from file
with open("data.txt", "r") as file:
    content = file.read()

# Email pattern
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Extract emails
emails = re.findall(pattern, content)

# Print extracted emails
print("Extracted Emails:")

for email in emails:
    print(email)

# Save emails into another file
with open("emails.txt", "w") as file:

    for email in emails:
        file.write(email + "\n")

print("Emails saved in emails.txt")
#We are entering email and dividing it into two parts by strip
Email = input("Enter the Email: ").strip()
#We are taking the first part of Email before @
username = Email[:Email.index("@")]
# We are taking secodn half of email after @
domain_name = Email[Email.index("@")+1:]

format = (f"Yur username is: '{username}' and your domain name is: '{domain_name}'")
print(format)

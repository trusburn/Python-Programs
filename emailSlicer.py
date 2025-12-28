#Collect email from user
#Split the email using the @ symbol

def main():
    print("\nWelcome to the email splicer")
    print("")

    email_input = input("Enter email: ")
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ",username)
    print("Domain: ",domain)
    print("Extension: ",extension)
    
while True:
    main()

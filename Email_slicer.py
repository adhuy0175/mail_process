def Emailprocess(email):
    email_username = email[0:email.index('@')]
    email_domain = email[email.index('@') + 1:]
    return [email_username, email_domain]



def print_message(email_username, email_domain):
    print(f'User Name is {email_username} and Domain is {email_domain}')




def main(): 
    email = input("Please enter your email address").strip() #nhan 1 chuoi 
    email_username, email_domain = Emailprocess(email)
    print_message(email_username, email_domain)




if __name__ == '__main__':
    main()
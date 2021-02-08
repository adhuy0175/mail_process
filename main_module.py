from Email_slicer import Emailprocess,print_message



def main():
    emails = ["tranquanghuy@gmail.com","adhuy017@gmail.com","adhuy016@gmail.com"]
    for email in emails :
        userName,domain= Emailprocess(email)
        print_message(userName,domain)


if __name__ == "__main__":
    main()
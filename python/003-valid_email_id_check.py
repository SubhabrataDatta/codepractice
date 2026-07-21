#The code takes input from user and checks for a valid mail id
#by checking @ and (.co or .in or .uk) in the input 
#
#Explored Concepts
#Function, if-else, while not loop, in, search, list structure, any(), generator expression
#f string/formatted string literal, indentation, 

valid_domains = [".com", ".in",".co",".uk",".us"]

def sd_emailinput():
 email=input("Enter your mail ID \n : ")
 return email.lower()

emailid=sd_emailinput()


while not( "@" in emailid and any(domain in emailid for domain in valid_domains)):
 retry=input("The mail you have entered is invalid. To retry please type R and ENTER. To exit press any other key.")
 if retry.lower()!="r":
  break
  print("Mail Registration Failed! Exiting!")
 emailid=sd_emailinput()
else:
   print("\n\n")
   print(f"Your mail ID is now registered as {emailid}")
   print("\n\n")
  
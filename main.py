


user_input = input("""
           ***** BENGALURU➡️⬅️OOTY *****
  1.🚌ENTER CHOICE 1 TO GET THE BUS TICKET PRICE LIST🚌
  2.🛏️ENTER CHOICE 2 TO GET THE HOTELS FARES🛏️
  3.ENTER CHOICE 3 TO GET THE LIST OF PLACES TO VISIT IN  OOTY 
  4.💬ENTER CHOICE 4 TO DROP THE COMMENTS💬
   ©️©️ENTER YOUR CHOICE:""")

if user_input == "1":
    fp1 = open("file1.txt","r")
    print(fp1.read())
elif user_input == "2":
     fp2 = open("file2.txt","r")
     print(fp2.read())

elif user_input == "3":
    fp3 = open("file33.txt","r")
    print(fp3.read())

else:
    fp4 =  open("file4.txt","a")
    write_file = input(fp4.write(""))
    print(write_file)
    print("THANK YOU FOR YOUR COMMENTS")
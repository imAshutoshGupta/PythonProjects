'''
#main file
fp=open("data1.txt","w")
print(fp)
print(type(fp)) # Printing the type of the file object 'fp' (which will show it's a TextIOWrapper)
d="File handling"
fp.write(d)

fp=open("data1.txt","a")
d="Hello all"
fp.write(d)

fp.close()

'''
#contact directory project
def SearchByMobile():
 smob=input("Enter the mobile number to be saerched:")   # Ask the user for input: mobile number to be searched
 fp=open("data.txt","r")  # Open the file named "data.txt" in read mode and assign it to the variable 'fp'
 data=fp.readlines()#it will return list &  # Read all lines from the file into a list named 'data'
 #print(data)
 for x in data:   # Loop through each line in 'data'
    r=x.split(':')  # Split the current line by ':' and store the result in 'rec' (a list)
    if smob+'\n'==r[1]:  # Check if the input mobile number matches the one in the record
       print("Mobile number found",x)   # Print a message indicating that the mobile number is found along with the entire line
       fp.close() # Close the file

       break # Exit the loop
     #else:
        # print("Not found!!!")
         
         

def delete_record():
    emob=input("Enter the mobile number to be deleted") # Ask the user for input: mobile number to be deleted
    fp=open("data.txt","r")  # Open the file named "data.txt" in read mode and assign it to the variable 'fp'
    data =fp.readlines() # Read all lines from the file into a list named 'data'
    for x in data:#accessing the data
        rec=x.split(':')#it will split the list
        if emob+'\n'==rec[1]:#it will check
            data.remove(x)#it will remove the record which the user has entered
            fp1=open("data.txt","w")# Opening a file named "data1.txt" in write mode and assigning it to the variable 'fp'
            newdata=''.join(data)#converting the data from list to string
            fp1.write(newdata)#overriding the data
            fp1.close()
            print("Contact successfully deleted")
            break
     
    
def SearchByName(): # Function to search for a contact by name
     sname=input("Enter the name to be searched:")# Ask the user for input: name to be searched
     fp=open("data.txt","r") # Open the file named "data.txt" in read mode and assign it to the variable 'fp'
     data=fp.readlines()#it will return list  and # Read all lines from the file into a list named 'data'
     #print(data)
     for x in data:
         r=x.split(':')  # Split the current line by ':' and store the result in 'rec' (a list)
         if sname==r[0]:  # Check if the input name matches the one in the record
           print("Name found",x) # Print a message indicating that the name is found along with the entire line
           fp.close()

def update_record():  # Function to update a contact by mobile number
    mob=input("Enter mobile number to update record:")
    fp=open("data.txt","r")
    data =fp.readlines()
    for x in data:#accessing the data
        rec=x.split(':')#it will split the list
        if mob+'\n'==rec[1]:  # Check if the input mobile number matches the one in the record
            print("1.update mobile no.:")
            print("2.update Name:")
            ch=input("Enter your choice:")
            if ch=='1':
                nmob=input("Enter new mobile no.:")
                rec[1]=nmob+'\n'  # Update the mobile number in the record
                data.remove(x) # Remove the current line from the 'data' list
                temp=':'.join(rec) # Join the 'rec' list back into a string 'temp'
                data.append(temp)# Append the 'temp' string to the 'data' list
                fdata=''.join(data) # Join the 'data' list into a single string 'fdata'
                fp1=open("data.txt","w") # Open the file named "data.txt" in write mode and assign it to the variable 'fp1'
                fp1.write(fdata) # Write the 'fdata' string back to the file, effectively overwriting the data
                fp1.close()
                print("Record updated successfully!!!")  # Print a message indicating that the record is updated successfully
                
            elif ch=='2':
                print("update name")
            else:
                print("please enter valid choice")
            break
    else:
            print("No record found")
    
while True:
    print()
    print("1.Add Contact")
    print("2.View Contact")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.Search by mobile number")
    print("6.Search by name")
    print("7.Exit")
    ch=input("Enter your choice:")

    if ch=='1':
        fp=open("data.txt","a")
        n=input("Enter your name:")
        mob=input("Enter mobile number:")
        c=n+":"+mob+"\n" 
        fp.write(c)
        fp.close()
        
    elif ch=='2':
         fp=open("data.txt","r")
         cdata=fp.read()
         print("CONTACT DIRECTORY")
         print("===========================")
         print(cdata)
         fp.close()
         
    elif ch=='3':
         update_record() # Call the update_record function
    elif ch=='4':
        delete_record() # Call the delete_record function
    elif ch=='5':
         SearchByMobile()  # Call the SearchByMobile function
    elif ch=='6':
         SearchByName()  # Call the SearchByName function
    elif ch=='7':
         print("Thanks for using the application!!!")
         break
    else:
         print("Please enter a valid choice!!!")
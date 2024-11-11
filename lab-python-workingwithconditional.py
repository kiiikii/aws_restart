userReply = input("Do you need to ship a package? (Yes or No): ")

# Check for Yes or Y
if (userReply.lower() == "Yes" or "Y"):
    print("We can help with your ship that package!")
# Check for No or N
elif (userReply.lower() == "No" or "N"):
    print("We cannot help with your ship that package!")
# For any other input, print the fallback message
else:
    print("Please come back when you need to ship this package.")
    
print("-----")

reply = input("Would you like to but Stamp, an envelope, or make a copy ? (stamp, envelope, copy): ")
if reply == "stamp":
    print("We have many stamp designs to choose from.")
elif reply == "envelope":
    print("We have many envelope size to choose from.")
elif reply == "copy":
    while True:
        copies = input("How many copy do you need ? (Enter number): ")
        if copies.isdigit():
            print("Here are {} copies".format(copies))
            break
        else:
            print("please input the coorect number to copy")
else:
    print("Thank you please come again")
#check if db.txt exist
#if exits check if todays date exists
#if exists add track.py x  x will be added with that


#if db.txt not exists then it will create a db.txt file
#if date not exits then will create date in DD-MM-YY:0 format
#whatever count is adding will get added 


import os
import sys
from datetime import datetime

# Get the current date
today_date = datetime.now()
formatted_date = today_date.strftime("%d/%m/%y")

# Define the database file name
database_name = "db.txt"

# Check for the hour argument or "read" command
if len(sys.argv) > 1:
    if sys.argv[1].lower() == "read":
        # Show contents of db.txt
        if os.path.isfile(database_name):
            with open(database_name, "r") as file:
                print("Contents of db.txt:")
                for line in file:
                    print(line.strip())
        else:
            print(f"{database_name} does not exist.")
        sys.exit(0)  # Exit the program after showing the contents
    else:
        try:
            # Convert the argument to an integer for hours
            hour = int(sys.argv[1])
        except ValueError:
            print("Please provide a valid integer for the hour.")
            sys.exit(1)
else:
    print("Ashir, please don't forget to include the HOUR or use 'read'.")
    sys.exit(1)

# Read the file and process the dictionary
if os.path.isfile(database_name):
    dic = {}
    with open(database_name, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                key, value = line.split(":")
                dic[key] = int(value)  # Convert value to integer
    
    print(f"Current data: {dic}")

    # Update the dictionary
    if formatted_date in dic:
        dic[formatted_date] += hour
       
    else:
        dic[formatted_date] = hour
      

    # Write the updated dictionary back to the file
    with open(database_name, "w") as file:
        for key, value in dic.items():
            file.write(f"{key}:{value}\n")
else:
    # Create the file and add the new entry
    with open(database_name, "w") as file:
        file.write(f"{formatted_date}:{hour}\n")
    print(f"Created new file and added entry: {formatted_date}: {hour}")


# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each cadidate won

# Import the datetime class from the datetime module,
import datetime
# Use the now() attribute ib the datetime class to get the present time.
now = datetime.datetime.now()
#Print the present time.
print("The time right now is ", now)
# Import the datetime class from the datetime module.
import datetime as dt
#Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
import csv
dir(csv)
dir(counties_dict)
dir(str)
dir(int)
dir(float)
#Assign a variable for the file to load and the path
file_to_load = "Resources\election_results.csv"
#Open the election results and read the file.
election_data = open(file_to_load, "r")

# To do: perform analysis.

#Close the file.
election_data.close()
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: perform analysis
    print(election_data)
import os
dir(os.path)

import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file
with open(file_to_load) as election_data:
    # Print the file object.
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
#Write some data to the file.
outfile.write("Hello World")

#Close the file
outfile.close()

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson\n")

# Add our dependencies.
import csv
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader function.
file_reader = csv.reader(election_data)

#Print the header row
headers = next(file_reader)
print(headers)
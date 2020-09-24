#   In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
import csv
import os

#   Variable that points to the file
file_path="election_data.csv"
Total_Votes=0
Candidates=[]
OTooley_Votes=0



with open(file_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 

    # Read the header row first (skip this step if there is now header)
    next(csvreader,None)
    # Read each row of data after the header
    for x in csvreader:
    #   The total number of votes cast  
        Total_Votes = Total_Votes + 1
        New_Candidate=x[2]
        if New_Candidate not in Candidates:
            Candidates.append(New_Candidate)

        if New_Candidate == "O'Tooley":
            OTooley_Votes = OTooley_Votes + 1


       

            
    
    print("Votes:" + str(Total_Votes)) 
    print("")
    print("The Candidates were:") 
    x = ", ".join(Candidates)
    print(x)
    print("O'Tooley:" + str(OTooley_Votes))








#   The percentage of votes each candidate won

#   The total number of votes each candidate won

#   The winner of the election based on popular vote.

#   As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   ------

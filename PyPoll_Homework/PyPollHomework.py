#   In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
import csv
import os

#   Variable that points to the file
file_path="election_data.csv"
Total_Votes=0
Candidates=[]
OTooley_Votes=0
Khan_Votes=0
Li_Votes=0
Correy_Votes=0
#   Khan_pct=0




with open(file_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 

    # Read the header row first (skip this step if there is now header)
    next(csvreader,None)
    # Read each row of data after the header
    for x in csvreader:
    # The total number of votes cast  
        Total_Votes = Total_Votes + 1
    
    # The total number of votes each candidate won
       
        New_Candidate=x[2]
        if New_Candidate not in Candidates:
            Candidates.append(New_Candidate)

        if New_Candidate == "O'Tooley":
            OTooley_Votes = OTooley_Votes + 1

        if New_Candidate == "Khan":
            Khan_Votes = Khan_Votes + 1
        
        if New_Candidate == "Li":
            Li_Votes = Li_Votes + 1

        if New_Candidate == "Correy":
            Correy_Votes = Correy_Votes + 1

    #   The percentage of votes each candidate won

    print("***************************************************")
    print("Welcome to the Decision 2020 Headquarters")
    print("***************************************************")
    print("")
    print("The candidates in this year's election were:") 
    x = ", ".join(Candidates)
    print(x)
    print("")
    print("The total number of votes cast for all candidates was:" + str(Total_Votes))
    print()
    print("As predicted by the pollsters, Candidate Khan won the election by an historic margin!")
    print("")
    print("Khan:" + str(Khan_Votes)) 
    print("Correy:" + str(Correy_Votes))
    print("Li:" + str(Li_Votes))
    print("O'Tooley:" + str(OTooley_Votes))
    print("Khan:" + str(Khan_pct))









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

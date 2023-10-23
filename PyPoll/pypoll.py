import os
import csv

election_csv = os.path.join('PyPoll/Resources/election_data.csv')

candidates = []
single_candidate = []
total_votes = 0
county = []
percent_votes = []
Diana_DeGette = []
Charles_Casper_Stockham = []
Raymon_Anthony_Doane = []


with open(election_csv) as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')
    headcsv = next(readcsv)
    
    for row in readcsv:
        total_votes = total_votes + 1
        candidates.append(row[2])
        county.append(row[1])

    for candidate in candidates:
        if candidate == "Diana DeGette":
            Diana_DeGette.append(candidate)
            #Diana_Degette = len(Diana_Degette)
        if candidate == "Charles Casper Stockham":
            Charles_Casper_Stockham.append(candidate)
            #Charles_Casper_Stockham = len(Charles_Casper_Stockham)
        if candidate == "Raymon Anthony Doane":
            Raymon_Anthony_Doane.append(candidate)
            #Raymon_Anthony_Doane = len(Raymon_Anthony_Doane)
    
Diana_total = len(Diana_DeGette)
Charles_total = len(Charles_Casper_Stockham)
Raymon_total = len(Raymon_Anthony_Doane)

percentage1 = (Diana_total/total_votes) * 100
percentage2 = (Charles_total/total_votes) * 100
percentage3 = (Raymon_total/total_votes) * 100
    
percentage1 = str(round(percentage1, 2))
percentage2 = str(round(percentage2, 2))
percentage3 = str(round(percentage3, 2))


#find winner
if max(Diana_total, Charles_total, Raymon_total) == Diana_total:
    winner = "Diana DeGette"
if max(Diana_total, Charles_total, Raymon_total) == Charles_total:
    winner = "Charles Casper Stockham"
if max(Diana_total, Charles_total, Raymon_total) == Raymon_total:
    winner = "Raymon Anthony Doane"

#print results
print(f"Election Results\n")
print(f"----------------------------------------\n")
print(f"Total Votes: {str(total_votes)}\n")
print(f"----------------------------------------\n")
print(f"Diana DeGette: {percentage1}% ({str(Diana_total)})\n")
print(f"Charles Casper Stockham: {percentage2}% ({str(Charles_total)})\n")
print(f"Raymon Anthony Doane: {percentage3}% ({str(Raymon_total)})\n")
print(f"----------------------------------------\n")
print(f"Winner: {winner}")

#results to txt
with open("PyPoll/Resources/pypollanalysis.txt", "w") as text:
    text.write(f"Election Results\n")
    text.write(f"----------------------------------------\n")
    text.write(f"Total Votes: {str(total_votes)}\n")
    text.write(f"----------------------------------------\n")
    text.write(f"Diana DeGette: {percentage1}% ({str(Diana_total)})\n")
    text.write(f"Charles Casper Stockham: {percentage2}% ({str(Charles_total)})\n")
    text.write(f"Raymon Anthony Doane: {percentage3}% ({str(Raymon_total)})\n")
    text.write(f"----------------------------------------\n")
    text.write(f"Winner: {winner}")






import os
import csv

csvpath = os.path.join("Resources","PyPoll.csv")
textPath = os.path.join("Analysis","PyPoll_Analysis.txt")



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    print (header)

    total_votes = 0
    candidates = []
    votes ={}
    vote_percentage ={}


    for row in csvreader:
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            print(candidates)

            votes[row[2]] = 0
            # print(votes)

        votes[row[2]] = votes[row[2]] + 1
    
    # print(candidates)
    # print(total_votes)
    print("Here are the votes")
    print(votes)
    print("_______________________")
    
    maxvotes = 0
    winner = ""   
    
    with open(textPath, 'w', newline='') as textfile:
    # with open(textPath, ‘w’, newline=‘’) as textfile:
        textfile.write(f'Election Results  \n')
        textfile.write(f'---------------------\n')
        textfile.write(f'Total Votes: {total_votes}\n')
        textfile.write(f'----------------------\n')
        
        

        for row in votes:
            vote_percentage[row] = round(((votes[row]/total_votes)*100),2)
            results = f'{row}: {vote_percentage[row]}% ({votes[row]})\n'
            print ("------------------")
            print(results)
            if votes[row] > maxvotes:
                maxvotes = votes[row]
                winner = row
            # print(row,vote_percentage[row],votes[row])
            # results = f'{row}: {vote_percentage[row]}% ({votes[row]})\n'
            # print ("------------------")
            # print(results)
            print("Winner: " + winner)
            textfile.write(f'{results}\n')
        



    # with open(textPath, 'w', newline='') as textfile:
    #     textfile.write(f'   Election Results   \n') 
        # textfile.write(f'----------------------\n')
        # textfile.write(f'Total Votes: {total_votes}\n')
        # textfile.write(f'----------------------\n')
        textfile.write(f'----------------------\n')
        textfile.write(f'Winner: {winner}\n')
        textfile.write(f'----------------------\n')
        

# textfile.write(f'Greatest Increase:  {max_change[0]} ($ {max_change[1]})\n' )

    
    # print(votes)
    # print(vote_percentage)



    # print(winner)
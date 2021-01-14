import os
import csv

csvpath = os.path.join("Resources","PyBank.csv")
textPath = os.path.join("Analysis","PyBank_Analysis.txt")



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    # print (header)

    total_months = 0
    total_sum = 0
    change = 0
    previous = 0
    average_change = []
    final_average = 0
    max_change = ["",0]
    min_change = ["",9999999999]

    for row in csvreader:
        total_months += 1
        total_sum += int(row[1])
        change = int(row[1]) - previous
        average_change.append(change)
        previous = int(row[1])
        if change > max_change[1]:
            max_change[1] = change
            max_change[0] = row[0]
        
        if change < min_change[1]:
            min_change[1] = change
            min_change[0] = row [0]

    final_average = round((sum(average_change[1:])/len(average_change[:-1])),2)


    print (total_months)
    print (total_sum)
    # print (previous)
    # print(average_change)
    print(final_average)
    print (max_change[0],max_change[1])
    print (min_change[0],min_change [1])


    with open(textPath, 'w', newline='') as textfile:
        textfile.write(f'Total Months:  {total_months}\n' )
        textfile.write(f'Total Sum: $ {total_sum}\n' )
        textfile.write(f'Final Average Change: $ {final_average}\n' )
        textfile.write(f'Greatest Increase:  {max_change[0]} ($ {max_change[1]})\n' )
        textfile.write(f'Greatest Decrease:  {min_change[0]} ($ {min_change[1]})\n' )
        # textfile.write(max_change[0],max_change[1])
        # textfile.write(min_change[0],min_change [1])




    # # Initialize csv.writer
    # csvwriter = csv.writer(csvfile, delimiter=',')

    # # Write the first row (column headers)
    # csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # # Write the second row
    # csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])



  





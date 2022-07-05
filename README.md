# python-challenge
> Module 3 - Python challenge: PyBank and PyPoll
This project will showcase coding using Python.


## PyBank Instructions
Analyze the financial records from the dataset budget_data.csv. Create a Python script which outputs a financial analysis of the following:

* Total # of months
* Net total Profit/Losses over the period
* Changes in "Profit/Losses" over the period, then the average of the changes
* Greatest increase in profits (date and amt)
* Greatest decrease in profits (date and amt)

The final script should print the _financial analysis_ output in terminal and write to the "analysis" folder.
## PyBank Analysis

This is the given analysis to compare my answers to:

```Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558) 
```

## PyBank Code Theory

1. First we import the relevant modules (os, csv)
2. Input and output variables are set to read the CSV file and then write the results to a text file.
3. Lists are created to store the data from the CSV files. 
4. General variables are set to 0 to ensure they're ready for calculations later on.
5. The CSV is opened and its rows are set and indexed after the header.
6. Data for each row is added to lists and the change btw months is calculated and stored.
7. Then come the following calculations: count of months, average change of revenue, greatest increase in profits and greatest decrease.
8. All values are printed in the terminal window as well as into a text file.

---

## PyPoll Instructions
Help a small, rural town to modernize it's vote-counting process. Using the provided election_data.csv, create a Python script to analyze the votes and calculate the following:

* Total # of votes cast
* List of candidates who received votes
* Percentage of votes each candidate won
* Total # of votes each candidate won
* The winner of the election based on popular vote

The final script should print the _election results_ output in terminal and write to the "analysis" folder.

## PyPoll Analysis
This is the given analysis to compare my answers to:
```Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
```

## PyPoll Code Theory

1. First we import the relevant modules (os, csv)
2. Input and output variables are set to read the CSV file and then write the results to a text file.
3. Lists are created to store the data from the CSV files
4. General variables are set to null or 0 to ensure they're ready for use later on in the code.
5. The CSV is opened and its rows are set and indexed after the header. A counter is also added for the ballots.
6. For every row, the ballot counter is incremented and it's data is indexed and stored.
7. We check to see if the counties and candidates exist in their respective lists and if not they are added, and the counter is increased.
8. Then we calculate the # of votes and percent of votes for each candidate.
9. We format the output to display the numbers for these candidates.
10. The most votes is calculated by comparing the total votes fo the candidates.
11. We format the output to display the winning candidate.
12. All values are printed in the terminal window as well as into a text file.


---
Hints and Considerations

* Consider what you've learned so far. You've learned how to import modules like csv. You’ve learned how to read and write files in various formats. You’ve learned how to store content in variables, lists, and dictionaries. You’ve learned how to iterate through basic data structures. And you’ve learned how to debug along the way. Using all that you've learned, try to break down your tasks into discrete mini-objectives.

* The datasets for these Challenges are quite large. This was done purposefully to showcase one of the limits of Excel-based analysis. As data analysts, our first instinct is often to go straight to Excel, but creating scripts in Python can provide us with more powerful options for handling big data.

* Write one script for each of the provided datasets. Run each script separately to make sure that the code works for its respective dataset.

* Always commit your work and back it up with pushes to GitHub or GitLab. You don't want to lose hours of your hard work! Also make sure that your repo has a detailed README.md file.

---
Assignments and other documentation sourced from the Georgia Tech Boot Camp, Summer/Fall 2022
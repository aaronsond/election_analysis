# Election Analysis

## Overview of Election Audit

Client requested that we provide an audit of a Colorado congressional election. We were asked to look at county level turnout, votes cast for each candidate, and to determine the winner of the election. We provided the following results for them, based on data provided to us.

![Printed results from analysis](Resources/Results_printout.png)

## Election-Audit Results

* The total count of votes was 369,711
* 306,055 total votes in Denver, 38,855 in Jefferson, 24801 in Arapahoe county. 
* Denver had the largest number of votes.  
* Candidates recieved the following vote counts and percentages:
  * Charles Casper Stockham: 23.0% (85,213)
  * Diana DeGette: 73.8% (272,892)
  * Raymon Anthony Doane: 3.1% (11,606)
* Diana DeGette won this election by popular vote, with 272,892 votes cast for her, equaling 73.8% of all votes cast.

## Election-Audit Summary

The code used to read the data and output results automatically pulls the candidate names, county names, and vote totals from the data itself. It could easliy be re-used on many other data sets, simply by changing the file that it looks at. The use of open ended variables allows for easy re-use. 

### Suggested Modifications for Future Elections Analysis

If we were looking at national elections, we could add in code to look at state vote counts, percentages, and other factors, or we could re-factor existing county level analysis code to do this. We could also add in additional variables if we wanted to simultaneously look at more than one item per ballot. For instance, if we wanted to look at how these votes went for Governor and Lieutenant Governor, we could pull that data in, then repeat existing code, with new variables, to also output results for this additional election. 

## Resources

- Data source: election_results.csv
- Software: Python 3.8.5, Visual Studio Code 1.55.0

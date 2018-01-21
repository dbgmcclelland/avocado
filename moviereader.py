#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dave
#
# Created:     17-01-2018
# Copyright:   (c) Dave 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import csv

# Setting up export variables as empty dictionaries

movieData = {}
yearData = {}
dirData = {}
userBallot = {}
userData = {}

# Function to export each dictionary to CSV

def csvExport(outfile, source):
        with open(outfile, 'wb') as csv_file:
            writer = csv.writer(csv_file, delimiter = ";")
            for key, value in source.items():
                writer.writerow([key, value])

# CSV reader that reads source spreadsheet and totals fans for each title, year, and director. Also builds ballots for each user that voted.

with open("Avocado.csv", "rb") as csvfile:
    moviereader = csv.reader(csvfile, delimiter = ";")
    for row in moviereader:
        fans = 0
        title = row[0]
        director = row[1]
        year = str(row[2])
        length = len(row) - 1
        for x in range(3, length):
            if row[x] != '':
                fans += 1
                user = row[x]
                if row[x] not in userBallot:
                    userBallot[user] = []
                    userBallot[user].append(title)
                else:
                    userBallot[user].append(title)
        movieData[title] = fans
        if year not in yearData:
            yearData[year] = fans
        else:
            yearData[year] += fans
        if director not in dirData:
            dirData[director] = fans
        else:
            dirData[director] += fans

# Loop through each user ballot to determine the total score of each user

for user, filmlist in userBallot.iteritems():
    userData[user] = 0
    for film in filmlist:
        fans = movieData[film]
        userData[user] += fans

# Exports the four completed dictionaries to CSV

csvExport("faveMovies.csv", movieData)
csvExport("faveYears.csv", yearData)
csvExport("faveDirectors.csv", dirData)
csvExport("userScores.csv", userData)





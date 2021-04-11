#!/usr/bin/env python3
# congrats to whoever's reading this, here's a challenge for you: http://bit.ly/rot13willbehelfulateron
# now fuck off

import csv

botsList = []

# Search Terms
searchTerms = ["2021-04-02 00:00:30", "2021-04-02 00:02:22", "2021-04-02 00:02:23", "2021-04-10 02:39:03", "2021-04-10 02:39:04", "2021-04-10 03:16:08", "2021-04-10 04:42:30"]
for i in range(59, 143):
    searchTerms.append('2021-04-10 03:{}:{:02d}'.format(17 + (i // 60), i % 60))

# Searching for searchTerms in database
with open('f.csv') as followList:
    csvForm = csv.reader(followList)
    for i in csvForm:
        if i[3] in searchTerms:
            botsList.append(i[0])

# Saving to a file
with open('botsList', 'w') as outputFile:
    for bot in botsList:
        outputFile.write('{}\n'.format(bot))

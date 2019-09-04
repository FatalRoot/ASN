'''
Final Project - Kassandra Bethune
Python v3.7
Sep 9, 2019
Script uses requests, re, and json libraries
To gather ASN's from URL, remove duplicates and save to file.
'''


import requests
import re


def getAsnData():
    # Let user know we are attempting to connect to URL
    print("Attempting to connect to ASN site...")
    try:
        asnUrl = "https://ipinfo.io/countries/cn"
        # verifies web-page is accessible
        pageData = requests.get(url= asnUrl)
        print("Accessed website.", pageData.status_code)
        # if http code is 200, return html page text
        if pageData.status_code == 200:
            return pageData.text
        else:
            # don't return anything, will work on way to handle empty return
            return ""
        # if page is unreachable, returns error.
    except Exception as err:
        raise SystemExit("Website unreachable: " + str(err))

print("Attempting to grab ASNs from web page...")
webPageText = getAsnData()

# reads the text from page_data and scans for all ASN numbers
asns = re.findall("AS\d{3,6}", webPageText)

# remove duplicates from list
asnsFinal = list(set(asns))
print("Gathered ASNs and removed duplicates.")

# prints the number of ASNs found.
print(str(len(asnsFinal)) + " ASNs in China.")

print("Saving ASNs to asnlist.txt")
# creates file if doesn't exist and writes ASN data to file
asnFile = open("asnlist.txt", "w+")

# writes each ASN to new line in file
for asn in asnsFinal:
    asnFile.write(asn + '\n')

# close file
asnFile.close()
print("Done nerds.")


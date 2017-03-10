import TextAnalysis


def openfile(filename):
    file = open(filename)
    file = file.read()
    words = file.split()
    limit = len(words)
    return file



text=openfile("scam2.txt")

#EMAIL ANALYSIS algorithm in TextAnalysis

def emailanalysis(text):

    if (TextAnalysis.getemail(text))is not None:
        mail = TextAnalysis.getemail(text)
        print mail
        print "Found Email Searching Databases"
        if TextAnalysis.emailsearch(mail)!="Not found email is clean":
            print "Scammer Found by Email Address"
            terminate=1
    else:
        print "No email found"
#ADDRESS FINDER AND CHECKER

def addressfinder(text):
    if (TextAnalysis.getaddress(text)) is not None:
        address = TextAnalysis.getaddress(text)
        if TextAnalysis.AddressGeo(address) is not None:
            print "Address Exists"
        else:
            print "We couldn Lookup the address"



text=openfile("scam2.txt")
addressfinder(text)
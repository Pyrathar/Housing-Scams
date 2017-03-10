import emailanalysis
from postal.parser import parse_address
import re
import nltk
import time
import numpy

emaillist = ["dorissmorgans@gmail.com", "krishraj660@gmail.com", "mrsdonnawilliams01@gmail.com", "dhldeliverycompanycode141@gmail.com", "office_filess@yahoo.com",]

text =" Hello Carolina and Paulo,Good day and thanks for the response. the apartment is still free the address is Denmark Lyngsby Hestegangen 6 and you can start to rent as soon as possible but sorry viewing the flat will not be possible for now because i have left the country already and i have the flat keys here with me, I just relocated here in England due to my new job and that is the main reason I am renting outthe flat but I can only send you some of the flat pictures to see and have an idea  of the flat. I will be waiting to hear from you soon. Where are you now and what date do you intend to start renting and move into the flat?, has to be made in Western Union my email is blackninja@gmail.com"



def getemail(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    email=str(match.group(0))
    return email

def getaddress(text):

 address=parse_address(text)

 for i in range(len(address)):

     if address[i][1]=="road":
        print "Road " + address[i][0]
        UserAddress = address[i][0]
        UserAddress.ljust(2)
     if address[i][1]=="house_number":
         if (address[i][0]).isdigit():
             print "House number" + address[i][0]
             UserAddress = UserAddress + " " +address[i][0]

 return UserAddress

def processLanguage(text):

            tokenized = nltk.word_tokenize(text)
            tagged = nltk.pos_tag(tokenized)

#still a mess
            namedEnt = nltk.ne_chunk(tagged)

            VPs_str = [" ".join(namedEnt.leaves()) for namedEnt in list(namedEnt.subtrees(filter=lambda x: x.label() == 'PERSON'))]
            print VPs_str
            for subtree3 in namedEnt.subtrees():
                if subtree3.label() == 'ORGANIZATION' or subtree3.label() == 'PERSON' :
                    for leaf in namedEnt:
                        print leaf




            time.sleep(1)
emailanalysis.emailsearch(emaillist)

words = text.split()
getaddress(text)
for i in words:
    temp = []
    index= words.index(i)

    while len(temp) != 7:
     temp.append(words[index])
     index = index+1
     if len(temp) == 7:
         print temp

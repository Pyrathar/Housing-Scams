from bs4 import BeautifulSoup
import urllib2
from cookielib import CookieJar

#Complete

def emailsearch(emaillist):
 print emaillist
 cj = CookieJar()
 opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
 opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]


 for email in emaillist:


  path = "http://scammed.by/indexfrom.php?email=" + email
  sourceCode = opener.open(path).read()
  soup = BeautifulSoup(sourceCode)

  print email
  letters = soup.find_all("div",class_="previewsubject")
  returnstatement = "http://scammed.by/" + letters[0].a["href"]
  return returnstatement

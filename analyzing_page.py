import urllib.request
from io import StringIO
from html.parser import HTMLParser
from collections import Counter
import operator

#----------------------------------------
fp = urllib.request.urlopen("http://www.python.org")#URL
mybytes = fp.read()
html_var = mybytes.decode("utf8")
fp.close()
#database access
#----------------------------------------

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def linkfinder(html_var):
    x = html_var.split('"')
    j=0
    links_numb=0
    for i in x:
        last = x[j]
        if (last[0:4] == "http")or(last[0:3] == "www"): 
            #print(last) #print link
            links_numb += 1
        j += 1
    print("Links:"+str(links_numb))
    return links_numb

def full_to_raw(html):
    global rowhtml
    s = MLStripper()
    s.feed(html)
    rowhtml = s.get_data()
    return rowhtml

def countwordnothtml(html):#count wihtout html
    rowhtml = full_to_raw(html)
    words_numb = len(rowhtml.split()) 
    print("words no html:"+str(words_numb))
    return words_numb

def countwords(html_var):#raw
    words_numb = len(html_var.split()) 
    print("word with html:"+str(words_numb))
    return words_numb

def countwordsmultiple():#rowhtml
    x=dict(Counter(rowhtml.split()))
    print (type(x))
    #sort
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))
    print(sorted_x)
    #blacklist ex. "and"
    
def main():
    cw=countwords(html_var)
    lf=linkfinder(html_var)
    cwh=countwordnothtml(html_var)
    countwordsmultiple()
    
if __name__ == "__main__":
    main()

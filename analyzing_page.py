import urllib.request
from io import StringIO
from html.parser import HTMLParser

#----------------------------------------
fp = urllib.request.urlopen("http://www.python.org")#URL
mybytes = fp.read()
global html_var
html_var = mybytes.decode("utf8")
fp.close()
#database access
#get data
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

def countwordnothtml(html):#count wihtout html
    s = MLStripper()
    s.feed(html)
    rowhtml = s.get_data()
    words_numb = len(rowhtml.split()) 
    print("words no html:"+str(words_numb))

def countwords(html_var):#raw
    words_numb = len(html_var.split()) 
    print("word with html:"+str(words_numb))

def main():
    countwords(html_var)
    linkfinder(html_var)
    countwordnothtml(html_var)
    
if __name__ == "__main__":
    main()

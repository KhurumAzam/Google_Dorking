import googlesearcher
from googlesearcher import *

class GoogleDorking:
    domain = ""
    tld = ""
    def __init__(self):
        pass
    def askDomain(self):
        try:
            self.domain = input("What's the website your Dorking: ")
            self.tld = self.domain.split('.')[1]
        except Exception as e:
            print("Error with input", e)

    def dorking(self):
        try:
            exploitDB = input("Where's the file location: ")
            f = open(exploitDB, "r")
            with open(f, "r") as g:
                contents = f.read()
                googlesearcher.search(self.domain + contents, self.tld,lang='en',safe='off', num=1, start=0, stop=None, pause=2)

        except Exception as e:
            print("Error with code", e)


if "__main__" == __name__:
    obj = GoogleDorking()
    obj.askDomain()
    obj.dorking()

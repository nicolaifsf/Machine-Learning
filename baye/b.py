from decimal import *
class Sayer:
        def __init__(self, w, filename):
                self.whoBy = w
                self.word = readIn(filename)

def readIn(filename):
    l = []
    f = open(filename)
    for line in f.readlines():
            line = line.strip()
            line = line.upper()
            word = line.split(' ')
            l.append(word)

    return l 
    

# def start():

def parse(phrase, sayer1, sayer2):
        phrase = phrase.upper()
        phrase = phrase.split(' ')
        cS1 = 0.0
        cS2 = 0.0
        totalNumPhrases = len(sayer1.word) + len(sayer2.word)
        cS1 = float(len(sayer1.word))/float(totalNumPhrases)
        s1NumWords = 0.0
        for i in sayer1.word:
                s1NumWords += len(i)
        cS2 = float(len(sayer2.word))/float(totalNumPhrases)
        s2NumWords = 0
        for i in sayer2.word:
                s2NumWords += len(i)
        for w in phrase:
                w = w.upper()
                c1 = 0;
                for each in sayer1.word:
                        c1 += each.count(w) 
                c1 = float(c1) / float(s1NumWords)
                cS1 *= c1
                c2 = 0
                for each in sayer2.word:
                        c2 += each.count(w)
                c2 = float(c2)/float(s2NumWords)
                cS2 *= c2

        if(cS1 > cS2):
                sayer1.word.append(phrase)
                print sayer1.whoBy
        else:
                for i in phrase:
                        i = i.upper()
                sayer1.word.append(phrase)
                print sayer2.whoBy





# s1 = Sayer("Kant", "file.txt")
# s2 = Sayer("Heidegger", "file2.txt")
# parse("Transcendental Being is knowledge", s1, s2)
# parse("Intuition is Knowledge", s1,s2)

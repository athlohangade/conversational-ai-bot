class HTMLParsed:

    def __init__(self, l = None):
        if not l:
            self.parsed = []
        else:
            self.parsed = l
        self.d = {}

    def addParsed(self, para, heading = None):
        if heading:
            self.d[heading] = para
        for i in para:
            self.parsed.append(i)

    def getParagraphForheading(self, heading):
        return self.d.get(heading, None)

    def getheadings(self):
        return self.d.keys()

    def getparagraphs(self):
        return self.parsed



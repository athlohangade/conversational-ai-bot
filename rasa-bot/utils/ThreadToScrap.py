import threading
import time
from utils.ScrapAllWebpages import ScrapAllWebpages

class ThreadToScrap (threading.Thread):

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        ScrapAllWebpages.scrap_all()

        


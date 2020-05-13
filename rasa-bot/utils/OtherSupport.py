import csv

class OtherSupport:

    @classmethod
    def getResponse(cls, entities):

        link = None
        message = "Sorry, I didn't get that. Can you please rephrase the query?"
        found = False

        with open('lookup-files/keywords-urls.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    for e in entities:
                        if e['value'] == row[0]:
                            link = row[1]
                            message = row[2]
                            found = True
                            break
                    if found:
                        break
                line_count += 1

        res = [message, link]
        return res
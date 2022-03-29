import csv
import datetime


def parse_time(text):
    return datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S.%f")


with open('messages.csv', encoding='utf8') as f:
    messages = list(csv.reader(f, delimiter=','))
    graph = {line[0]: line[1:] for line in csv.reader(f, delimiter=',')}
with open('results.csv', encoding='utf8') as f:
    results = list(csv.reader(f, delimiter=','))


def init():
    results = {}
    with open('messages.csv', encoding='utf8') as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            #print(row)
            results[row[0]] = row[1:]
            counter += 1
        #print(counter)
    return results


if __name__ == "__main__":
    print(messages[0])
    print(results[0])
    #print(graph)
    #print('\n')
    #print(init())
    print(init())

import csv

def write_hill(size, eval, iteration):
    row = [size, eval, iteration]
    with open('hillplot.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(row)
def write_restart(size, restarts, eval, iteration):
    row = [size, restarts, eval, iteration]
    f = open('restart.csv', 'w')
    for item in row:
        f.write(str(item))
        f.write(',')
    f.write('\n')
def write_walk(size, eval, iteration):
    return 0
def write_anneal(size, eval, iteration, temp, decay):
    return 0
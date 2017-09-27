import csv

def write_hill(size, eval, iteration, time): 
    row = [size, eval, iteration, time]
    csvfile = 'hillplot.csv'
    with open (csvfile, 'a') as output:
        writer = csv.writer (output, delimiter = ',')
        writer.writerow(row)

def write_restart(size,  eval, iteration, time, restarts):
    row = [size,  eval, iteration, time, restarts]
    csvfile = 'restart.csv'
    with open(csvfile, 'a') as output:
        writer = csv.writer (output, delimiter = ',')
        writer.writerow(row)

def write_walk(size, eval, iteration, time, prob):
    row = [size, eval, iteration, time, prob]
    csvfile = 'walk.csv'
    with open (csvfile, 'a') as output:
        writer = csv.writer (output, delimiter = ',')
        writer.writerow(row)

def write_anneal(size, eval, iteration, time, temp, decay):
    row = [size, eval, iteration, time, temp, decay]
    csvfile = 'anneal.csv'
    with open (csvfile, 'a') as output:
        writer = csv.writer (output, delimiter = ',')
        writer.writerow(row)

#_4
import csv
def error_extarct() :
    with open ('maktab137.hw.log', 'r') as file:
        with open ('critical_error.csv' , 'w' ,) as critical_error:
            time = 'timeing'
            mess =' message'
            culumn = ((time),(mess))
            writer1 = csv.writer(critical_error)
            writer1.writerow(culumn)
            for line in file:
                try :
                    clean = line.split()
                    if clean[5] != 'error':
                        timeing = "".join(clean[0:5])
                        message = "".join(clean[6:])
                        with open ('critical_error.csv','a') as critical_error:
                            writer2 = csv.writer(critical_error)
                            writer2.writerow(timeing,message)
                except IndexError:
                    continue
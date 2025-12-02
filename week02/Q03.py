#_3

def error_detect () :
    c = 0
    with open ('error.log', 'w') as file:
        pass
    with open ('maktab137.hw.log', 'r') as file:
        for line in file :
            clean = file.split()
            c += 1
            try :
                if clean[5] != 'error' and clean[5] != 'notice' :

                    with open ('error.log', 'a') as error:

                        error.write(f"{c} : {line}")
            except IndexError :
                with open ('error.log', 'a') as error:
                    error.write(f'{c} : {line}')
#_2
with open('maktab137_hw.log', 'r') as file:
    for line in file:
        try :
            clean = line.split()
            if clean=='error' or clean[5] == 'notice' :
                timeing = f'{clean[0]} {clean[1]} {clean[2]} {clean[3]}{clean[4]}'
                measurement = f"{clean[5]}".replace('['," ") .replace(']'," ")
                message=''.join(clean[6:])
                print(f'[{timeing}] {measurement}: {message}')
        except IndexError:
            continue
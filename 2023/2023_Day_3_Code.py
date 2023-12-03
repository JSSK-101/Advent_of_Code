f = open("Day_3_Input.txt", "r")
data = f.readlines()

def part_1():
    def symbol():
        symbols = []
        f = open("Day_3_Input.txt", "r")
        data1 = f.read()
        data1 = data1.replace(".", "")
        data1 = data1.replace("\n", "")
        for k in range(len(data1)):
            if (data1[k] not in symbols) and (data1[k].isdigit() == False):
                symbols.append(data1[k])
        return symbols
    symbols = symbol()
    counter = 0

    for i in range(len(data)):
        j = 0
        while j < (len(data[i])):
            test = False
            l = 1
            number = ''
            if data[i][j].isdigit():
                number += str(data[i][j])
                if data[i][j+1].isdigit():
                    number += str(data[i][j+1])
                    if data[i][j+2].isdigit():
                        number += str(data[i][j+2])
                        l = 3
                    else:
                        l = 2
            j += l
            if number != '':
                if (j-l)!=0:
                    if data[i][j-l-1] in symbols:
                        test = True
                if data[i][j] in symbols:
                    test = True
                for m in range (l+2):
                    if i!=0:
                        if data[i-1][j-m] in symbols:
                            test = True
                    if i+1 < len(data):
                        if data[i+1][j-m] in symbols:
                            test = True
                if test == True:
                    counter += int(number)
    return counter

def part_2():
    symbols = '*'
    coords = []
    gears = []
    
    for i in range(len(data)):
        j = 0
        while j < (len(data[i])):
            test = False
            l = 1
            number = ''
            if data[i][j].isdigit():
                number += str(data[i][j])
                if data[i][j+1].isdigit():
                    number += str(data[i][j+1])
                    if data[i][j+2].isdigit():
                        number += str(data[i][j+2])
                        l = 3
                    else:
                        l = 2
            j += l
            if number != '':
                if (j-l)!=0:
                    if data[i][j-l-1] in symbols:
                        coords.append([i, j-l-1])
                        gears.append(number)
                if data[i][j] in symbols:
                    coords.append([i, j])
                    gears.append(number)
                for m in range (l+2):
                    if i!=0:
                        if data[i-1][j-m] in symbols:
                            coords.append([i-1, j-m])
                            gears.append(number)
                    if i+1 < len(data):
                        if data[i+1][j-m] in symbols:
                            coords.append([i+1, j-m])
                            gears.append(number)
                            
    count = 0
    while len(coords)>1:
        x = coords[0]
        y = gears[0]
        del coords[0]
        del gears[0]
        if x in coords:
            z = coords.index(x)
            count += int(gears[z])*int(y)
            del gears[z]
            del coords[z]
    return count

print(part_1, part_2())

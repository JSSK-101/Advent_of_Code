f = open("Day_2_Input.txt", "r")
data = f.readlines()

def part_1():
    count = 0
    j = 1
    for line in data:
        game = line.split(": ")
        bag = game[1].split("; ")
        x = True
        for i in range(len(bag)):
            r = 0
            b = 0
            g = 0
            cubes = bag[i].split(", ")
            for k in range(len(cubes)):
                cubes[k] = cubes[k].split(" ")
                if cubes[k][1] == "red":
                    r += int(cubes[k][0])
                elif cubes[k][1] == "green":
                    g += int(cubes[k][0])
                elif cubes[k][1] == "blue":
                    b += int(cubes[k][0])
            if r > 12 or g > 13 or b > 14:
                x = False
        if x == True:
            count += j
        j += 1
    return count

def part_2():
    count = 0
    for line in data:
        game = line.split(": ")
        bag = game[1].split("; ")
        rmin = 0
        bmin = 0
        gmin = 0
        for i in range(len(bag)):
            r = 0
            b = 0
            g = 0
            cubes = bag[i].split(", ")
            for k in range(len(cubes)):
                cubes[k] = cubes[k].split(" ")
                if "red" in cubes[k][1]:
                    r += int(cubes[k][0])
                elif "green" in cubes[k][1]:
                    g += int(cubes[k][0])
                elif "blue" in cubes[k][1]:
                    b += int(cubes[k][0])
            if r > rmin:
                rmin = r
            if g > gmin:
                gmin = g
            if b > bmin:
                bmin = b
        count += (rmin*gmin*bmin)
    return count
                        
print(part_1(), part_2())

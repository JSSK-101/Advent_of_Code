f = open("Day_1_Input.txt", "r")
data = f.readlines()

def part_1():
    count = 0
    for line in data:
        n = []
        for i in range(len(line)):
            if line[i].isdigit():
               n.append(line[i])
        count += (10*int(n[0])) + int(n[-1])
    return count

def part_2():
    j = 0
    number = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    replacements = ["o1e", "t2o", "t3e", "4", "5e", "6", "7n", "e8t", "9e"]
    for line in data:
        for i in range(len(number)):
            if number[i] in data[j]:
                data[j] = data[j].replace(number[i], replacements[i])
        j += 1
    return part_1()

print(part_1(), part_2())

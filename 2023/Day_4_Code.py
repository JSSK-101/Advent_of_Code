import re as r

f = open("Day_4_Input.txt", "r")
data = f.readlines()

def part_1():
    count = 0
    for line in data:
        times = 0
        x = r.split(": | \| |\n", line)
        y = x[1].split(" ")
        z = x[2].split(" ")
        while True:
            if "" in y:
                j = y.index("")
                del y[j]
            else:
                break
        for i in range(len(y)):
            if y[i] in z:
                times+= 1
        if times>0:
            count += 2**(times-1)
    return count
            
def part_2():
    scratchcards = []
    for i in range(len(data)):
        scratchcards.append(1)
    k = 0
    for line in data:
        times = 0
        x = r.split(": | \| |\n", line)
        y = x[1].split(" ")
        z = x[2].split(" ")
        while True:
            if "" in y:
                j = y.index("")
                del y[j]
            else:
                break
        for i in range(len(y)):
            if y[i] in z:
                times+= 1       
        for j in range(scratchcards[k]):
            for i in range(times):
                scratchcards[k+i+1] += 1     
        k+= 1    
    count = 0
    for i in range(len(scratchcards)):
        count += scratchcards[i]   
    return count
        
print(part_1(), part_2())

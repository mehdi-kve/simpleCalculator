data = []
sum = 0
def mulPriority():
    j = 0
    for i in data:
        if i == "*" or i == "/":
            if i == "*":
                tmp = data[j-1] * data[j+1]
            if i == "/":
                tmp = data[j-1] / data[j+1]
            data[j+1] = tmp
            data.pop(j)
            data.pop(j-1)
            mulPriority()
        elif i == "=":
            break
        j += 1
    
while True:
    number = int(input('Enter number : '))
    op = input('Enter Operation(+, -, *, /, =): ')
    data.append(number)
    data.append(op)
    if op == "=":
        mulPriority()
        l = 0
        sum = data[0]
        for k in data:
            if k == "+":
                sum += data[l + 1]
            if k == "-":
                sum -= data[l + 1]
            l += 1 
        break
print(sum)



    



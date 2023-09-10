comp = 0

def minmax(seq):
    mi = seq[0]
    ma = seq[0]
    global comp

    for i in range(1, len(seq)):
        comp += 1
        if seq[i] < mi:
            mi = seq[i]
        comp += 1
        if seq[i] > ma:
            ma = seq[i]

    return 'Minimum: ' + str(mi), 'Maximum: ' + str(ma)

a = eval(input("Enter an array: "))
result = minmax(a)
print(result)
print("Comparisons:", comp)

def odd(sequence):
    comp = 0
    flag = True
    pairs = []

    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            k = sequence[i] * sequence[j]
            comp += 1

            if k % 2 != 0:
                pairs.append([sequence[i], sequence[j]])
                print("Pair Present")
                flag = False

        if not flag:
            break

    if len(pairs) == 0:
        print("No such pair")

    print(pairs)
    print("comparisons:", comp)

user_input = eval(input("Enter a sequence:"))
odd(user_input)

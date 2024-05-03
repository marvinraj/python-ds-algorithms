# a la russe multiplication

def main():
    # user inputs
    num_one = int(input("Input first number :"))
    num_two = int(input("Input second number : "))

    # variables & lists
    total = 0
    col_one = []
    col_two = []
    col_three = []
    
    # append 2 inputs into first 2 list/column
    col_one.append(num_one)
    col_two.append(num_two)

    # algorithm that uses the user input
    while num_one > 1:
        # num one
        num_one = num_one//2
        col_one.append(num_one)
        # num two
        num_two = num_two*2
        col_two.append(num_two)

    for i in col_one:
        if i % 2 != 0:
            index_col_one = col_one.index(i)
            col_three.append(col_two[index_col_one])
            print(col_three)
    for j in col_three:
        total += j
    
    print(total)


if __name__ == "__main__":
    main()
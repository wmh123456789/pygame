
def find_adder(sum, num, min=1):
    rst = []
    if num == 1:
        if sum >= min:
            return [[sum]]
    elif num > 1:
        for i in range(min, sum):
            rst += [[i] + sub_rst for sub_rst in find_adder(sum - i, num - 1, i) if sub_rst]

    return rst



def main():
    sum = 20
    num = 3
    rst = find_adder(sum, num)
    print(f"For {num} adders get {sum}, found {len(rst)} ways:\n {rst}")


    pass


if __name__ == '__main__':
    main()

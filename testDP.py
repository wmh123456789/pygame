



def find_adder(sum, num):
    rst = []
    if num == 1:
        return [[sum]]
    elif num > 1:
        for i in range(1,num):
            return [[i]+sub_rst for sub_rst in find_adder(sum-i, num-1)]

    pass






def main():


    pass


if __name__ == '__main__':
    main()

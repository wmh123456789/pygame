
class DPFindAdder:
    dp = {}
    call_cnt = 0

    def __init__(self):
        pass

    def find_adder(self,sum, num, min=1):
        self.call_cnt += 1
        rst = []
        if num == 1:
            if sum >= min:
                return [[sum]]
        elif num > 1:
            for i in range(min, sum):
                if (sum-i, num-1, i) in self.dp:
                    rst += [[i] + sub_rst for sub_rst in self.dp[(sum-i, num-1, i)]]
                else:
                    rst += [[i] + sub_rst for sub_rst in self.find_adder(sum - i, num - 1, i) if sub_rst]

        self.dp.update({(sum, num, min): rst})
        return rst



def main():
    adder_sum = 100
    adder_num = 10
    adder_min = 1
    dp = DPFindAdder()
    rst = dp.find_adder(adder_sum, adder_num, adder_min)
    print(f"For {adder_num} adders get {adder_sum}, found {len(rst)} ways")
    if len(rst)<100:
        print(rst)
    else:
        print(f"with {dp.call_cnt} calls")
    pass


if __name__ == '__main__':
    main()

import random
 
# 是否使用测试用例
debug_example = False
# type example: [[int, bool], [int, bool] ... ]
example =  [ [0, False], [1, True], [2, False], [3, False], [4, True], [5, True], [6, False], [7, True], [8, False], [9, True],[10, False], [11, True], [12, False], [13, False] ]
 
# 随机创建实例个数范围
rand_min = 50
rand_max = 100
 
class chip():
    def __init__(self, number,quality):
        self.number = number
        self.quality = quality
    
    def test_target(self, target):
        # type target : chip
        # rtype ： bool
        # 接收一个芯片实例形参 判断该芯片好坏 返回bool
        # 如果本实例是好芯片 不会说谎 直接报告目标芯片的quality
        # 如果本实例不是好芯片 报告就有不确定性 返回一个随机值
        if self.quality:
            return target.quality
        else:
            return random.choice((True,False))
 
def create_chips():
    # rtype : list[chip,chip,...]
    # 随机创建实例 随机好坏
    # 最后补正好芯片比坏芯片多条件
    # 随机选取1或2个坏芯片改成好的 使得好芯片比坏芯片多
    chips = []
    quality_count = 0
    badnums = []
    for x in range(random.randint(rand_min,rand_max)):
        if random.choice((True,False)):
            chips.append(chip(number = x, quality = True))
            quality_count += 1
        else:
            chips.append(chip(number = x, quality = False))
            badnums.append(x)
    while quality_count <= len(chips)/2:
        for _ in range(random.choice((1,2))):
            num = badnums.pop(random.randint(0,len(badnums)-1))
            chips[num].quality = True
            quality_count += 1
    return chips
 
def test(A,B):
    # type A: chip
    # type B: chip
    # rtype : bool
    return A.test_target(B) and B.test_target(A)
 
def create_test_chips():
    # rtype : list[chip, chip...]
    chips = []
    for i in example:
        chips.append(chip(number = i[0], quality = i[1]))
    return chips    
 
def main():
    # rtype : chip
    if debug_example:
        chips = create_test_chips()
    else:
        chips = create_chips()
    while len(chips) > 3:
        # 当总量为奇数时 对最后一个元素单独判断 
        # 循环遍历前面的元素 与最后一个元素测试 得到最后一片芯片的quality 
        if len(chips)%2 != 0:    
            count = 0
            for i in chips[:-1]:
                if i.test_target(chips[-1]):
                    count += 1
            if count >= len(chips)//2: # 此时已经发现最后一片是好芯片
                return chips[-1]
            else:
                chips.pop()
        else:   # 如果不是奇数 进入分组淘汰模式
            surplus = []
            for i in range(len(chips)//2):
                # 两两一组互相测试 都报告好芯片 就随机选一个进入下一轮
                if test( chips[i*2], chips[i*2+1] ):
                    surplus.append( chips[ i*2 + random.choice((0, 1))] )
            chips = surplus   
    
    if len(chips) <= 2:
        return chips[0]
    elif len(chips) == 3:
        if test(chips[0],chips[1]):
            return chips[0]
        else:
            return chips[2]
    else:
        print("Error!")
        return        
 
if __name__ == "__main__":
    target = main()
    print("target:\nnumber {}\nquality {}".format( target.number, target.quality))
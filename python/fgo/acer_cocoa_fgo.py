import my_mouse as m 
import time
from PIL import ImageGrab
import numpy
import os
import pickle
import win32gui
import web_image
import random
import threading
import ali

project_path = os.getcwd()

b = "bun"
s = "sayu"
user = s

debug = True
# 最多吃几个苹果结束
max_apple = 0
# 吃完关机？
shutdown_bool = 1



yellow_coord = (
    (0.934375, 0.29583333333333334, 0.9390625, 0.3138888888888889)     ,
    (0.93359375, 0.5722222222222222, 0.9375, 0.5875)             ,
   (0.4828125, 0.30694444444444446, 0.4875, 0.3125)              ,  # 白色区域
)
poker_coord = (
    (0.8546875, 0.7541666666666667, 0.91953125, 0.7777777777777778),
    (0.25546875, 0.058333333333333334, 0.2625, 0.06388888888888888)
)
poker_xy = [
    (296, 467),
    (493, 467),
    (682, 472),
    (877, 473),
    (1074, 485),
]
liang = (0.20234375, 0.8361111111111111, 0.221875, 0.8763888888888889) 
over_next = (0.8953125, 0.9388888888888889, 0.90078125, 0.9486111111111111)

class fgo():
    def __init__(self,user):
        self.user = user
        self.first = False
        self.conf = dict()
        self.conf['game_coord'] = (203, 111, 1163, 651)
        self.friend_count = 0
        self.apple = 0
        self._over_count = 0
        self.mouse_xy = {
            '1':{'x': 253, 'y':  545, 'timeout': 5, 's': '技能1' },
            '2':{'x': 322, 'y':  543, 'timeout': 5, 's':  '技能2'},
            '3':{'x': 393, 'y':  540, 'timeout': 5, 's':  '技能3'},
            '4':{'x': 491, 'y':  540, 'timeout': 5, 's':  '技能4'},
            '5':{'x': 562, 'y':  540, 'timeout': 5, 's':  '技能5'},
            '6':{'x': 632, 'y':  540, 'timeout': 5, 's':  '技能6'},
            '7':{'x': 732, 'y':  540, 'timeout': 5, 's':  '技能7'},
            '8':{'x': 807, 'y':  540, 'timeout': 5, 's':  '技能8'},
            '9':{'x': 870, 'y':  540, 'timeout': 5, 's':  '技能9'},
            # m.click(253, 545, d, s = '技能1')
            # m.click(322, 543, d, s = '技能2')
            # m.click(393, 540, d, s = '技能3')
            # m.click(491, 540, d, s = '技能4')
            # m.click(562, 543, d, s = '技能5')
            # m.click(632, 542, d, s = '技能6')
            # m.click(732, 544, d, s = '技能7')
            # m.click(807, 543, d, s = '技能8')
            # m.click(870, 544, d, s = '技能9')
            'y':{'x': 1099, 'y':  345, 'timeout':  2 , 's': '御主技能'},
            'y1':{'x': 884, 'y':  343, 'timeout':  3 , 's': '御主技能1' },
            'y2':{'x': 948, 'y':  343, 'timeout':  3 , 's': '御主技能2' },
            'y3':{'x': 1014,'y':  343, 'timeout':  3 , 's': '御主技能3' },
            # m.click(1099, 345, 2, s = '御主技能')
            # m.click(884, 342, 2, s = '御主技能1')
            # m.click(948, 346, 2, s = '御主技能2')
            # m.click(1014, 343, 2, s = '御主技能3') 

            'h1':{'x': 313, 'y':  375, 'timeout':  2 , 's': '换人第1位置'},
            'h2':{'x': 455, 'y':  375, 'timeout':  2 , 's': '换人第2位置'},
            'h3':{'x': 601, 'y':  375, 'timeout':  2 , 's': '换人第3位置'},
            'h4':{'x': 759, 'y':  375, 'timeout':  12 , 's': '换人第4位置'},
            'h5':{'x': 899, 'y':  375, 'timeout':  12 , 's': '换人第5位置'},
            'h6':{'x': 1055, 'y':  375, 'timeout':  12 , 's': '换人第6位置'},

            'sk1':{'x': 451, 'y':  445, 'timeout': 5  , 's': '点击第一个人' },
            'sk2':{'x': 687, 'y':  423, 'timeout': 5  , 's': '点击第二个人'},
            'sk3':{'x': 927, 'y':  456, 'timeout': 5  , 's': '点击第三个人'},
            # m.click(451, 445, d, '孔明技能1 点击第一个人')
            # m.click(687, 423, d, '孔明技能1 点击第二个人')
            # m.click(927, 456, d, '孔明技能1 点击第三个人')
            
            'b1':{'x': 505, 'y': 265 , 'timeout': 3 , 's': '宝具1' },
            'b2':{'x': 678, 'y': 265 , 'timeout': 3 , 's': '宝具2' },
            'b3':{'x': 840, 'y': 265 , 'timeout': 3 , 's': '宝具3' },
            # m.click(505, 272, 1, s = '宝具1')
            # m.click(678, 265, 2, s = '宝具2')
            # m.click(840, 265, 2, s = '宝具3')
            
            'a':{'x': 1047, 'y': 569 , 'timeout': 3  , 's': '攻击' },
            # m.click(1047, 569, 3, s = '攻击')                
        }
        self.friend_mouse_xy = {
            "one_":(675, 324),
            "two_":(687, 469),
        }
        self.concept_dict = self.get_histogram_dict()

    # ###### 检测上次用户
    # def _get_laastuser(self):
    #     return self.user

    ###### 出击
    def attack(self, order=None, concept= None):
        one, two, three = [x.strip() for x in order.split('|')]
        if one or two or three:
            print ('args order --> ', order)
        else:
            print ('func attack args order error!')
            print ('one --> ', one)
            print ('two --> ', two)
            print ('three --> ', three)
            return
        print (one)
        print (two)
        print (three)
    
        d = 5    # 默认等待鼠标时间
        m.click(853, 262, d, s = '点击第一个地图')   ##
        attack_count = 0
        liz_count = 0
        while True:
            attack_count += 1
            if self.game_friends():
                if attack_count == 1:
                    print ('不需要吃苹果')
                    if not concept:
                        break
                if type(concept) == str:
                    print ('sleep 2')
                    time.sleep(2)
                    # 如果需要做概念里装判定
                    # self.concept_dict 是本地已保存的标准直方图字典 每个key有4个元素  
                    #     (index, now_coord, im.histogram(), im)
                    #         0. index 枚举： ( "one_", "two_" )
                    #         1. coord 原始截图坐标
                    #         2. 直方图
                    #         3. 原始ImageGrab.grab()对象
                    # 判定本地的直方图 与 现抓的直方图 是否一致 不一致循环刷新好友    
                    aooone = "one_" + concept
                    atttwo = "two_" + concept
                    break_bool = False
                    for key in [aooone, atttwo]:   # 迭代做好的下标
                        if key not in self.concept_dict:
                            print ('self.concept_dict error! ')
                            # return 
                        else:
                            # or_tuple 是本地保存个体值 有4个元素的元祖
                            or_tuple = self.concept_dict[key]
                            index = or_tuple[0]
                            or_im = or_tuple[3]
                            new_im = ImageGrab.grab( or_tuple[1] )
                            print ("type new_im --> ", type(new_im))
                            if new_im.histogram() == or_im.histogram():
                                # 用保存的坐标截新图 对比新图和保存的图直方图 
                                # 一致就点击 sel下标index 不一样就循环刷新好友
                                m.click(self.friend_mouse_xy[index][0],self.friend_mouse_xy[index][1], 10, s="点击好友下标 "+index)
                                break_bool = True
                                break
                            else:
                                print ('not target object --> ', index)
                    # 如果只判断一次是否有礼装 代码到这里就缺一步点击第一个好友 因为下面 if 不会点
                    if not break_bool:
                        m.click(675, 315, 3, s='点击第一个好友')
                        break

                                # new_im.show()
                                # or_tuple[3].show()
                    # else:
                    #     # 如果不需要刷新 就直接break
                    #     break
                    liz_count += 1
                    if liz_count > 3:  # 刷新3次
                        liz_count = 0
                        concept = None
                        break
                    print('未发现符合对象 即将刷新好友')
                    m.click(280, 145, 5, '返回')
                    m.click(853, 262, 5, '点击第一个地图')
                    m.click(830, 210, 5, '刷新列表')
                    m.click(764, 550, 5, s = '刷新 确定')
                    if break_bool:
                        break
            else:
                # 需要吃苹果
                print ('ap不足')
                time.sleep(3)
                if attack_count > 50:
                    exit()
                # 如果已吃苹果 >= 最大苹果限制
                if self.apple >= max_apple:
                    try:
                        im = ImageGrab.grab()
                        im.save('temp.jpg')
                    except:
                        pass
                    if shutdown_bool:
                        print ("over! ")
                        self.log()
                        os.system('shutdown -s -t 20')
                    exit()
                self.apple += 1    
                if True:  # self.apple %2 == 0:
                    self.log()
                m.click(686, 350, 5, s = '点击金苹果')
                # m.click(723, 463, 5, s = '点击银苹果')
                # m.click(898, 536, 5, s = '点击铜苹果 ')
                m.click(764, 550, 5, s = '吃！')
                print ('第{}个苹果'.format(str(self.apple)))
                time.sleep(5)
                # m.click(853, 262, 5, s = '点击第一个地图')           

        if not concept:
            m.click(675, 315, 8, s='点击第一个好友')
        # m.click(594, 457, d, s = '点击第二个好友')
        m.click(1087, 615, 10, s = '开始任务')
        while True:
            _enemy_count = self.get_enemy_count()
            if _enemy_count:
                print ('发现{}名敌人'.format(str(_enemy_count)))
                time.sleep(5)
                break
            else:
                time.sleep(1)
        one, two, three = [x.strip() for x in order.split('|')]
        ####### 第一轮攻击
        if self.first:
            m.click(1096, 256, timeout = 5, s = "战斗菜单")
            def _temp():
                or_tuple = self.concept_dict["two_jineng"]
                index = or_tuple[0]
                or_im = or_tuple[3]
                new_im = ImageGrab.grab( or_tuple[1] )
                print ("type new_im --> ", type(new_im))
                if new_im.histogram() == or_im.histogram():
                    # 用保存的坐标截新图 对比新图和保存的图直方图 
                    # two_jineng 保存的是关闭时的直方图
                    # 不一致就返回False
                    return False
                else:
                    return True
            if _temp():
                m.click(969, 322, timeout = 5, s='取消技能提示')
            m.click(1027, 185,timeout=5, s = "关闭")

        for xy in one.split(' '):
            if xy == "one_monalisa":
                continue
            if debug:
                print ('one xy --> ', xy)
            if xy in self.mouse_xy:
                m.click(**self.mouse_xy[xy])

                if self.first:
                    time.sleep(2)
                    if xy == 'a':
                        pass
                        m.click( 1048, 173,timeout = 3,  s = "快进")
            else:
                print('one mouse error  xy --> ', xy)
                input('wait for input...')
        self.rand_k()
        time.sleep(25)

        #######  判断第二轮攻击
        while True:
            # 进入可选择攻击卡片状态后 
            # 判断血条区有多少个血条
            temp_enemy_count = self.get_enemy_count()
            if type(temp_enemy_count) == int:
                if temp_enemy_count < _enemy_count:
                    print ('未发现第二轮攻击 进入补刀状态')
                    m.click(1047, 569, 3, s = '攻击')
                    print ('随机选取3张普通卡')
                    self.rand_k()
                    time.sleep(10)
                if temp_enemy_count == 3:
                    _enemy_count = temp_enemy_count
                    print ('发现{}名敌人'.format(str(_enemy_count)))
                    time.sleep(3)
                    break
            else:
                time.sleep(1)

        for xy in two.split(' '):
            if xy == "one_monalisa":
                continue
            if debug:
                print ('two xy --> ', xy)
            if xy in self.mouse_xy:
                m.click(**self.mouse_xy[xy])
            else:
                print('two mouse error  xy --> ', xy)
                input('wait for input...')
        self.rand_k()
        time.sleep(25)

        ####### 判断第三轮攻击
        while True:
            temp_enemy_count = self.get_enemy_count()
            if type(temp_enemy_count) == int:
                if temp_enemy_count >= 2:
                    _enemy_count = temp_enemy_count
                    print ('发现{}名敌人'.format(str(_enemy_count)))
                    time.sleep(3)
                    break
                if temp_enemy_count < _enemy_count:
                    print ('未发现第三轮攻击 进入补刀状态')
                    m.click(1047, 569, 3, s = '攻击')
                    print ('随机选取3张普通卡')
                    self.rand_k()
                    time.sleep(10)
                
            else:
                time.sleep(1)

        for xy in three.split(' '):
            if xy == "one_monalisa":
                continue
            if debug:
                print ('three xy --> ', xy)
            if xy in self.mouse_xy:
                m.click(**self.mouse_xy[xy])
            else:
                print('three mouse error  xy --> ', xy)
                input('wait for input...')
        self.rand_k()
        time.sleep(25)

        while True: # 未检测完成就补刀
            temp_enemy_count = self.get_enemy_count()
            if type(temp_enemy_count) == int:
                if temp_enemy_count <= 3:
                    print (' 进入补刀状态')
                    m.click(1047, 569, 5, s = '攻击')
                    m.click(505, 272, 1, s = '宝具1')
                    m.click(678, 265, 1, s = '宝具2')
                    m.click(840, 265, 1, s = '宝具3')
                    print ('随机选取3张普通卡')
                    self.rand_k()
                    time.sleep(10)

            if self.over():
                break
            else:
                m.click(285, 271, 3, 'void')
        self._over_count += 1
        print("已出击{}次".format(str(self._over_count)))
        if self._over_count %5 == 0:
            self.log()
        m.click(1020, 622, 8, '下一步')
        if self.first:
            time.sleep(20)
            self.log()
            m.click(1020, 622, 8, '下一步')
            self.first = False

    ###### 截取coord尺寸并存储
    def coord_save(self,now_coord ,target_path, index = None):
        # now_coord   : 截图的坐标  
        # target_path : 保存直方图的路径 文件名.pkl 
        im = ImageGrab.grab(now_coord)
        save_im_object = (index, now_coord, im.histogram(), im)
        with open(os.path.join("my_images",index + target_path), 'wb') as f:
            pickle.dump(save_im_object, f)
        im.save( os.path.join("my_images/",time.strftime("%m-%d %H_%M ", time.localtime()) + index +  target_path[:-3] + 'jpg'))
        print ('ok')
        im.show()

    ###### 获取直方图
    def get_histogram_dict(self):
        files_path = os.listdir(os.path.join(os.getcwd(), 'my_images'))
        data = {}
        for file in files_path:
            if file[-3:] == "pkl":
                print ('get file pkl --> ', file)
                pkl_data = None
                pkl_path = os.path.join(os.getcwd(), 'my_images', file)
                print ('pkl_path --> ', pkl_path)
                with open( pkl_path , 'rb') as f:
                    pkl_data = pickle.load(f)
                pkl_key = file[:-4]
                data.update({
                    pkl_key:pkl_data
                })
        
        return data

    ###### 检测主界面
    def home(self, print_bool = True):
        # 下面几个列表 第一个是坐标 第二个是rgb值
        # 判断坐标色块等于rgb值则视为回到主页 
        data = [
        #    [(248, 138, 257, 147), (211, 212, 212)],  # 左上 
      #      [(1043, 618, 1056, 627), (218, 218, 219)],# 菜单  
        #    [(513, 610, 515, 617), (251, 202, 136)], # 礼物
        #    [(523, 617, 529, 627), (223, 58, 33)],   # 礼物
            [(533, 617, 539, 623), (158, 2, 2)],     # 礼物
        ]
        im = ImageGrab.grab()
        rgb_count = 0
        for i in data:
            rgb = web_image.get_dominant_color(im.crop(i[0]))
            if i[1] == rgb or rgb == (5,7,38) or rgb == (210, 210, 211) or rgb == (137, 13, 1) or rgb == (213, 210, 212):
                rgb_count += 1
            else:
                if debug:
                    print ('home rgb error ',i, rgb )
        if rgb_count >= len(data):
            if print_bool:
                print('检测到主页面')
            time.sleep(3)
            return True
        
    # ###### 分解
    # def remove_food(self, count = 1):
    #     m.click(1091, 622, 3, '菜单')
    #     m.click(738, 604, 5, '商店')
    #     m.click(914, 352, 3, "贩卖")
    #     self.log()
    #     move_coord_list = [
    #         (299, 309),
    #         (433, 306),
    #         (581, 309),
    #         (722, 306),
    #         (854, 311),
    #         (301, 453),
    #         (451, 454),
    #         (585, 451),
    #         (712, 459),
    #         (859, 458),
    #         (854, 606),
    #         (709, 601),
    #         (569, 600),
    #         (440, 597),
    #         (303, 589),
    #     ]
    #     while count > 0:
    #         count -= 1
    #         for i in move_coord_list:
    #             m.click(i[0], i[1], 0.5, '狗粮')
    #         time.sleep(1)
    #         m.click(1071, 618, 3, '决定')
    #         m.click(828, 548, 8, '销毁')
    #         m.click(687, 553, 3, '关闭')

    #     m.click(283, 152, 3, '关闭')
    #     m.click(283, 152, 10, '关闭')

    # 配置参数
    def game_conf(self):
        try:
            with open("fgo.pkl", 'rb') as f:
                conf = pickle.load(f)
        except FileNotFoundError as e:
            subwin = int(input('未检测到游戏配置 请输入窗口句柄: '))
            conf = dict()
            conf['game_coord'] = win32gui.GetWindowRect(subwin)
            conf['game_x'] = conf['game_coord'][2] - conf['game_coord'][0] 
            conf['game_y'] = conf['game_coord'][3] - conf['game_coord'][1]

        def _percent_coord(x,y):
            pass
        
    # 判断是否进入选择好友界面
    def game_friends(self):
        if self.friend_count > 20:
            m.click(282, 146, 5, '回家')
            m.click(911, 252, 5, s = '点击第一个地图')
            self.friend_count -= 10
        im = ImageGrab.grab(self.conf['game_coord'])
        rgb = []
        for i in yellow_coord:
            rgb.append(web_image.get_dominant_color(im.crop(self.coord(i))))
        try:
            if rgb[0] == rgb[1] == (229, 179, 31):
                print ('yellow 0 True')
                if rgb[2] == 0:
                    print ('yellow 1 True')
                    self.friend_count = 0
                    return True
                else:
                    print ('yellow 1 False')
                    print (rgb[2])
                    self.friend_count += 1
            else:
                print ('yellow 0 False')
                self.friend_count += 1
        except:
            pass    

    # 判断进入选择卡片状态 并返回敌人数量
    def get_enemy_count(self):
        im = ImageGrab.grab(self.conf['game_coord'])
        rgb = web_image.get_dominant_color(im.crop(self.coord(poker_coord[0])))
        # print ('poker battle_rgb --> ', rgb)
        if rgb == (2, 233, 249):
            print ('battle_rgb True')
            rgb = web_image.get_dominant_color(im.crop(self.coord(poker_coord[1])))
            # print ('poker blood_rgb', rgb)
        #    if rgb == (188, 0, 35):
            # 到这步是已可以选择卡片状态
            im = ImageGrab.grab()
            rgb_lsit = list()         # 临时存放rgb变量
            rgb_satisfy_count = 0     # 满足条件的rgb数量
            blood_shadow = [            
                (266, 150, 273, 152),   # 3个血条阴影区的坐标
                (445, 150, 454, 152),   # 判断血条rgb是否符合条件
                (626, 150, 633, 152),   # 返回 血条的数量
            ]
            for coord_index in range(len(blood_shadow)):
                temp_blood_rgb = web_image.get_dominant_color(im.crop(blood_shadow[coord_index]))
                if debug:
                    print ('第{}个血条rgb --> {}'.format(str(coord_index+1), str(temp_blood_rgb)))
                if temp_blood_rgb == (81, 64, 47) or temp_blood_rgb == (54,22,0) or temp_blood_rgb == (80, 60, 44) or temp_blood_rgb == (74,66,57):
                    rgb_satisfy_count += 1
            if rgb_satisfy_count > 0 and rgb_satisfy_count < 4:
                return rgb_satisfy_count
            # else:
            #     if debug:
            #         print ('blood_rgb False')
        else:
            if debug:
                print ('battle_rgb False')

    # 随机选取3张卡
    def rand_k(self):
        for i in random.sample(poker_xy, 3):
            m.click( i[0], i[1], 0.5, s = '' )

    # 判断战斗结束
    def over(self):
        im = ImageGrab.grab(self.conf['game_coord'])
        rgb = web_image.get_dominant_color(im.crop(self.coord(liang)))
        # if rgb == (203, 187, 41):
        if rgb == (35, 29, 0) or rgb == (4,18,38) or rgb == (4,18,37) or rgb == (7, 18, 38) or rgb == (10,10,21) or rgb == (8, 19, 39) or rgb == (10,10,20) or rgb ==(9, 9, 20) or rgb ==(9, 9, 19) or rgb == (6 ,16, 35) or rgb == (4, 16, 37):
            print ('liang True')
            rgb = web_image.get_dominant_color(im.crop(self.coord( over_next )))
            if rgb == (179, 213, 225)  or rgb == (36,45,81) or rgb == (9, 9, 20) or rgb == (13, 15, 35):
                print ('战斗结束')
                return True
            else:
                print ('next rgb --> ', rgb)
                print ('next False')
                
        else:
            print ('liang False')
            print ('liang rgb --> ', rgb)
            
    # 根据百分比找出目标坐标
    def coord(self, coord_percent):
        x = self.conf['game_coord'][2] - self.conf['game_coord'][0] 
        y = self.conf['game_coord'][3] - self.conf['game_coord'][1]       
        coord_t = (
            int(coord_percent[0] * x),
            int(coord_percent[1] * y),
            int(coord_percent[2] * x),
            int(coord_percent[3] * y)
        )        
        # print ('coord_t --> ', coord_t)
        return coord_t

    # 截图记录
    def log(self, up_ali= False):
        print('log start ')
        now = time.strftime('%m-%d_%H_%M', time.localtime())
        im = ImageGrab.grab()
        im_path = os.path.join('log_image', now + '.jpg')
        im.save(im_path)
        # if up_ali:
        #     # send(img_path = im_path)       
        #     t = threading.Thread(target=ali.send, args=(im_path, ))
        #     t.start()

if __name__ == '__main__':
    user = 'cocoa'
    order = " a | 4 5 a | 1 2 sk3 7 8 9 a "
 
    f = fgo(user) 
    c = 0
    while True:
        now_hour = int(time.strftime('%H', time.localtime()))
        if f.home():
            c += 1
            f.log()
            f.attack(order= order, concept = "cba")

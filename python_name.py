# -*- coding: utf-8 -*-
# @date    : 2020-12-22
# @author  : WGC

import datetime
import random

def CleanFile(FileURL):
    # 定义 每次打开文件清空旧文件内容
    with open(FileURL, 'r+', encoding='UTF-8') as file:
        file.truncate(0)

def WriteFile(FileURL,File):
    # 定义 写入数据
    file = open(FileURL, mode='a+', encoding='UTF-8')
    file.write(str(File) + '\n')
    file.close()

def Result():
    # 定义 通过.bat调用Python脚本执行成功时，在控制台显示信息
    return print('Result：' +  'The Python script executed successfully')

def FirstName():
    # 定义 随机生成6千多汉字
    OneByte = random.randint(0xb0, 0xf7)
    TwoByte = random.randint(0xa1, 0xf9)
    FirstName = bytes.fromhex(f'{OneByte:x} {TwoByte:x}').decode('gb2312')
    return FirstName

def LastName():
    # 定义 生成百家姓 共计504个
    LastNameOne = ['赵','钱','孙','李','周','吴','郑','王','冯','陈','褚','卫','蒋','沈','韩','杨','朱','秦','尤','许','何','吕',
                   '施','张','孔','曹','严','华','金','魏','陶','姜','戚','谢','邹','喻','柏','水','窦','章','云','苏','潘','葛',
                   '奚','范','彭','郎','鲁','韦','昌','马','苗','凤','花','方','俞','任','袁','柳','酆','鲍','史','唐','费','廉',
                   '岑','薛','雷','贺','倪','汤','滕','殷','罗','毕','郝','邬','安','常','乐','于','时','傅','皮','卞','齐','康',
                   '伍','余','元','卜','顾','孟','平','黄','和','穆','萧','尹','姚','邵','湛','汪','祁','毛','禹','狄','米','贝',
                   '明','臧','计','伏','成','戴','谈','宋','茅','庞','熊','纪','舒','屈','项','祝','董','梁','杜','阮','蓝','闵',
                   '席','季','麻','强','贾','路','娄','危','江','童','颜','郭','梅','盛','林','刁','钟','徐','邱','骆','高','夏',
                   '蔡','田','樊','胡','凌','霍','虞','万','支','柯','昝','管','卢','莫','经','房','裘','缪','干','解','应','宗',
                   '丁','宣','贲','邓','郁','单','杭','洪','包','诸','左','石','崔','吉','钮','龚','程','嵇','邢','滑','裴','陆',
                   '荣','翁','荀','羊','於','惠','甄','麴','家','封','芮','羿','储','靳','汲','邴','糜','松','井','段','富','巫',
                   '乌','焦','巴','弓','牧','隗','山','谷','车','侯','宓','蓬','全','郗','班','仰','秋','仲','伊','宫','宁','仇',
                   '栾','暴','甘','钭','厉','戎','祖','武','符','刘','景','詹','束','龙','叶','幸','司','韶','郜','黎','蓟','薄',
                   '印','宿','白','怀','蒲','邰','从','鄂','索','咸','籍','赖','卓','蔺','屠','蒙','池','乔','阴','欎','胥','能',
                   '苍','双','闻','莘','党','翟','谭','贡','劳','逄','姬','申','扶','堵','冉','宰','郦','雍','舄','璩','桑','桂',
                   '濮','牛','寿','通','边','扈','燕','冀','郏','浦','尚','农','温','别','庄','晏','柴','瞿','阎','充','慕','连',
                   '茹','习','宦','艾','鱼','容','向','古','易','慎','戈','廖','庾','终','暨','居','衡','步','都','耿','满','弘',
                   '匡','国','文','寇','广','禄','阙','东','殴','殳','沃','利','蔚','越','夔','隆','师','巩','厍','聂','晁','勾',
                   '敖','融','冷','訾','辛','阚','那','简','饶','空','曾','毋','沙','乜','养','鞠','须','丰','巢','关','蒯','相',
                   '查','後','荆','红','游','竺','权','逯','盖','益','桓','公','仉','督','晋','楚','闫','法','汝','鄢','涂','钦',
                   '归','海','岳','帅','缑','亢','况','后','有','琴','商','牟','佘','佴','伯','赏','墨','哈','谯','笪','年','爱',
                   '阳','佟','言','福',]
    LastNameTwo = ['万俟','司马','上官','欧阳','夏侯','诸葛','闻人','东方','赫连','皇甫','尉迟','公羊','澹台','公冶','宗政','濮阳','淳于',
                   '单于','太叔','申屠','公孙','仲孙','轩辕','令狐','钟离','宇文','长孙','慕容','鲜于','闾丘','司徒','司空','亓官','司寇',
                   '子车','颛孙','端木','巫马','公西','漆雕','乐正','壤驷','公良','拓跋','夹谷','宰父','谷梁','段干','百里','东郭','南门',
                   '呼延','羊舌','微生','梁丘','左丘','东门','西门','南宫','第五']
    i = random.randint(1, 100)
    if i <= 20:
        # 取20%的复姓
        LastName = LastNameTwo[random.randint(0, len(LastNameTwo) - 1)]
    else:
        LastName = LastNameOne[random.randint(0, len(LastNameOne) - 1)]
    return LastName

def ChineseName():
    # 定义 生成中文名
    i = random.randint(1, 100)
    if i <= 50:
        # 生成50%的1个字的名字 样本数：504 * 6000 = 3024000
        ChineseName = LastName() + FirstName()
    else:
        # 生成50%的2个字的名字 样本数：504 * 6000 * 6000 = 18144000000
        ChineseName = LastName() + FirstName() + FirstName()
    # 总样本数 18147024000
    return ChineseName

def WriteChineseName(FileURL,data):
    z = ''
    i = 0
    # 定义 循环生成多少数据
    while i < data:
        z = (
            ChineseName()
        )
        WriteFile(FileURL, z)
        i = i + 1

def WriteFirstName(FileURL,data):
    z = ''
    i = 0

    # 定义 循环生成多少数据
    while i < data:
        j = random.randint(1, 100)
        if j <= 50:
            z = (
                FirstName()
            )
        else:
            z = (
                FirstName() + FirstName()
            )
        WriteFile(FileURL, z)
        i = i + 1

def WriteLastName(FileURL,data):
    z = ''
    i = 0
    # 定义 循环生成多少数据
    while i < data:
        z = (
            LastName()
        )
        WriteFile(FileURL, z)
        i = i + 1


if __name__ == '__main__':

    data = 100000
    ChineseNameFileURL = 'D:\\dir\\filename.csv'
    CleanFile(ChineseNameFileURL)
    WriteChineseName(ChineseNameFileURL, data)

    FirstNameFileURL = 'D:\\dir\\csv_firstname.csv'
    CleanFile(FirstNameFileURL)
    WriteFirstName(FirstNameFileURL, data)

    LastNameFileURL = 'D:\\dir\\csv_lastname.csv'
    CleanFile(LastNameFileURL)
    WriteLastName(LastNameFileURL, data)

    Result()


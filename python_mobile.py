# -*- coding: utf-8 -*-
# @date    : 2022-01-06
# @author  : wangguangchen

import random

mobile_yd = [
    # 移动号码段，更新至198号段，不包含物联网、卫星电话、虚拟号段。
    159, 178, 182, 183, 184, 187, 188, 198, 134, 135, 136, 137, 138, 139, 147, 148, 150, 151, 152, 157, 158
]
mobile_lt = [
    # 联通号码段，更新至186号段，不包含物联网、卫星电话、虚拟号段。
    185, 130, 131, 132, 145, 146, 155, 156, 166, 175, 176
]
mobile_dx = [
    # 电信号码段，更新至199号段，不包含物联网、卫星电话、虚拟号段。
    133, 149, 153, 173, 177, 180, 181, 189, 191, 199
]


# # 批量生成订单流水号用
# mobile_yd = [987, 876, 765, 654, 543, 432, 321, 123, 234, 345, 456, 567, 678, 789]
# mobile_lt = [147, 741, 258, 852, 369, 963]
# mobile_dx = [753, 357, 159, 951]


def Mobile_Three():
    # 手机号前3位
    i = random.randint(1, 100)
    if i <= 40:
        # 生成40%的移动号码
        three = mobile_yd[random.randint(0, len(mobile_yd) - 1)]
    elif 40 < i <= 70:
        # 生成30%的联通号码
        three = mobile_lt[random.randint(0, len(mobile_lt) - 1)]
    else:
        # 生成30%的电信号码
        three = mobile_dx[random.randint(0, len(mobile_dx) - 1)]
    return three

def Mobile_Eight():
    # 手机号后8位
    eight = random.randint(10000000, 99999999)
    return eight

def Mobile():
    # 生成11位手机号
    mobile = str(Mobile_Three()) + str(Mobile_Eight())
    return mobile

def CleanFile(FileURL):
    # 每次打开文件清空旧文件内容
    with open(FileURL, 'r+', encoding='UTF-8') as file:
        file.truncate(0)

def WriteFile(FileURL,File):
    # 写入数据，每写一次就换行一次。
    file = open(FileURL, mode='a+', encoding='UTF-8')
    file.write(str(File) + '\n')
    file.close()

def Result():
    # 调用Python脚本执行成功时，在控制台显示信息。
    return print('Result：' + 'The Python script executed successfully')

def WriteMobile(FileURL,data):
    i = 0
    # 定义 循环生成多少数据
    while i < data:
        mobile = [
            Mobile()
        ]
        # 去掉重复的手机号
        mobile_old = set(mobile)
        mobile_new = list(mobile_old)
        # 开始循环写入csv文件
        j = 0
        while j < len(mobile_new):
            z = (
                mobile_new[j]
            )
            WriteFile(FileURL, z)
            j = i + 1
        i = i + 1


if __name__ == '__main__':

    data = 25000
#   区分文件
    FileURL = 'D:\\jmeter\\csv_mobile.csv'
#    FileURL = 'D:\\jmeter\\csv_sequenceNumber.csv'

    MobileFileURL = FileURL
    CleanFile(MobileFileURL)
    WriteMobile(MobileFileURL, data)

    Result()
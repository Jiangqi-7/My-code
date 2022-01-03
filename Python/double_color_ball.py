#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Author:Crow
import random

single_list = []
result_list = []
def get_redNum() :
    num = random.randint(1, 33)
    re_num = str(num).zfill(2)
    return re_num
def get_redBall() :
    single_list = []
    while True :
        re_num = get_redNum()
        if re_num  in single_list :
            continue
        else :
            single_list.append(re_num)
        if len(single_list) == 6 :
            break
    single_list.sort()
    return single_list
def get_buleBall() :
    num = random.randint(1, 16)
    re_num = str(num).zfill(2)
    return re_num
def begin(total) :
    for i in range(int(total)) :
        while True :
            single_list = get_redBall()
            single_list.append(get_buleBall())
            if single_list in result_list :
                continue
            else :
                result_list.append(single_list)
                break

    for i in result_list:
        print('第' + str(result_list.index(i) + 1) + '注：', end='')
        for j in i:
            print(j, end=' ')
        print()
def again(total) :
    list_temp = []
    for i in range(int(total)) :
        print('%d：第%d注重打' % (i+1,i+1))
        list_temp.append(str(i+1))
    while True :
        choice = input('请选择：')
        if choice not in list_temp :
            print('您的输入有误，请重新输入。')
            continue
        else :
            return choice
        break
if __name__ == '__main__' :
    while True :
        total = input('请输入需要的注数（1——5）：')
        if total not in ('1','2','3','4','5') :
            print('您的输入有误，请重新输入。')
            continue
        begin(total)
        while True :
            choice = input('''
            0 : 确认
            1 ： 单注重打
            2 ：全部重打
            请输入：''')
            if choice not in ('0','1','2') :
                print('您的输入有误，请重新输入。')
                continue
            elif choice == '0' :
                break
            elif choice == '1' :
                choice = again(total)
                single_list = []
                single_list = get_redBall()
                single_list.append(get_buleBall())
                result_list[int(choice)-1] = single_list
                for i in result_list:
                    print('第' + str(result_list.index(i) + 1) + '注：', end='')
                    for j in i:
                        print(j, end=' ')
                    print()
                continue
            elif choice == '2' :
                result_list = []
                begin(total)
                continue
        is_continue = input('是否继续？输入y继续，其他任意键退出：')
        if is_continue == 'y' :
            result_list = []
            continue
        else :
            break

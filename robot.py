# -- coding: utf-8 --
from termcolor import colored

import csv_wr
import string


"""
csvを作成し、まずcsvの中身を辞書化(load_csv)する。
追加する場合にload_csvと照らし合わせて値を追加する。

"""


class Robot:
    def __init__(self):
        self.name = ''
        self.restaurant = ''
        self.robot_name = 'roboko'

    def robot_hallo(self):
        with open('text/hallo.txt', encoding='UTF-8') as f:
            print(colored("*"*60, 'green'))
            for row in f.readlines():
                print(colored(string.Template(row).substitute(robot_name=self.robot_name)
                              .rstrip(), 'red'))
            print(colored("*"*60, 'green'))
            self.name = input()
        return self.name

    def robot_greeting(self):
        self.restaurant_list = []
        try:
            restaurant_dict = csv_wr.csv_read()
            list_k = [k for k, v in sorted(restaurant_dict.items(), key=lambda x: -x[1])]
            self.restaurant = list_k[0]
            print(colored("*" * 60, 'green'))
            with open('text/greeting.txt', encoding='UTF-8') as cf:
                for row in cf.readlines():
                    print(colored(string.Template(row).substitute(restaurant=self.restaurant)
                                  .rstrip(), 'green'))
            print(colored("*" * 60, 'green'))
            ans = input('')
            if ans == 'yes':
                restaurant_dict[self.restaurant] += 1
                for name, count in restaurant_dict.items():
                    restaurant_dict2 = {'Name': name, 'Count': count}
                    self.restaurant_list.append(restaurant_dict2)
                csv_wr.csv_write(self.restaurant_list)

            else:
                pass
        except:
            pass

    def robot_which(self):
        with open('text/which_restaurant.txt', encoding='UTF-8') as af:
            for row in af.readlines():
                print(colored('*'*60 + '\n' + string.Template(row).substitute(name=self.name)
                              + '\n' + '*'*60, 'green'), sep='')
        self.restaurant = input('').title()
        return self.restaurant

    def restaurant_write(self):
        self.restaurant_list = []
        try:
            restaurant_dict = csv_wr.csv_read()
            if self.restaurant in restaurant_dict:
                restaurant_dict[self.restaurant] += 1
            else:
                restaurant_dict[self.restaurant] = 1
            for name, count in restaurant_dict.items():
                restaurant_dict_insert = {'Name': name, 'Count': count}
                self.restaurant_list.append(restaurant_dict_insert)
            csv_wr.csv_write(self.restaurant_list)

        except:
            restaurant_dict_no = {}
            restaurant_dict_no[self.restaurant] = 1
            for name, count in restaurant_dict_no.items():
                restaurant_dict_insert = {'Name': name, 'Count': count}
                self.restaurant_list.append(restaurant_dict_insert)
            csv_wr.csv_write(self.restaurant_list)

    def robot_good_by(self):
        print(colored("*" * 60, 'green'))
        with open('text/sayonara.txt', encoding='UTF-8') as bf:
            for row in bf.readlines():
                print(colored(string.Template(row).substitute(name=self.name).rstrip(), 'green'))

        print(colored("*" * 60, 'green'))


def main():
    robot = Robot()
    robot.robot_hallo()
    robot.robot_greeting()
    robot.robot_which()
    robot.restaurant_write()
    robot.robot_good_by()


if __name__ == '__main__':
    main()



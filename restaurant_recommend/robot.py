# -- coding: utf-8 --
from termcolor import colored

import csv_wr
import string


"""
ロボコがオススメのレストランを質問し、それに答えるアプリ。
答えはcsvファイルに書き込まれ、その後の質問で、オススメのレストランとしてロボコに紹介される。
"""


class Robot:
    def __init__(self):
        self.name = ''
        self.restaurant = ''
        self.robot_name = 'roboko'

    def robot_hallo(self):
        """
        名前を聞く関数。text/hallo.txtを読み込み出力する。空白の場合は「名無しさん」を返す。
        ************************************************************
        こんにちは、私はrobokoです。あなたの名前はなんでスカ？
        ************************************************************
        :return 名前
        """

        with open('text/hallo.txt', encoding='UTF-8') as f:
            print(colored("*"*60, 'green'))
            for row in f.readlines():
                print(colored(string.Template(row).substitute(robot_name=self.robot_name)
                              .rstrip(), 'green'))
            print(colored("*"*60, 'green'))
            self.name = input()
            if not self.name:
                self.name = '名無しさん'
            return self.name

    def robot_greeting(self):
        """
        csvに書き込まれた情報を読み込み、Countが一番多いレストランをオススメとしてtext/greeting.txtへ出力する。
        yesと答えれば、該当のレストランのCountが一つ増える。
        なお初めの質問で、csvファイルが存在しないか、データが何もない場合はこの関数はパスされ表示されない。

        ************************************************************
        私のオススメのレストランは、マックです。
        このレストランは好きですか？ [yes/no]
        ************************************************************
        """

        self.restaurant_list = []
        try:
            restaurant_dict = csv_wr.csv_read()  #ranking.csvがない、あるいはデータが何もない場合はパスする
            list_k = [k for k, v in sorted(restaurant_dict.items(), key=lambda x: -x[1])]
            self.restaurant = list_k[0]
            print(colored("*" * 60, 'green'))
            with open('text/greeting.txt', encoding='UTF-8') as cf:
                for row in cf.readlines():
                    print(colored(string.Template(row).substitute(restaurant=self.restaurant)
                                  .rstrip(), 'green'))
            print(colored("*" * 60, 'green'))
            ans = input('')
            if not ans:  #空白の場合は何もしない
                pass
            elif ans == 'yes' or 'Yes' or 'y':
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
        """
        好きなレストラン名を聞く関数。
        ************************************************************
        〜さん。どこのレストランが好きですか？
        ************************************************************
        :return: レストラン名
        """

        with open('text/which_restaurant.txt', encoding='UTF-8') as af:
            for row in af.readlines():
                print(colored('*'*60 + '\n' + string.Template(row).substitute(name=self.name)
                              + '\n' + '*'*60, 'green'), sep='')
        self.restaurant = input('').title()
        return self.restaurant

    def restaurant_write(self):
        """
        robot_which関数で返されるレストラン名をcsvに書き込む関数。
        ranking.csvに含まれていれば該当のCountが1増える。なければ新規で加わる。
        一番初めの質問の場合は新たにranking.csvが作成され書き込まれる。

        """
        self.restaurant_list = []
        try:
            restaurant_dict = csv_wr.csv_read()  #ranking.csvがなければexceptへ
            if not self.restaurant:  #空白が返された場合は何もしない
                pass
            elif self.restaurant in restaurant_dict:
                restaurant_dict[self.restaurant] += 1
            else:
                restaurant_dict[self.restaurant] = 1
            for name, count in restaurant_dict.items():
                restaurant_dict_insert = {'Name': name, 'Count': count}
                self.restaurant_list.append(restaurant_dict_insert)
            csv_wr.csv_write(self.restaurant_list)

        except:
            restaurant_dict_no = {}   #新しく作成されるcsvに書き込むための辞書
            restaurant_dict_no[self.restaurant] = 1
            for name, count in restaurant_dict_no.items():
                restaurant_dict_insert = {'Name': name, 'Count': count}
                self.restaurant_list.append(restaurant_dict_insert)
            csv_wr.csv_write(self.restaurant_list)

    def robot_good_by(self):
        """
        最後の文。
        ************************************************************
　　　　　〜さん、ありがとうございました。
　　　　　良い一日を！さようなら。
　　　　　Have a good day!
　　　　　************************************************************

        """

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



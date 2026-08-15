#プログラムのメインメニュー

"""
pip install cryptography
↑↑↑↑↑↑↑↑↑↑↑↑↑↑
これを実行前にインストールしてください。
"""

import enter
import pass_gen
import decrypt
import encrypt
from time import sleep

try:
    print()
    print("<<--パスワードジェネレーター-->>")
    print("パスワードの生成を行ったり、ファイルの復号及び暗号化を行います。")
    print("")


    while True:
        sleep(1)
        print("---- メニュー番号 ----")
        print("1. パスワード生成")
        print("2. ファイルの復号化")
        print("3. ファイルの暗号化")
        print("4. 終了")
        print("----------------------")

        #メニュー番号に応じて各プログラムを実行させます。
        select_num = enter.input_num_lim("メニュー番号を入力してください。",1,4)
        
        if int(select_num) == 1:
            #パスワード生成プログラムを実行
            pass_gen.execute()

        elif int(select_num) == 2:
            #復号化プログラムを実行
            decrypt.execute()

        elif int(select_num) == 3:
            #暗号化プログラムを実行
            encrypt.execute()

        elif int(select_num) == 4:
            print
            print("プログラムを終了します。")
            exit()

         
except KeyboardInterrupt:
    print()
    print("<<Ctrl+Cが押されました。プログラムを修了します。>>")
    print()
    exit()

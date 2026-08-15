#パスワードジェネレーター
#パスワードの長さと種類を設定してランダムなパスワードを生成

import os
import generar
import enter
import file_proc
from time import sleep

#外部からこのプログラムを実行させる関数
def execute():
    password = ""   #生成されるパスワード
    pass_len = 0    #パスワードの文字数

    try:
        print()
        print("<<--パスワードジェネレーター-->>")
        print("5~20文字のランダムなパスワードを生成します。")
        print()
        sleep(0.5)


        """パスワードの文字数の指定"""
        print("🧮--パスワード文字数の設定--🧮")
        
        pass_len = enter.input_num_lim("何文字のパスワードを生成しますか？",5,20)
        
        print()


        """パスワードの種類を設定"""
        print("🔧--パスワードの種類の設定--🔧")
        while True:
            #小文字の有無
            if enter.input_bool("小文字を含みますか？"):   #インプットでTrueかFalseで判断する関数
                #Trueが返された実行
                set_lower = True                               
            else:
                #Falseが返された実行 
                set_lower = False                                       
            print()

            #大文字の有無
            if enter.input_bool("大文字を含みますか？"):   
                set_upper = True                               
            else:
                set_upper = False                                       
            print()

            #数字の有無
            if enter.input_bool("数字を含みますか？"):   
                set_number = True                             
            else:
                set_number = False                                       
            print()
            
            #記号の有無
            if enter.input_bool("記号を含みますか？"):   
                set_sign = True                               
            else: 
                set_sign = False                                       
            print()

            #全てFalseなら入力し直し
            if (set_lower == False and
                set_upper == False and
                set_number == False and
                set_sign == False
                ):

                print("無効な設定：最低でも1つ含めてください。")
                print()
                sleep(1)
            else:
                break

        
        """入力内容の確認"""
        print("📄--入力の確認--📄")
        #パスワードの文字数を表示
        print(f"パスワード文字数：{pass_len}")


        #大文字、数字、記号、いずれも0であるときは有効と表示
        print(f"小文字：{set_lower}")
        print(f"大文字：{set_upper}")
        print(f"数字　：{set_number}")
        print(f"記号　：{set_sign}")

        print()


        #パスワードを生成させるかの確認
        if enter.input_bool("パスワードを生成しますか"):
            #パスワードの生成
            password = generar.pass_generate(pass_len,set_lower,set_upper,set_number,set_sign)   #パスワードを生成する関数(generate.py参照)                                        
        else:
            return                                     
        print()


        #生成したパスワードの表示
        print("<<パスワード生成完了>>")
        print(f"生成したパスワード：{password}")
        sleep(1)
        print()
        

        if os.path.isfile("passwd.txt"): #パスワードがかかれたファイルが既に存在すれば警告
            print("📌passwd.txtは既に存在します！書き込むと内容が置き換わります")
            print()
            sleep(0.5)

        #txtファイルに書き込むかの確認
        if enter.input_bool("パスワードをtxtファイルに書き込みますか？"):
            pass    #yesなら何もせず次のプログラムに移動
        else:
            return  #noならプログラムを終了
        print()


        if os.path.isfile("pass.key"): #キーファイルが既に存在すれば警告
            print("📌pass.keyは既に存在します！暗号化するとキーファイルは置き換わります")
            print()
            sleep(0.5)

        #ファイルを暗号化するかの確認
        if enter.input_bool("txtファイルを暗号化しますか？"):
            file_proc.pass_write(password) #パスワードをtxtファイルに書き込む関数
            file_proc.pass_lock()          #ファイルの暗号化を行う関数
            print()

            print("ファイルを暗号化しました。")
            print("※キーファイル(pass.key)は復号の際に必要なので変更を加えないでください。※")
        else:
            file_proc.pass_write(password) #暗号化しない場合はtxtファイルの書き込みのみ行う
            print()
            
            print("txtファイルに書き込みました。")


    #ctrl+cが押されたときの例外処理(エラーを表示させずにプログラムを中断させる)            
    except KeyboardInterrupt:
        print()
        print("<<Ctrl+Cが押されました。メニューに戻ります。>>")

if __name__ == "__main__":
    execute()
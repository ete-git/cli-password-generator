#暗号化されたtxtを復号、また暗号化を行います

import enter
import file_proc
from time import sleep

#外部からこのプログラムを実行させる関数
def execute():
    try:
        print()
        print("<<--txtファイルの暗号化-->>")
        print("passwd.txtの暗号化を行います。")
        print()
        sleep(0.5)


        #暗号化されたtxtファイルのパス指定
        passwd_path = enter.input_path("passwd.txt")
        print()


        #暗号化の処理
        if enter.input_bool("パスが読み込まれました。txtファイルを暗号化しますか？"):
            file_proc.pass_lock_alt(passwd_path)   #ファイルの暗号化をする関数
            print()
            print("ファイルの暗号化が完了しました。ファイルを確認ください。")
            print("※キーファイル(pass.key)は復号の際に必要なので変更を加えないでください。※")
        else:
            return


            
    #ctrl+cが押されたときの例外処理(エラーを表示させずにプログラムを中断させる)            
    except KeyboardInterrupt:
        print()
        print("<<Ctrl+Cが押されました。メニューに戻ります。>>")

if __name__ == "__main__":
    execute()
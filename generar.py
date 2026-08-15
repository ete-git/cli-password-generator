#パスワード生成用関数

import random

#引数を基に乱数を用いて生成したパスワードを返します
def pass_generate(length,low,up,num,zign):  #引数：パスワードの長さ&小文字、大文字、数字、記号の有無
    """
    引数について
    ・lengthはパスワードの長さ
    ・low～zignはいずれも引数がTrueなら使用、Falseなら使用しないと見なす

    例）文字数12文字で、小文字、数字を使用したいとき
        → pass_generate(12,True,False,True,False)
    """

    #生成されるパスワード
    password = ""
    
    #小文字
    lower = "abcdefghijklmnopqrstuvwxyz"
    #大文字
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #数字
    number = "1234567890"
    #記号
    sign = "!#$%&'=-^\+:@?,"


    #パスワードを生成に使用するリスト
    pass_lists = []
    

    #小文字を使用する場合はリストにupperを追加
    if low == True:
        pass_lists.append(lower)
    #大文字を使用する場合はリストにupperを追加
    if up == True:
        pass_lists.append(upper)
    #数字を使用する場合はリストにnumberを追加
    if num == True:
       pass_lists.append(number)
    #記号を使用する場合はリストにsignを追加
    if zign == True:
        pass_lists.append(sign)


    #パスワードの生成
    n = 0   #pass_lists内のインデックスをnと定義
    for i in range(int(length)):  #length(パスワードの長さ)の数だけループ
        #現在のインデックス値の文字列をsel_str格納
        sel_str = pass_lists[n]
        #sel_strの中にあるランダムな一文字をpasswordに格納
        password += sel_str[random.randint(0,len(sel_str)-1)]

        #インデックス値を1上げる
        n += 1

        #もしnがpass_listsの要素数以下ならnを0にさせる
        if n >= len(pass_lists):
            n = 0

    #完成したパスワードの文字列を更にランダムにする
    #パスワードをリスト化
    list_password = list(password)
    #リストの要素をシャッフルする
    random.shuffle(list_password)
    #リストから文字列に元に戻す
    password = "".join(list_password)

    return password #完成したパスワードを返す


# デバッグ用
# if __name__ == "__main__":
#     password = pass_generate(10,True,False,True,True)
#     print(password)
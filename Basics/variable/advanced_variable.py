"""複数の変数を一括でそれぞれに値を持たせる"""
# 変数の一括宣言
NUM1, NUM2, NUM3 = 5, 7, 9
print('NUM1:', NUM1)
print('NUM2:', NUM2)
print('NUM3:', NUM3)



"""左辺の変数の数と右辺の値の数が合わないとエラーになる"""
# 一括宣言をする際は変数の数と代入する値の数を同じにしなければならない
# NUM1, NUM2, NUM3 = 100
# print(NUM1)
# print(NUM2)
# print(NUM3)



"""複数の変数に一括で同じ値を入れる"""
# 複数の変数に同一の値を代入する
# この時、それぞれの変数に値を代入しているため、個別に値を変えても他の変数には影響しない
NUM4 = NUM5 = NUM6 = 100
print('NUM4:', NUM4)
print('NUM5:', NUM5)
NUM6 = 200
print('NUM6:', NUM6)



"""変数に*をつけると、変数の数より多い値はリストとなる"""
NUM7, *NUM8 = 1, 2, 3, 4, 5
print('NUM7:', NUM7)
print('NUM8:', NUM8) # 1より先は全てリストとしてNUM5に入る



"""１つの変数に,区切りの値を入れるとタプルとなる"""
# タプルの簡略記法
NUM9 = 10, 11, 12
print('NUM9:', NUM9)



"""変数の複数宣言がクラスの__init__でもできるのか試す"""
# 変数の複数宣言をクラスの初期化時にできるか試す
class VarTest(object):
    '''インスタンス変数テスト用クラス'''
    def __init__(self):
        self.NUM10, self.NUM11 = 10, 20


VAR_TEST = VarTest()
print('NUM10:', VAR_TEST.NUM10)
print('NUM11:', VAR_TEST.NUM11)


# ユークリッドの互除法は、以下のような手順ですすめます。

# ①最大公約数を求めたい2つの数のうち、大きい数を小さい数で割る。
# ②割って出てきたあまりで①の計算で割る数だった数を割られる数として割る。
# ③そのあまりで②の計算で割る数だった数を割られる数として割る。
# ④③の操作をあまりが出なくなるまで繰り返す。
# ⑤最後の計算の割る数が求める最大公約数である。

input1 = input()
input2 = input()

def CalcGreatestCommonDivisor(denominator, surplus):
    if surplus == 0:
        return denominator
    else:
        return CalcGreatestCommonDivisor(surplus, denominator % surplus)

print(CalcGreatestCommonDivisor(int(input1), int(input2)))
# ユークリッドの互除法で、求まった最大公約数で A,B のどちらか一方を割って、
# その結果を割っていない方に掛けた結果が、2つの数 A,B の 最小公倍数 になる。

input1 = int(input())
input2 = int(input())

def CalcGreatestCommonDivisor(denominator, surplus):
    if surplus == 0:
        return denominator
    else:
        return CalcGreatestCommonDivisor(surplus, denominator % surplus)
# 最大公約数
greatest_common_divisor = CalcGreatestCommonDivisor(input1, input2)

print(input2 / greatest_common_divisor * input1)
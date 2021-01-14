# 請求金額を計算する関数
def calc_billing_amount(tanka, suryo, tesuryo, tax_rate):
    return (tanka * suryo + tesuryo) * tax_rate


x = calc_billing_amount(tanka=100, suryo=10, tesuryo=50, tax_rate=1.1)
print(x)

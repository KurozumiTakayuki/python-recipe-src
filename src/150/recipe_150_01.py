from decimal import Decimal, ROUND_HALF_UP

x = Decimal("1.5454")
x0 = x.quantize(Decimal("0"), rounding=ROUND_HALF_UP)
print(x0)
x1 = x.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
print(x1)
x2 = x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(x2)
x3 = x.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
print(x3)

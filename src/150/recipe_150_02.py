from decimal import Decimal, ROUND_HALF_UP

x = Decimal("5454.1234")
x0 = x.quantize(Decimal("1E1"), rounding=ROUND_HALF_UP)
print(int(x0))
x1 = x.quantize(Decimal("1E2"), rounding=ROUND_HALF_UP)
print(int(x1))
x2 = x.quantize(Decimal("1E3"), rounding=ROUND_HALF_UP)
print(int(x2))
x3 = x.quantize(Decimal("1E4"), rounding=ROUND_HALF_UP)
print(int(x3))

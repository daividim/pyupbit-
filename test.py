import pyupbit

access = "g0WDzQ9FRaX0rtesy94foSZlj26iTxl0mYL72pD4"          # 본인 값으로 변경
secret = "VttTJiUKc6xRhpxyzuKiL0mbG4xeLKf98cnmg6o1"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-btc"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
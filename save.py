def calc_total():
    total = 0
    for i in range(1, 101):
        total = total + i
    return total

result = calc_total()

with open("result.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("前回の計算結果は", content, "でした⭐️")
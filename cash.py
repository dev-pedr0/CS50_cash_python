from cs50 import get_float

m = 0

while True:
    i = get_float("Change Owned: ") * 100
    if i > 0:
        break

while i > 24:
    i = i - 25
    m = m + 1

while i > 9:
    i = i - 10
    m = m + 1

while i > 4:
    i = i - 5
    m = m + 1

while i > 0.9:
    i = i - 1
    m = m + 1

print(m)

print("-- Tabuada Pronta --")

num = int(input("De qual número será a tabuada: "))

print(
    "-" * 20,
    """\n  {} X 1 = {}
  {} X 2 = {}
  {} X 3 = {}
  {} X 4 = {}
  {} X 5 = {}
  {} X 6 = {}
  {} X 7 = {}
  {} X 8 = {}
  {} X 9 = {}
  {} X 10 = {}\n""".format(
        num, num,
        num, num * 2,
        num, num * 3,
        num, num * 4,
        num, num * 5,
        num, num * 6,
        num, num * 7,
        num, num * 8,
        num, num * 9,
        num, num * 10
    ),
    "-" * 20
)

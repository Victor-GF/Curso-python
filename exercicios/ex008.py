print("-- Conversor de Metro --")

metros = float(input("Informe a quantidade de metros: "))

print(f"  -- {metros} Metros --")

print(
  """
    {:.3f}  Kilômetros
    {:.3f}   Hectômetros
    {:.3f}    Decâmetros
    {:.1f}   Decimetros
    {:.1f}  Centimetros
    {:.1f} Milimetros
  """.format(
    metros / 1000,
    metros / 100,
    metros / 10,
    metros * 10,
    metros * 100,
    metros * 1000
  )
)


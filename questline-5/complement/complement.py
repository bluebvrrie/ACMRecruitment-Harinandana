num = -42
bits = 8

two_complement = (num + (1 << bits)) % (1 << bits)

print(f"Decimal:",num)
print(f"{bits}-bit 2's complement:{two_complement:08b}")

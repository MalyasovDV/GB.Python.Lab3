def dec_to_bin(n):
    binaryValue = ""
    while (n > 0):
        binaryValue = str(n % 2) + binaryValue
        n = n // 2
    return binaryValue

dec = 45
print(dec, "->", dec_to_bin(dec))

dec = 3
print(dec, "->", dec_to_bin(dec))

dec = 2
print(dec, "->", dec_to_bin(dec))
empty_array = bytearray()
null_array = bytearray(11)
ints_array = bytearray((84, 114, 97, 100, 101, 109,
                        97, 114, 107, 32, 194, 174))
str_array = bytearray("Trademark ®", "utf-8")
bytes_array = bytearray(b"Trademark \xc2\xae")
print("bytes_array =", bytes_array)
print("bytes_array.decode() ->", bytes_array.decode())
str_literal = "Trademark ®"
print("str_literal.count('T') ->", str_literal.count('T'))
print("str_literal.index('T') ->", str_literal.index('T'))
print("bytes_array.count(0x54) ->", bytes_array.count(0x54))
print("bytes_array.index(0x54) ->", bytes_array.index(0x54))
print("\n")
print("bytes_array =", bytes_array)
bytes_array.append(32)
print("bytes_array =", bytes_array)
bytes_array.extend((194, 174))
print("bytes_array =", bytes_array)
print("bytes_array.decode() ->", bytes_array.decode())
bytes_array.remove(0x54)
print("bytes_array =", bytes_array)
print("bytes_array.decode() ->", bytes_array.decode())
bytes_array.insert(0, 0x54)
print("bytes_array =", bytes_array)
print("bytes_array.decode() ->", bytes_array.decode())
bytes_array.pop()
print("bytes_array =", bytes_array)
# print("bytes_array.decode() ->", bytes_array.decode())
bytes_array.pop()
print("bytes_array =", bytes_array)
print("bytes_array.decode() ->", bytes_array.decode())


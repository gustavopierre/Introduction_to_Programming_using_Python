a_range = range(5)
print("a_range ->", a_range)
print("list(a_range) ->", list(a_range))
print("type(a_range) ->", type(a_range))
for i in range(5):
    print(i, end=" ")
print()
a_range = range(10)
print("list(a_range) ->", list(a_range))
a_range = range(10, 16)
print("list(a_range) ->", list(a_range))
a_range = range(10, -1, -1)
print("list(a_range) ->", list(a_range))
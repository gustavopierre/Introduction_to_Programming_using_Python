from io import UnsupportedOperation

print("Default Windows 10 encoding 'cp1252'")
with open("written.txt", mode="w") as out_file:
    out_file.write("This is the first line on text.\n")

with open("written.txt", mode="a") as append_file:
    append_file.write("This line is appended at the end.\n")

with open("written.txt", mode="r") as in_file:
    print(in_file.read())

lines = (
    "Line 1\n", "Line 2\n",
    "Line 3\n", "Line 4\n",
)

try:
    out_file = open("without.txt", mode="w", buffering=1, encoding="us")
    out_file.writelines(lines)
    out_file.flush()
finally:
    out_file.close()

try:
    in_file = open("without.txt", encoding="us")
    print(in_file.tell(), end="<- File position before first read\n")
    print(in_file.read(7))
    print(in_file.tell(), end="<- File position after first read\n")
    print(in_file.read(7))
    print(in_file.tell(), end="<- File position after second read\n")
    in_file.seek(0, 0)
    print(in_file.tell(), end="<- BOF after seek(0,0)\n")
    in_file.seek(0, 2)
    print(in_file.tell(), end="<- EOF after seek(0,2)\n")
    print(in_file.read())
    print(in_file.tell(), end="<- EOF after read()\n")
    in_file.seek(7, 1)
    print(in_file.tell(), end="<- File position after relative seek\n")
except UnsupportedOperation:
    print("Text files do not support relative seeks")
finally:
    in_file.close()

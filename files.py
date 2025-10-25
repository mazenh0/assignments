f = open("/Users/mazenhamid/downloads/A4/a.txt")
# print(f.read())
# # print(f.read(4))
# print(f.readline())
# print(f.readline())
for line in f:
    print(line)

f.close()

try:
    f = open("/Users/mazenhamid/downloads/A4/b.txt")
    print(f.read())
except:
    print("the file you want to open DNE")
finally:
    f.close()
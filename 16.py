poem = '''e speed was far faster than light; \
       she started one day,' \
       in a relative way,' \
       and returned om the previous night.'''
print(len(poem))

fout = open('relativity','wt')    #将整首诗写到文件'relativity'中
print(fout.write(poem))
fout.close()

fout = open('relativity','wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset + chunk])
    offset += chunk


fin = open('relativity','rt')
poem = fin.read()
fin.close()
print(len(poem))

poem = ''
fin = open('relativity','rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
print(fin.close())

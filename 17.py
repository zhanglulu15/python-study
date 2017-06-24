bdata = bytes(range(0,256))
print(len(bdata))
fout = open('bfile','wb')
fout.write(bdata)
fin = open('bfile','rb')
fin.tell()

print(fin.seek(255))   #使用seek()读取最后一个字节


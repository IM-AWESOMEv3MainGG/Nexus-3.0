import marshal, zlib, base64, os, lzma, shutil
with open('script-here.txt', 'r',errors='ignore') as f:
    mysrc = f.read()
marsrc = compile(mysrc, 'coduter', 'exec')
encode1 = marshal.dumps(marsrc)
encode2 = zlib.compress(encode1)
encode3 = lzma.compress(encode2)
encode4 = base64.b64encode(encode3)
encode5 = base64.b85encode(encode4)

me = '__'
n = 0
while n < 75:
    n += 1
    me += 'NEXUS_VERSION_3__'
me += f' = "{encode4}"'
realcode = f'## Obfuscated by Nexus :troll:\nimport marshal, zlib, base64, lzma'
x = 0
while x < 150:
    x += 1
    realcode += '\n'+str(me)
realcode += f'\nexec(marshal.loads(zlib.decompress(lzma.decompress(base64.b64decode(base64.b85decode({encode5}))))))'
realcode += '\n'+str(me)
L = [str(realcode)]
with open("script-here.txt", "w") as file1:
    file1.writelines(L)
parent = os.getcwd()
shutil.copy2(f'{parent}\script-here.txt',f'{parent}\copy.txt')
f = open("script-here.txt", "r+")
f.truncate(0)
os.rename(f'{parent}\copy.txt', 'obfuscated.py')
#py3
#批量生成手机号码

f=open('tel.txt',mode='a')
for i in range(10):
    f.write('170'+str(i).zfill(8)+'\n')
f.close()
f=open('input.txt','r',encoding='UTF-8')
input_data=f.read()
f.close()

num=int(input_data.split('\n')[-2])
input_data=input_data.split('\n')[:-2]

dic={}
for i in input_data:
    t=i.split(':')
    dic[t[0]]=t[1]

dics=sorted(dic.items())

for i in dics:
    if num%int(i[0])==0:
        print(i[1],end='')
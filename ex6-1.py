import re,random,string
count1=int(input('请输入密码个数（必须大于零）:'))
i=0
passwds=[]
while i < count1:
    tmp=random.sample(string.ascii_letters+string.digits,8)
    passwd=''.join(tmp)
    if re.search('[0-9]',passwd) and re.search ('[A-Z]',passwd)and  re.search('[a-z]',passwd):
        passwds.append(passwd)
        i += 1
print(passwds)

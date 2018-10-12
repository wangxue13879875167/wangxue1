Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str1=input("请输入一个人的名字:")
请输入一个人的名字:
>>> str2=input("请输入一个国家的名字:")
请输入一个国家的名字:
>>> print("世界那么大，{}想去{}看看。".foymat(str1,str2))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print("世界那么大，{}想去{}看看。".foymat(str1,str2))
AttributeError: 'str' object has no attribute 'foymat'
>>> str1=input("please a name:")
please a name:李俊
>>> str2=input("please a country:")
please a country:把撒克斯坦
>>> print("世界那么大，{}想去{}看看。".format(str1,str2,))
世界那么大，李俊想去把撒克斯坦看看。
>>> 

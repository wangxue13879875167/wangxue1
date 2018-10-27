K=5
X=eval(input("请输入一个0~100之间的整数:"))
tem=0
while X!= K:
    tem += 1
    if(X>K):
        print("遗憾，太大了")
    else:
        print("遗憾，太少了")
    X=eval(input("请输入0~100之间的整数"))
print("预测{}次，你猜中了".format (tem))

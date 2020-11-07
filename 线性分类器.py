#直线方程s0+s1x+s2y=0，x,y,t是列表(表示很多点的坐标)
def judge(s0,s1,s2,x,y,t):
    #两个列表存入不同侧的点
    list0=[]
    list1=[]
 
    #对所有点进行判断
    for i in range(len(x)):
        temp=s1*x[i]+s2*y[i]+s0
        if temp<0:
            list0.append(i)
        else:
            list1.append(i)
    
    #求每一侧点的数量   
    lenlist0=len(list0)
    lenlist1=len(list1)
    #设flag为每一侧第一个点的坐标
    flag0=t[list0[0]]
    flag1=t[list1[0]]

    #如果两侧flag相同
    if flag0==flag1:
        print("No")
        return

    #如果每一侧只有两个点，单独进行判断
    if (lenlist0==2) and (t[list0[0]]!=t[list0[1]]):
        print("No")
        return

    if lenlist0>2:
        for i in range(1,lenlist0):
            if t[list0[i]]!=flag0:
                print("No")
                return
    #判断另一侧
    if (lenlist1==2) and (t[list1[0]]!=t[list1[1]]):
        print("No")
        return

    if lenlist1>2:
        for i in range(1,lenlist1):
            if t[list1[i]]!=flag1:
                print("No")
                return

    print("Yes")

if __name__ == "__main__":
    #n表示点的个数
    #m表示要查询的直线个数
    n,m=map(int,input().split())
    
    #用x,y,t存储每一个点的x,y,type_
    x=[0]*n
    y=[0]*n
    t=[0]*n

    for i in range(n):
        x[i],y[i],t[i]=input().split()
        x[i]=int(x[i])
        y[i]=int(y[i])
    
    #标准输入直线的信息
    s0=[0]*m 
    s1=[0]*m
    s2=[0]*m
    for i in range(m):
        s0[i],s1[i],s2[i]=map(int,input().split())

    for i in range(m):
        judge(s0[i],s1[i],s2[i],x,y,t)


    
        
        


















print("输入您的月薪金额，将显示该月需要交的所得税金额与您的税后工资")
q = float(input("请输入月薪金额："))
a1 = 0.03 #3000
b2 = 0.1  #3000-12000
c3 = 0.2  #12000-25000
d4 = 0.25 #25000-35000
e5 = 0.3  #35000-55000
f6 = 0.35 #55000-80000
g7 = 0.4  #80000
l = 3000 #3000数字
m = q-3000 # 三千后的工资
qqq = q * 0.03
q22 =  q - qqq
if q<=3000:
    print("您的税额为:",qqq,"您的工资为：",q22)
else:
    ts3000 = l*0.03 # 三千前的税
    a11 = m*0.1 # 三千后的税
    a12 = ts3000+a11 #两个税相加 扣税金额
    a13 = q-a12 # 工资-税 税后工资
if q>=3001 and q <= 11999:
    print("您的税额为:",a12,"您的工资为：",a13)
else:
    c31 = m*0.2 # 三千后的税
    c32 = c31+ts3000 #两个税相加 扣税金额
    c33 = q-c32 # 工资-税 税后工资
if q>=12000 and q <= 24999:
    print("您的税额为:",c32,"您的工资为：",c33)
else:
    d41 = m*0.25
    d42 = d41+ts3000
    d43 = q-d42
if q>=25000 and q <= 34999:
    print("您的税额为:",d42,"您的工资为：",d43)
else:
    e51 = m*0.3
    e52 = e51+ts3000
    e53 = q-e52
if q>=35000 and q <= 54999:
    print("您的税额为:",e52,"您的工资为：",e53)
else:
    f61 = m*0.35
    f62 = f61+ts3000
    f63 = q-f62
if q>=55000 and q <= 79999:
    print("您的税额为:",f62,"您的工资为：",f63)
else:
    g71 = m*0.4
    g72 = g71+ts3000
    g73 = q-g72
if q >= 80000:
    print("您的税额为:",g72,"您的工资为：",g73)
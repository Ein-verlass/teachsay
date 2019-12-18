"""
#iterantion and yield

def ha(max):
    n,a,b=0,0,1
    while n< max:
        yield b
        a,b=b,a+b
        n+=1
for x in ha(5):
    print(x)
f=ha(6)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print("_____________________")
class MyNumbers:
    def __init__(self,max):
        self.n, self.a, self.b,self.max = 0, 0, 1 ,max
    def __iter__(self):
        return self
    def __next__(self):
        if self.n<self.max:
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r
        raise StopIteration()
myclass = MyNumbers(5)
myiter = iter(myclass)
for x in myiter:
  print(x)
a,b=1,2
a,b=b,a
print(a,b)
"""

#不可变与可变参数
"""
a=[1,2,3]
b=a
c=[1,2,3]
print(a,b,c)
b.append(5)
print(a,b,c)

x=[2,3,4]
y=[2,3,4]
x.append(9)
print(x,y)
"""
#lambda
"""
a=3
b=[1,22,33]
sum=lambda x,y:x+y+a+b[1]
print(sum(1,3))
"""
"""
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],]
def ch(wd):
    we = [[row[i] for row in wd] for i in range(4)]
    return we

print(ch(matrix))
"""
"""
#1-1
for i in range(1,10):
    for j in range(1,i+1):
        print("%4d"%(i*j), end="")
    print("\n")
"""
"""
#1-2
import math
def gg():
    for i in range(3,501):
        for j in range(i,501):
            k=math.sqrt(i**2+j**2)
            if k%1==0 and k<=500:
                yield("%-6d%-6d %-6d"%(i,j,round(k)))               
f=gg()
for x in f:
    print(x)
"""
"""
#1-3
import random
q,con=["Please guess the number: ","Too big:","Too small:","You are right ",
           "","Please input 'q' to end or any keys to continue:"],''
guess=lambda i:input(q[i])
while(con!='q'):
    num,n,j=random.choice(range(101)),0,0
    print(num)
    while(n<7):
        k=int(guess(j))
        if k!=num:
            j=1 if k>num else 2
        else:
            break
        n+=1
    q[4]="The answer is "+str(num)+" you used 7 chances."
    con=guess(4) if n>=7 else guess(3)
    con=guess(5)
print("Bye-bye.")
"""
#main
"""
a=[3]
def ha():
    print("hahah")
def wa():
    a[0]+=3
    print(a[0])

if __name__ == '__main__':
   print('程序自身在运行')
   ha()
   wa()
else:
   print('我来自另一模块')
"""
#字符串的输出
"""
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print(table)
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
for x in range(1, 11):
    print(repr(x).center(2), repr(x*x).ljust(3), end=' ')
    print(repr(x*x*x).rjust(4))
print('{0} 和 {1}'.format('Google', 'Runoob'))
table = {'G': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
  print('{0:10} ==> {1:10f}'.format(name, number))
"""
#最大公约数和最小公倍数
"""
def gcd_lcm(x,y):
    if x%y==0:
        return y
    else:
        return gcd_lcm(y,x%y)
a,b=map(int,input("Pleae input two integers: :").split())
x=gcd_lcm(a,b)
print("The GCD of them is %d\nThe LCM of them is %d" %(x,a*b/x))
"""
#legendre
"""
def legendre(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        return ((2*n-1)*x*legendre(x,n-1)-(n-1)*legendre(x,n-2))/n 
a=float(input("Please input x:"))
b=int(input("Please input n:"))
print("The result is %s"%str(legendre(a,b)))
"""
#calender
'''
day=(myyear-1800)*365+mymonth*30
for x in range(1800,myyear+1):
    day+=isLeap(x)
for x in range(1,mymonth+1):
    day+=monthDay(x)
print(day//7,day%7)
'''
"""
week={'sun':-2,'mon':-1,'tue':0,'wed':1,'thu':2,'fri':3,'sat':4}
weekday=list(week.keys())
def isLeap(x):
    x=1 if x%400==0 or x%4==0 and x%100!=0  else 0
    return x
def monthDay(x):    
    if x<=7:
        y=31 if x%2==1 else 30        
    else:
        y=31 if x%2==0 else 30
    y=28+isLeap(myyear) if x==2 else y
    return y
def prWeek():
    print('-'*49)
    for x in range(7):
        print(weekday[x].title().rjust(7),end="")
    print('')
def calender():
    for x in range(6):
        for y in range(7):
            if y<=5 and week[weekday[y]]>week[weekday[y+1]]:
                week[weekday[y+1]]+=7
            a=week[weekday[y]]+7*x
            b=str(a) if a>0 and a<=monthDay(mymonth) else ''
            print(b.rjust(7),end="")
        print("")
def firstWeek():
    for z in range(1800,myyear):
        for y in range(7):
            week[weekday[y]]=week[weekday[y]]-(365+isLeap(z))%7
            if week[weekday[y]]<=-6 :
                     week[weekday[y]]+=7
    if mymonth>1:
        for x in range(mymonth-1):
            for y in range(7):
                 week[weekday[y]]=week[weekday[y]]+28-monthDay(x+1) 
                 if week[weekday[y]]<=-6 :
                     week[weekday[y]]+=7
myyear,mymonth=map(int,input("please input the year and month:").split())
firstWeek()
prWeek()
calender()
"""
#登录
'''
class account:
    name=''
    code=''
    agcode=''  
    def  __init__(self):
       self.name=input("请输入用户名:")
       while(1):
           self.code=input("请输入密码: ")
           if self.exco(self.code)=='':break      
       while(1):
           self.agcode=input('请再次输入密码:')
           if self.agcode==self.code:break
           print("两次输入的密码不一致")
       print("注册成功!")
    def exco(self,x):
        y=''
        y='密码必须包含字母' if x.isdigit() else y
        y='密码必须包含数字' if x.isalpha() else y
        y='密码长度至少8位' if len(x)<8 else y
        if y!='':print(y)
        return y
    def log(self):
        myname,mycode=input('请输入用户名:'),input('请输入密码登录，你有三次机会：')
        n=0
        while(n<2):            
            if self.name==myname and self.code==mycode:
                print('登陆成功')
                break
            else:
                mycode=input('密码错误，请重新输入:')
            n+=1
        else:print('登陆失败')
me=account()
me.log()
'''
#创建用户登录（未完成）
'''
class account:
    code=''
    agcode=''  
    def  __init__(self):
       
       while(1):
           self.code=input("请输入密码: ")
           if self.exco(self.code)=='':break      
       while(1):
           self.agcode=input('请再次输入密码:')
           if self.agcode==self.code:break
           print("两次输入的密码不一致")
       print("注册成功!")
    def exco(self,x):
        y=''
        y='密码必须包含字母' if x.isdigit() else y
        y='密码必须包含数字' if x.isalpha() else y
        y='密码长度至少8位' if len(x)<8 else y
        if y!='':print(y)
        return y
    def log(self):
        myname,mycode=input('请输入用户名:'),input('请输入密码登录，你有三次机会：')
        n=0
        while(n<2):            
            if buname==myname and self.code==mycode:
                print('登陆成功')
                break
            else:
                mycode=input('密码错误，请重新输入:')
            n+=1
        else:print('登陆失败')
while(1):
    name=input('请输入用户名:')
    buname=name
    locals()[name]=account()
    locals()[name].log()
'''
#格式化输入与输出
"""
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('{0[Runoob]:5}{0[Taobao]:2} {1:8}{2:3}'.format(table,"hah",99))
"""
'''
f = open("C:/Users/早开的晚霞/Desktop/foo.txt", "rb+")
f.write(b'0123456789abcdef')
#f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
#str1=f.readlines()
#print(str1)
#for line in f:
#    print(line, end='')
print(f.tell())
f.seek(-1,2)
print(f.read(1))
# 关闭打开的文件
f.close()
'''
'''

import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()
'''
'''
import pprint, pickle

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()
'''
#装饰器1
"""
def hi():
    def greet():
        return "hah"
    def welcom():
        return "233"
    return greet if 2 else welcom
print(hi()())
def hello():
    return "233"
def do(x):
    print(x())
do(hello)

def deco(x):
    def inf():
        print("www")
        x()
        print("qqqq")
    return inf
def rede():
    print("eeee")
rede()
rede=deco(rede)
rede()
@deco  # @deco等价于 ha=deco(ha)
def ha():
    print("nnnn")
ha()
print(ha.__name__) #ha被inf取代了
#以下是调用functools.wrpas函数解决
from functools import wraps
def a_new_decorator(a_func):
    @wraps(a_func)  #将wraps函数作为装饰
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction
 
@a_new_decorator
def a_function_requiring_decoration():
   
    print("I am the function which needs some decoration to "
          "remove my foul smell")
a_function_requiring_decoration()
print(a_function_requiring_decoration.__name__) #正常输出
"""
#装饰器2
"""
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated():
        if not can_run:
            return "Function will not run"
        return f()
    return decorated
 
@decorator_name
def func():
    return("Function is running")
 
can_run = True
print(func())
# Output: Function is running
 
can_run = False
print(func())


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging
 
@logit
def addition_func(x):

   return x + x
 
 
result = addition_func(4)
print(result)



from functools import wraps
def logit(logfile='out.txt'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator 
@logit()
def myfunc1():
    pass
 
myfunc1()
# Output: myfunc1 was called
# 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串

@logit(logfile='func2.txt')
def myfunc2():
    pass
 
myfunc2()
# Output: myfunc2 was called
# 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串

from functools import wraps
class wa():
    a=1
    b=2
    def __call__(self,x): #类的调用函数
        @wraps(x)
        def ha():
            print(self.a+1)
            return x()
        return ha
@wa()
def we():
    print("2333")
we()
"""

#利用__或者property装饰器进行私有变量的定义
"""
class Vector2D(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    @property
    def a(self):
        return self.x
    @property
    def b(self):
        return self.y
    @b.setter
    def b(self,c):
        self.y=c

v = Vector2D(3, 4)
print(v.a, v.b)
v.b = 8 
print(v.b)

class ha():
    def __init__(self):
        self.__a=3
    def wee(self):
        return self.__a+6
jj=ha()
c=jj.wee()
print(c)
print(jj.__a)
"""

#__slots__对类的外部添加进行限制，内部变量命名不能重复，如果重复需要用__init__进行命名
"""
class ha():
    __slots__ = ["x", 'y']
    def __init__(self):
        self.x = 1
we=ha()
we.z=4
print(we.z)

class Dog(object):
    def __init__(self, name):
        self.name = name


class Cat(object):
    __slots__ = ["name"]

    def __init__(self, name):
        self.name = name

d = Dog("dog")
d.age = 23
print(d.age)
c = Cat("cat")
print(c.name)
c.age = 24

class ha():
    
    __slots__ = []
    s=3
we=ha()

print(we.s)
we.x=4
print(we.x)

"""
#实验二
"""
num=[0]
student=[]
a=0
txt=('学号','姓名','数学','语文','英语')
def welcome():
    print("欢迎进入教务处学生成绩系统")
    print('1. 学生成绩录入\n2. 学生成绩修改\n3. 查询学生成绩\n4. 学生成绩排名\n5. 退出系统')
    num[0]=int(input("请输入功能序号进入相应功能:"))
def again(x):
    def txtpr():
        x()
        if input("\n是否继续(1-继续）（0-停止）:")=='1':return txtpr()             
    return txtpr
def prtxt():
    for x in range(5):print(txt[x].rjust(6+len(txt[x])), end='')
    print("")
    for z in range(a):
        for x in range(5):
            print(student[z][x].rjust(7+len(txt[x])),end='')
        print('')

@again
def entry():   
    student.append([input("请输入学生%s："%txt[x])  for x in range(5)])
    global a
    a+=1
    prtxt()
@again
def chansco():
    am=input("请输入学生学号:")
    q=0
    k=0
    for z in range(a):
        if am in student[z][0]:q=z
    print('1. 数学成绩修改\n2. 语文成绩修改\n3. 英语成绩修改\n ')
    k=int(input("请输入功能序号进入相应功能:"))
    if k==1:student[q][2]=input("数学成绩修改为：")
    elif k==2:student[q][3]=input("语文成绩修改为：")
    else:student[q][4]=input("英语成绩修改为：")        
@again
def check():
    am=input("请输入学生学号:")
    q=0
    k=0
    for z in range(a):        
        if am in student[z][0]:q=z
    for x in range(5):print(txt[x].rjust(8), end='')
    print("")
    for x in range(5):print(student[q][x].rjust(7+len(txt[x])),end='')
@again
def level():
    print("1.按照学号排序\n2.按照姓名排序\n3.按照数学成绩排序\n4.按照语文成绩排序\n5.按照英语成绩排序\n6.按照总分排序")
    k=int(input("请输入功能序号进入相应功能:"))
    def takese(ele):
        return (ele[k-1]) if k!=6   else int(ele[2])+int(ele[3])+int(ele[4])
    student.sort(key=takese,reverse=True)
    prtxt()
while num[0]!=5:
    welcome()
    if num[0]==1:
        entry()
    if num[0]==2:
        chansco()
    if num[0]==3:
        check()
    if num[0]==4:
        level()
"""
#tkinter模块1
"""
import tkinter as tk
ws=tk.Tk()
ws.title('hah')
ws.geometry('500x300')
var=tk.StringVar()
l=tk.Label(ws,textvariable=var,bg='green', font=('Arial', 12), width=30, height=2)
l.pack()
on_hit=False
def hit():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')
b=tk.Button(ws,text="233",font=('Arial', 12),activebackground='red',width=10,height=1,command=hit)
b.pack()
e1=tk.Entry(ws,show=None)
e2=tk.Entry(ws,show='2')
e1.pack()
e2.pack()
def insert_point(): # 在鼠标焦点处插入输入内容
    vars = e1.get()
    t.insert('insert', vars)
def insert_end():   # 在文本框内容最后接着插入输入内容
    vars = e1.get()
    t.insert('end', vars)
b1 = tk.Button(ws, text='insert point', width=10,
               height=2, command=insert_point)
b1.pack()
b2 = tk.Button(ws, text='insert end', width=10,
               height=2, command=insert_end)
b2.pack()
t = tk.Text(ws, height=3)
t.pack()
ws.mainloop()
"""
#tkinter2
"""
import tkinter as tk
window=tk.Tk()
window.geometry('300x300')
var2 = tk.StringVar()
var2.set((1,2,3,4)) # 为变量var2设置值
# 创建Listbox
lb = tk.Listbox(window, listvariable=var2,width=10,height=2)
lb.pack()
var = tk.StringVar()    # 定义一个var用来将radiobutton的值和Label的值联系在一起.
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()
def print_selection():
    l.config(bg='blue')
r1 = tk.Radiobutton(window, text=' A', variable=var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='B', variable=var, value='B', command=print_selection)
r2.pack()
c1 = tk.Checkbutton(window, text='Python',variable=var, onvalue=1, offvalue=0, command=print_selection)    # 传值原理类似于radiobutton部件
c1.pack()
c2 = tk.Checkbutton(window, text='C++',variable=var, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
def print_selection1(v):
    l.config(text='you have'+v)
s = tk.Scale(window, label='try me', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection1)
s.pack()
"""
"""
import tkinter as tk 
 
window = tk.Tk()
window.title('My Window')
window.geometry('500x300') 
canvas = tk.Canvas(window, bg='green', height=200, width=500)
image_file = tk.PhotoImage(file='pic.gif')  
image = canvas.create_image(250, 0, anchor='n',image=image_file) 
#image=canvas.create_image(250,0,anchor='n',image=tk.PhotoImage(file='pic.gif'))
canvas.pack()
def moveit():
    canvas.move(image, 2, 2) 
 

b = tk.Button(window, text='move item',command=moveit).pack()
window.mainloop()
"""
#双重字典查询
"""
hit = {
'01':{'name':'航天学院', 'url':'http://sa.hit.edu.cn/'},
'02':{'name':'电信学院', 'url':'http://seie.hit.edu.cn/'},
'03':{'name':'机电学院', 'url':'http://sme.hit.edu.cn/'},
'04':{'name':'材料学院', 'url':'http://mse.hit.edu.cn/'},
'05':{'name':'能源学院', 'url':'http://power.hit.edu.cn/'},
'06':{'name':'电气学院', 'url':'http://hitee.hit.edu.cn/'},
'07':{'name':'仪器学院', 'url':'http://ise.hit.edu.cn/'},
'08':{'name':'数学学院', 'url':'http://math.hit.edu.cn/'},
'09':{'name':'物理学院', 'url':'http://physics.hit.edu.cn/'},
'10':{'name':'经管学院', 'url':'http://som.hit.edu.cn/'},
'11':{'name':'土木学院', 'url':'http://civil.hit.edu.cn/'},
'12':{'name':'环境学院', 'url':'http://env.hit.edu.cn/'},
'13':{'name':'建筑学院', 'url':'http://jzxy.hit.edu.cn/'},
'14':{'name':'交通学院', 'url':'http://jtxy.hit.edu.cn/'},
'15':{'name':'化工学院', 'url':'http://chemeng.hit.edu.cn/'},
'16':{'name':'生命学院', 'url':'http://life.hit.edu.cn/'},
'17':{'name':'外语学院', 'url':'http://fls.hit.edu.cn/'},
'18':{'name':'人文学院', 'url':'http://rwxy.hit.edu.cn/'},
'19':{'name':'计算机学院', 'url':'http://cs.hit.edu.cn/'},
'20':{'name':'马克思学院', 'url':'http://marx.hit.edu.cn/'}
}
num=0
def welcome():
    global num
    print("欢迎进入教务处学院查询系统")
    print('1. 按编号查询\n2. 按名称查询\n3. 退出')
    num=int(input("请输入功能序号进入相应功能:"))
def nu():
    x=input('请输入编号:')
    try:print(hit[x])
    except KeyError:
        print("查询失败")
        return nu()
def na():
    x=input('请输入学院名称:')
    v=iter(hit.values())
    for i in range(20):
        s=next(v)
        if s['name']==x:return '0'+str(i+1)+'\t'+s['url'] if i+1<10 else str(i+1)+'\t'+s['url']
    else:
        print("查询失败")
        return na()
            
while(1):
    welcome()
    if num==1:nu()
    elif num==2:print(na())
    else:break
"""

#sqlitey与tkinter运用实例
'''
import sqlite3 as sq
import tkinter as tk
import tkinter.messagebox 
def entry():
   display.frame.pack_forget()
   fr=tk.Frame(display.ws)
   fr.pack(fill="both", expand=True)
   def ha():
      fr.pack_forget()
      display.frame.pack()
      display.ws.mainloop()
   for i in range(5):l1=tk.Label(fr,text=tex[i]+":").place(x=150,y=40+i*30)
   t1=tk.Entry(fr,show = None)
   t1.place(x=220,y=40)
   t2=tk.Entry(fr,show = None)
   t2.place(x=220,y=70)
   t3=tk.Entry(fr,show = None)
   t3.place(x=220,y=100)
   t4=tk.Entry(fr,show = None)
   t4.place(x=220,y=130)
   t5=tk.Entry(fr,show = None)
   t5.place(x=220,y=160)
   def sub():
      try:
         c.execute("insert into student values({0},'{1}',{2},{3},{4})".format(t1.get(),t2.get(),t3.get(),t4.get(),t5.get()))
         con.commit()
      except : tk.messagebox.showwarning(title='警告', message='请勿重复提交学生信息！')
   s1=tk.Button(fr,text="提交",activebackground='#0000a3',command=sub).place(x=220,y=190)
   s2=tk.Button(fr,text="结束",activebackground='#0000a3',command=ha).place(x=300,y=190)
   display.ws.mainloop()
def chansco():
   display.frame.pack_forget()
   fr=tk.Frame(display.ws)
   fr.pack(fill="both", expand=True)
   def ha():
      fr.pack_forget()
      display.frame.pack()
      display.ws.mainloop()
   l1=tk.Label(fr,text="学生学号:").place(x=150,y=40)
   t1=tk.Entry(fr,show = None)
   t1.place(x=220,y=40)
   t2=tk.Entry(fr,show = None)
   t2.place(x=220,y=70)
   var1 = tk.StringVar()  
   var2 = tk.StringVar()
   var1.set('修改项目')
   var2.set(('姓名','语文',"数学","英语"))
   def gai():
      try:
         if var1.get()!='姓名':v=list(c.execute("update student set {0}={1} where 学号={2} ".format(var1.get(),t2.get(),t1.get())))
         else:v=list(c.execute("update student set {0}='{1}' where 学号={2} ".format(var1.get(),t2.get(),t1.get())))
         con.commit()
      except :tk.messagebox.showwarning(title='警告', message='请按照正确格式输入！')
   def wa(event):
      lb.place(x=150,y=100,width=60,height=100)     
   def za(event):
      lb.place_forget()
   def we(event):
         value = lb.get(lb.curselection())
         var1.set(value)
   l2=tk.Button(fr,textvariable=var1)
   l2.place(x=150,y=70)  
   l2.bind("<Enter>", wa)
   l2.bind("<Leave>", za)
   lb = tk.Listbox(fr, listvariable=var2,width=20)
   lb.bind("<Enter>", wa)
   lb.bind("<Leave>", za)  
   lb.bind('<Double-Button-1>',we)
   s1=tk.Button(fr,text="提交",activebackground='#0000a3',command=gai).place(x=220,y=160)
   s2=tk.Button(fr,text="结束",activebackground='#0000a3',command=ha).place(x=300,y=160)
def check():
   display.frame.pack_forget()
   fr=tk.Frame(display.ws)
   fr.pack(fill="both", expand=True)
   def ha():
      fr.pack_forget()
      display.frame.pack()
      display.ws.mainloop()
   l1=tk.Label(fr,text="学生学号:").place(x=150,y=40)
   t1=tk.Entry(fr,show = None)
   t1.place(x=220,y=40)
   var1=tk.StringVar()
   var2=tk.StringVar()
   var3=tk.StringVar()
   var4=tk.StringVar()
   var5=tk.StringVar()
   ls1=tk.Label(fr,text="姓名").place(x=120,y=70)
   ls2=tk.Label(fr,text="语文").place(x=160,y=70)
   ls3=tk.Label(fr,text="英语").place(x=200,y=70)
   ls4=tk.Label(fr,text="数学").place(x=240,y=70)
   ls5=tk.Label(fr,text="总分").place(x=280,y=70)
   lts1=tk.Label(fr,textvariable=var1)
   lts2=tk.Label(fr,textvariable=var2)
   lts3=tk.Label(fr,textvariable=var3)
   lts4=tk.Label(fr,textvariable=var4)
   lts5=tk.Label(fr,textvariable=var5)
   def cha():
      try:
         cur=list(c.execute("select * from student where 学号={}".format(t1.get())))
         var1.set(cur[0][1])
         lts1.place(x=120,y=90)
         var2.set(cur[0][2])
         lts2.place(x=160,y=90)
         var3.set(cur[0][3])
         lts3.place(x=200,y=90)
         var4.set(cur[0][4])
         lts4.place(x=240,y=90)
         var5.set(cur[0][2]+cur[0][3]+cur[0][4])
         lts5.place(x=280,y=90)
      except :tk.messagebox.showwarning(title='警告', message='无当前学生信息！')
   s1=tk.Button(fr,text="查询",activebackground='#0000a3',command=cha).place(x=220,y=160)
   s2=tk.Button(fr,text="结束",activebackground='#0000a3',command=ha).place(x=300,y=160)
def level():
   display.frame.pack_forget()
   fr=tk.Frame(display.ws,width=500,height=300)
   fr.pack()
   def insco():
      sb=tk.Scrollbar(display.ws,orient="vertical",)
      sb.place(x=50,y=25,height=200)
      tx=tk.Text(fr,bg="#00f")
      tx.place(x=50,y=25,width=200,height=200)
      sb.configure(command=tx.yview)
   def ha():
      fr.pack_forget()
      display.frame.pack()
      display.ws.mainloop()
   var1 = tk.StringVar()
   var2 = tk.StringVar()
   var1.set('排序方式')
   var2.set(tex)
   def wa(event):
      lb.place(x=20,y=80,width=60,height=120)     
   def za(event):
      lb.place_forget()
   def we(event):
         value = lb.get(lb.curselection())
         var1.set(value)
   def sor():      
      try:
         sb=tk.Scrollbar(fr,orient="vertical")
         sb.place(x=440,y=25,height=200)
         tx=tk.Canvas(fr,bg="#00f")
         tx.place(x=80,y=25,width=360,height=200)
         ul=tk.Text(tx)
         ul.place(width=360,height=200)
         sb.config(command=ul.yview)
         ul.config(yscrollcommand=sb.set)
         
         hau=list(c.execute("select * from student order by {} desc".format(var1.get())))
         a=list(c.execute("select count(学号) from student "))
         for i in range(5):
            ul.insert(tk.END,'{0}'.format(tex[i]).center(8))
         ul.insert(tk.END,'\n')
         for j in range(a[0][0]):
            for i in range(5):
               if i==0:ul.insert(tk.END,'{0}'.format(hau[j][i]).ljust(12))
               elif i==1:ul.insert(tk.END,'{0}'.format(hau[j][i]).ljust(12-len(hau[j][i])))
               else:ul.insert(tk.END,'{0}'.format(hau[j][i]).ljust(9))
            ul.insert(tk.END,'\n')
      except:tk.messagebox.showwarning(title='警告', message='请选择排序方式！')
   l2=tk.Button(fr,textvariable=var1)
   l2.place(x=20,y=50)  
   l2.bind("<Enter>", wa)
   l2.bind("<Leave>", za)
   lb = tk.Listbox(fr, listvariable=var2,width=20,height=10)
   lb.bind("<Enter>", wa)
   lb.bind("<Leave>", za)  
   lb.bind('<Double-Button-1>',we)
   s1=tk.Button(fr,text="排序",activebackground='#0000a3',command=sor).place(x=120,y=250)
   s2=tk.Button(fr,text="结束",activebackground='#0000a3',command=ha).place(x=200,y=250)
def dexit():
   display.ws.destroy()
   con.commit()
class window():
   ws=tk.Tk()
   frame = tk.Frame(ws)
   frame.pack()
   def __init__(self):
      self.ws.title('哈工大教务处学生成绩系统')
      self.ws.geometry('500x300')
   def users(self):
      l=tk.Label(self.frame,text='欢迎进入教务处学生成绩系统',fg="#fff",bg='#00006e', font=('Microsoft Yahei UI', 12), width=30, height=2).pack()
      b1=tk.Button(self.frame,text="学生成绩录入",font=('Microsoft Yahei UI', 12),activebackground='red',width=10,height=1,command=entry).pack()
      b2=tk.Button(self.frame,text="学生信息修改",font=('Microsoft Yahei UI', 12),activebackground='red',width=10,height=1,command=chansco).pack()
      b3=tk.Button(self.frame,text="查询学生成绩",font=('Microsoft Yahei UI', 12),activebackground='red',width=10,height=1,command=check).pack()
      b4=tk.Button(self.frame,text="学生成绩排名",font=('Microsoft Yahei UI', 12),activebackground='red',width=10,height=1,command=level).pack()
      b5=tk.Button(self.frame,text="退出",font=('Microsoft Yahei UI', 12),activebackground='red',width=10,height=1,command=dexit).pack()
      self.ws.mainloop()
con=sq.connect("hit.db")
c=con.cursor()
tex=("学号","姓名","语文","英语","数学")
#c.execute(create table student(学号 int primary key not null,姓名 text not null,语文  int,英语  int,数学  int);)
con.commit()
display=window()
display.users()
'''
#作业5-1
"""
class person():
    name=''
    age=''
    def __init__(self):
        self.name=input("请输入姓名:")
        self.age=input("请输入年龄:")
    def getPay(self):
        pass
    def pri(x):
        def pr(self):
            print('姓名：',self.name)
            print('年龄：',self.age)
            x(self)
        return pr
class Manager(person):
    money=0
    def __init__(self):
        person.__init__(self)
    def getPay(self):
         self.money=500000
    @person.pri
    def pri(self):       
        print('薪水：',self.money)
class Employee(person):
    salary=''
    year=''
    money=0
    def __init__(self):
        person.__init__(self)
        self.salary=int(input("请输入月薪:"))
        self.year=int(input("请输入年终奖:"))
    def getPay(self):
        self.money=self.salary*12+self.year
    @person.pri
    def pri(self):       
        print('薪水：',self.money)
class Salesman(person):
    salary=''
    profit=''
    money=0
    def __init__(self):
        person.__init__(self)
        self.salary=int(input("请输入月薪:"))
        self.profit=int(input("请输入销售利润:"))
    def getPay(self):
        self.money=int(self.salary*12+self.profit*0.15)
    @person.pri
    def pri(self):       
        print('薪水：',self.money)
while(1):
    try:
        job=input('请输入职务: ')
        if job=='Manager':man=Manager()
        elif job=='Employee':man=Employee()
        elif job=='Salesman':man=Salesman()
        man.getPay()
        man.pri()
    except NameError:print('请输入正确的职务（Manager\Employee\Salesman)')
"""
#beautiful soup
"""
from bs4 import BeautifulSoup as bs
import re
htm= 
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>


so=bs(htm,'html.parser')
#print(so.prettify())
#beautifulsoup1

print(so.title)
print(so.title.name)
print(so.title.string)
print(so.a.parent.name)
print(so.p['class'])
print(so.p.attrs)
so.a.string.replace_with("233")
x=iter(so.find_all('a'))
for i in range(len(so.find_all('a'))):print(next(x))
so.p['id']='ha'
print(so.p.attrs)

print(so.a.string)
print(so.name)
print('--------------------------------------------------')
for i in range(len(so.contents)):print(so.contents[i])
print(23)
he=so.body
ti=he.contents[0]
print(he)
for i in he.children:print(i)
print("-----------")
s=so.head
for i in he.descendants:print(i)
print(23)
for i in so.strings:print(repr(i))
for i in so.stripped_strings:print(repr(i))

#beautiuflsoup2

t=so.title
print(t.string.parent)
print(so.parent)
for i in so.a.parents:print(i.name)
ll=bs("<a><b>text1</b><c>text2</c></b></a>",'html.parser')
print(ll.prettify())
print(ll.b.next_sibling)
print(ll.c.previous_sibling)
print("-----------")
sl=so.find("a",id='link3')
print(sl)
print(sl.next_sibling)
print(sl.next_element)
print(sl.previous_sibling)
print(sl.previous_element)
print("______________")
import re
print(so.find_all("a"))
print(23)
print(so.a.name)
for i in so.find_all(re.compile("t")):print(i.name)
#print(so.find_all(re.compile("^b")))
for i in so.find_all(["a","b"]):print(i.previous_element)
print("-------------------")
for i in so.find_all(True):print(i.string)
print(so("a"))
print(so.find("a"))

print(so.select(".sister"))

"""
#urlib
"""
import urllib.request
#response=urllib.request.urlopen('https://www.python.org')  #请求站点获得一个HTTPResponse对象
#print(response.read().decode('utf-8'))   #返回网页内容
#print(response.getheader('server')) #返回响应头中的server值
#print(response.getheaders()) #以列表元祖对的形式返回响应头信息
#print(response.fileno()) #返回文件描述符
#print(response.version)  #返回版本信息
#print(response.status)  #返回状态码200，404代表网页未找到
#print(response.debuglevel) #返回调试等级
#print(response.closed)  #返回对象是否关闭布尔值
#print(response.geturl()) #返回检索的URL
#print(response.info()) #返回网页的头信息
#print(response.getcode()) #返回响应的HTTP状态码
#print(response.msg)  #访问成功则返回ok
#print(response.reason) #返回状态信息

from urllib.request import urlopen
import urllib.parse

data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8') 
#data需要字节类型的参数，使用bytes()函数转换为字节，使用urllib.parse模块里的urlencode()方法来讲参数字典转换为字符串并指定编码
response = urlopen('http://httpbin.org/post',data=data)
print(response.read())
print(type(response))
"""
#requests
import requests
'''
url = 'https://www.runoob.com/w3cnote/python-spider-intro.html'
r = requests.get(url)
print(type(r))    # 类型是str（JSON格式）
print(r.status_code)
print("--------")
print(r.text)
print("--------")
print(r.cookies)
'''
"""
r = requests.get("http://github.com/favicon.ico")
print(r.text)
print(r.content)
# 保存图片
with open('favicon.ico','wb') as f:
    f.write(r.content)
"""
"""
from bs4 import BeautifulSoup as bs
import re
import json
ur2 = 'https://www.runoob.com/w3cnote/python-spider-intro.html'

#print(r.json().load())
#so=bs(r.text,'html.parser')

data = {
    'name': 'germey',
    'age': 22
}
url = 'http://httpbin.org/get'
#r = requests.get(ur2,params=data)
r1 = requests.post(url, params=data)
r2 = requests.get(url)

#print(r1.json())
print(r1.text)
print(r2.status_code)
print("______________")
print(r2.headers)
print("______________")
print(r2.cookies)
print("______________")
print(r2.history)
#v=so.find_all("a")
#x=iter(v)
#for i in so.find_all("a"):
    #print(i.string)
"""
"""
#贪吃蛇
import tkinter as tk
import random as rd
import time as tm
import tkinter.messagebox 

ws=tk.Tk()
ws.geometry("500x500")
ws.title("Snake")

fr=tk.Frame(ws,width=500,height=500)
fr.pack()

def start():
    fr.pack_forget()
    mygame=gameview()

title=tk.Label(fr,text="贪吃蛇",font=('Arial', 44)).place(x=180,y=100)
    
play=tk.Button(fr,text="Play",command=start)
play.place(x=250,y=250)

class gameview():
    def __init__(self):
        self.x=rd.randrange(0,191,10)
        self.y=rd.randrange(0,91,10)

        self.snakelist=[0]
        self.listx=[self.x]
        self.listy=[self.y]

        self.a=rd.randrange(0,91,10)
        self.b=rd.randrange(0,91,10)

        print(self.x,self.y,self.a,self.b)
        self.i=1
        self.j=0
           
        self.ifmove=False

        self.var1="233"
        
        self.main=tk.Frame(ws)
        self.main.pack(fill="both",expand=True)
        
        self.border=tk.Canvas(self.main,bg="#000",width=500,height=400)
        
        self.snake=self.border.create_rectangle(self.x,self.y,self.x+10,self.y+10,fill="#0ff")
        self.food=self.border.create_rectangle(self.a,self.b,self.a+10,self.b+10,fill="#f00")
        
        self.border.pack()

        def end():
            self.main.pack_forget()
            fr.pack()

        self.over=tk.Button(self.main,text="end",command=end)
        self.over.place(x=250,y=450)

        self.text1=tk.StringVar()
        self.text1.set("Play")

        self.text2=tk.StringVar()
        self.text2.set("0")

        self.score=tk.Label(self.main,text="Score:").place(x=100,y=450)
        self.myscore=tk.Label(self.main,textvariable=self.text2).place(x=140,y=450)
        
        def timeflood():
            while(self.ifmove):   
                self.border.move(self.snake,10*self.i,10*self.j)
                self.listx[0]+=10*self.i
                self.listy[0]+=10*self.j
                print("当前头部位置：",self.listx[0],self.listy[0])

                if(len(self.listx)>2):
                    for k in  range(len(self.listx)-1):
                        self.listx[k+1]+=10*self.i
                        self.listy[k+1]+=10*self.j                        
                prex=tuple(self.listx)
                prey=tuple(self.listy) 
                
                for k in range(len(self.snakelist)-1):
                    #self.border.move(self.snakelist[k+1],10*self.prei,10*self.prej)
                    self.border.coords(self.snakelist[k+1],prex[k]-10*self.i,prey[k]-10*self.j,prex[k]+10*(1-self.i),prey[k]+10*(1-self.j))
                    self.listx[k+1]=prex[k]-10*self.i
                    self.listy[k+1]=prey[k]-10*self.j

                    print("当前身子%d位置："%(k+1),self.listx[k+1],self.listy[k+1])
                
                eat()

                tm.sleep(0.4)
                ws.update()

                boun()
                boom()
                
        def ifplay():
            self.ifmove=not self.ifmove
            if self.ifmove:self.text1.set("Pause")
            else:self.text1.set("Continue")
            print(self.text1)
            
            if self.var1=="replay":
                self.var1='233'

                self.border.delete("all")
          
                self.x=rd.randrange(0,191,10)
                self.y=rd.randrange(0,91,10)

                self.a=rd.randrange(0,191,10)
                self.b=rd.randrange(0,91,10)

                self.snake=self.border.create_rectangle(self.x,self.y,self.x+10,self.y+10,fill="#0ff")
                self.food=self.border.create_rectangle(self.a,self.b,self.a+10,self.b+10,fill="#f00")

                self.snakelist=[0]
                self.listx=[self.x]
                self.listy=[self.y]
                
                self.text2.set('0')
                self.text1.set("Continue")
                self.ifmove=False
                
            timeflood()   
            
        self.start=tk.Button(self.main,textvariable=self.text1,command=ifplay)
        self.start.place(x=350,y=450)

        def up(event):
            if self.ifmove==True:              
                self.i=0
                self.j=-1
        
        def down(event):
            if self.ifmove==True:
                self.i=0
                self.j=1
        
        def left(event):
            if self.ifmove==True:              
                self.i=-1
                self.j=0
        
        def right(event):
            if self.ifmove==True:
                self.i=1
                self.j=0
            
        ws.bind("<Up>",up)
        ws.bind("<Down>",down)
        ws.bind("<Right>",right)
        ws.bind("<Left>",left)

        def fooding():
            self.a=rd.randrange(0,191,10)
            self.b=rd.randrange(0,91,10)
            return (self.a,self.b,self.a+10,self.b+10)
        def eat():
            if self.listx[0]==self.a and self.listy[0]==self.b:
                print(23)
                self.border.coords(self.food,fooding())
                print(2,self.a,self.b)
                lenth()
        def lenth():
            k=len(self.snakelist)-1
            print("当前身子长度%d"%(k+2))
            self.snakelist.append(self.border.create_rectangle(self.listx[k]-10*self.i,self.listy[k]-10*self.j,self.listx[k]+10*(1-self.i),self.listy[k]+10*(1-self.j),fill="#f0f"))

            self.text2.set(str(len(self.snakelist)-1))
            
            self.listx.append(self.listx[k]-10*self.i)
            self.listy.append(self.listy[k]-10*self.j)
            print("身体生成于：",self.listx[k]-10*self.i,self.listy[k]-10*self.j)

        def boun():
            if (self.listx[0]<0 or self.listx[0]>=500 or self.listy[0]<0 or self.listy[0]>=400):
                tk.messagebox.showwarning(title='失败', message='游戏结束')
                self.var1="replay"
                self.ifmove=False
                self.text1.set(self.var1)

        def boom():
            for k in range(len(self.snakelist)-1):
                if (self.listx[0]==self.listx[k+1] and self.listy==self.listy[k+1]):
                    print(23)
                    tk.messagebox.showwarning(title='失败', message='游戏结束')
                    self.var1="replay"
                    self.ifmove=False
                    self.text1.set(self.var1)
"""
#socket

import socket 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
print(host)
s.bind(('127.0.0.1',9092))#127那个是回路ip 自己访问自己
s.listen(5)
print("23333")

while True:
    sock,addr=s.accept() #sock 是真正的管道
    print("连接地址: %s" % str(addr))
    data=sock.recv(1024)
    print(data)
    sock.send("hahahhaah")
    #sock.close()

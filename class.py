#_*_coding:utf-8_*_
#类定义

class people: 
    name = '' 
    age = 0 
    __weight = 0 
    def __init__(self,n,a,w): 
        self.name = n 
        self.age = a 
        self.__weight = w 
    def speak(self): 
        print("%s is speaking: I am %d years old:%d" %(self.name,self.age,self.__weight)) 

#工程师继承人
class engerneer(people):
    C_language=''
    def __init__(self,n,a,w,c):
        people.__init__(self,n,a,w)
        self.C_language=c
    def speak(self): 
        print("%s is speaking: I am %d years old,and I am use C program language %d"%(self.name,self.age,self.C_language))

#默认不继承的管理职位
class manager():
    manager_year=''
    def __init__(self,mey):
        self.manager_year=mey
    def speak(self):
        print("%s is speaking: I am manager for %d years. "%(self.name,self.manager_year))

#多重继承职位
class VP(manager,engerneer):
    count=''
    def __init__(self,n,a,w,c,mey,count):
        engerneer.__init__(self,n,a,w,c)
        manager.__init__(self,mey)
        self.count=count
    def speak(self):
        print("%s is speaking: I am %d years old,use C %d year,manager %d people."%(self.name,self.age,self.C_language,self.manager_year))



p = people('tom',10,30) 
p.speak()
print "\n**************\n"
e=engerneer('gerry',22,100,2)
e.speak()
print "\n**************\n"
v=VP('boss',30,80,10,100,5)
v.speak()

import numpy as np

class var():
    # weather -> 1:sunny ,0: rainy
    WeatherSunny=1
    WeatherRainy = 0
    weather=[1,0,1,1,1,0,0,1,1,0]
    #car-> 1: working , 0: broken
    CarWorking=1
    CarBroken = 0

    car=[1,0,1,1,1,0,0,1,0,0]
    #class -> 1: go-out, 0:stay home
    GoOutClass=1
    StayHomeClass = 0

    class_=[1,1,1,1,1,0,0,0,0,0]
    x1 = 1
    x2 = 1
    Reset=1



def Pclass1():return len([i for i in var.class_ if i==var.GoOutClass])/len(var.class_)
def Pclass0():return len([i for i in var.class_ if i==var.StayHomeClass])/len(var.class_)

def PSunny_Goout():return len([i for i in range(0,len(var.class_)) if var.class_[i]==var.GoOutClass and var.weather[i]==var.WeatherSunny]) / len([i for i in var.class_ if i==var.GoOutClass])
def Prainy_Goout():return len([i for i in range(0,len(var.class_)) if var.class_[i]==var.GoOutClass and var.weather[i]==var.WeatherRainy]) / len([i for i in var.class_ if i==var.GoOutClass])
def Prainy_stayhome():return len([i for i in range(0,len(var.class_)) if var.class_[i]==var.StayHomeClass and var.weather[i]==var.WeatherRainy]) / len([i for i in var.class_ if i==var.StayHomeClass])
def Psunny_stayhome():return len([i for i in range(0,len(var.class_)) if var.class_[i]==var.StayHomeClass and var.weather[i]==var.WeatherSunny]) / len([i for i in var.class_ if i==var.StayHomeClass])


def Pworking_Goout():return len([i for i in range(0,len(var.class_)) if var.class_[i]==var.GoOutClass and var.car[i]==var.CarWorking]) / len([i for i in var.class_ if i==var.GoOutClass])
def Pbroken_Goout():return len([i for i in range(0,len(var.class_)) if var.class_[i]==var.GoOutClass and var.car[i]==var.CarBroken]) / len([i for i in var.class_ if i==var.GoOutClass])
def Pbroken_stayhome():return len([i for i in range(0,len(var.class_)) if var.class_[i]==var.StayHomeClass and var.car[i]==var.CarBroken]) / len([i for i in var.class_ if i==var.StayHomeClass])
def Pworking_stayhome():return len([i for i in range(0,len(var.class_)) if var.class_[i]==var.StayHomeClass and var.car[i]==var.CarWorking]) / len([i for i in var.class_ if i==var.StayHomeClass])
def ClearX1X2(): var.x1,var.x2=var.Reset,var.Reset


def prediction(Input):
    GoOutArr=[]
    StayHomeArr = []
    GoOutArr.append(Pclass1())
    StayHomeArr.append(Pclass0())
    if "sunny" in Input:

        GoOutArr.append(PSunny_Goout())
        StayHomeArr.append(Psunny_stayhome())
    if "rainy" in Input:

        GoOutArr.append(Prainy_Goout())
        StayHomeArr.append(Prainy_stayhome())
    if "working" in Input:

        GoOutArr.append(Pworking_Goout())
        StayHomeArr.append(Pworking_stayhome())
    if "broken" in Input:
        GoOutArr.append(Pbroken_Goout())
        StayHomeArr.append(Pbroken_stayhome())
    #Class probability
    for i in GoOutArr : var.x1=i * var.x1
    for i in StayHomeArr: var.x2 = i * var.x2

    return print([[ "GoOut",var.x1  ],["StayHome",var.x2],ClearX1X2()][:2])


if __name__=="__main__":
    prediction(Input=["sunny","broken"])


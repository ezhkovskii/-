"""
Явный метод Эйлера с графическим интерфейсом
"""
import matplotlib.pyplot as plt
from tkinter import *

"""
Метод Эйлера
n - количество итераций, h - шаг, (x, y) - начальная точка (начальные условия Коши)
"""

#списки значений чтобы построить график
xlist = []
ylist = []
yCorList = []
def Euler():
    n=10
    h=0.1
    x=0
    y=-1
    xlist.append(x)
    ylist.append(y)
    yCorList.append(CorrectFunction(x))
    result = "\n Явный метод Эйлера\n"
    result += "%7s\t%7s\t%7s\t%7s\n" % ("x", "y", "y*", "y*-y")
 #Вывод начальных значений (x, y, Точное решение, Погрешность метода)
    result += "%7f %7f %7f %7f\n" % (x, y, CorrectFunction(x), CorrectFunction(x) - y)
    for i in range(n-1):
            y += h * Function(x, y)
            x += h
            xlist.append(x)
            ylist.append(y)
            yCorList.append(CorrectFunction(x))
            #Вывод нач. знач. по циклу
            result += "%7f %7f %7f %7f\n" % (x, y, CorrectFunction(x), CorrectFunction(x) - y)
    return result # решение


'''
Усовершенствованный метод Эйлера-Коши
'''
ylist2 = []
def EulerK():
    n=10
    h=0.1
    x=0
    y=-1
    ylist2.append(y)
    result = "\n Усовершенствованный метод Эйлера-Коши\n"
    result += "%7s\t%7s\t%7s\t%7s\n" % ("x", "y", "y*", "y*-y")
 #Вывод начальных значений (x, y, Точное решение, Погрешность метода)
    result += "%7f %7f %7f %7f\n" % (x, y, CorrectFunction(x), CorrectFunction(x) - y)
    for i in range(n-1):
            yTemp = y + h * Function(x, y)
            yPrev = y
            xPrev = x
            x += h
            for j in range(3):
                if (j == 0 ): 
                    y = yPrev + h * (Function(xPrev, yPrev)+Function(x, yTemp))/2
                else:
                    y = yPrev + h * (Function(xPrev, yPrev)+Function(x, y))/2            
            ylist2.append(y)              
            #Вывод нач. знач. по циклу
            result += "%7f %7f %7f %7f\n" % (x, y, CorrectFunction(x), CorrectFunction(x) - y)
                
    return result # решение


yRunge = []
yR = []
deltaY = []
def Runge():
    #Уточнение по Рунге
    h = 2*0.1
    n = 5
    x=0
    y=-1
    yR.append(y)
 #Вывод начальных значений (x, y, Точное решение, Погрешность метода)
    for i in range(n-1):
        yTemp = y + h * Function(x, y)
        yPrev = y
        xPrev = x
        x += h
        for j in range(3):
            if (j == 0 ): 
                y = yPrev + h * (Function(xPrev, yPrev)+Function(x, yTemp))/2
            else:
                y = yPrev + h * (Function(xPrev, yPrev)+Function(x, y))/2
        yR.append(y)

    i = 0
    for k in range(n*2):
        if ( k%2 == 0):
            deltaY.append((ylist2[k]-yR[i])/(2**2-1))
            i += 1

    i = 0
    for k in range(n*2):
        if ((k%2)==0):
            yRunge.append( ylist2[k] + deltaY[i] )
            i += 1
        else:
            if(k==(n*2-1)):
                yRunge.append( ylist2[k] + ((deltaY[i-1])/2) )
                break              
            yRunge.append( ylist2[k] + ((deltaY[i-1] + deltaY[i])/2) )
            
        
            

    result = "\nУточнение по Рунге\n"
    x = 0
    h = 0.1
    for elem in yRunge:
        result += "%7f  %7f\n" % (elem, CorrectFunction(x) - elem)
        x += h
    return result

        
        
            


"""
Функция первой производной
"""
def Function(x, y):
    return (-3 * y * x + 8 * y - x**2)/(x**2 - 5 * x + 6)


"""
Точное решение 
"""
def CorrectFunction(x):
    return (-(1/4) * x**4 + (2/3) * x**3 + 12)/((x-2)*(x-2)*(x-3))



def ShowGUI(text):
    w = 500
    h = 300
    root = Tk()
    #root.geometry('600x400')
    root.title("Численные методы")
    #вывод решения оду
    frame1=Frame(root)
    lbl=Label(frame1,text=text)
    frame1.pack()
    lbl.pack(side='top')

    #вывод графика
    plt.plot(xlist, ylist, xlist, yCorList, xlist, ylist2,xlist,yRunge) #Построение графиков
    plt.text(0.1, -0.3, 'Метод Эйлера', color = 'blue') #подписи
    plt.text(0.1, -0.45, 'Усовершенствованный метод Эйлера-Коши', color = 'green')
    plt.text(0.1, -0.6, 'Точное решение', color = 'orange')
    plt.text(0.1, -0.75, 'Уточнение по правилу Рунге', color = 'red')
    plt.xlabel('x') #Метка по оси x в формате
    plt.ylabel('y') #Метка по оси y в формате 
    plt.title('') #Заголовок в формате 
    plt.grid(True) #Сетка
    plt.show() #Показать график
    
    root.mainloop()

 

ShowGUI(Euler()+EulerK()+Runge())


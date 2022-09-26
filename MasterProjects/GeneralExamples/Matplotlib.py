from matplotlib import pyplot as plt
import numpy as np
from matplotlib import dates as mpl_dates
from datetime import  datetime,timedelta

def create_plot():

    #print(plt.style.available)  Some built-in styiles can be used
    plt.style.use("dark_background")

    x = np.array([1, 5 , 10, 15 ,20, 25, 30])
    y1 = np.random.randint(100,150,7)
    y2 = np.random.randint(100,150,7)


    plt.plot(x,y1, label = "Label 1", color = "red", linewidth = 1, linestyle = "--")
    plt.plot(x,y2, label = "Label 2", color = "yellow", linestyle = "dotted")

    plt.title("Title")
    plt.xlabel("x label")
    plt.ylabel("y label")
    plt.legend()
    plt.grid()

    plt.show()

def bar_chart():

    #create a double bar chart

    x = np.array([1, 5, 10, 15, 20, 25, 30])
    y1 = np.random.randint(100, 150, 7)
    y2 = np.random.randint(100, 150, 7)

    indices = np.arange(x.size)
    width = .3

    plt.bar(indices,y1, label = "Label 1", width = width, color = "red")
    plt.bar(indices+width,y2, label = "Label 2", width = width, color = "#212121")

    plt.xticks(indices+width/2, x)

    plt.show()

def pie_chart():

    plt.style.use("ggplot")
    x = np.random.randint(1,100,5)
    labels = ["1","2","3","4","5"]
    explode = [0, 0, 0, 0, .2]
    colors = ["blue","green","yellow","orange","brown"]
    plt.pie(x, labels = labels,wedgeprops={'edgecolor':'#000000'}, colors = colors, explode = explode,autopct='%1.1f%%')

    plt.show()

def fill_chart():

    plt.style.use("ggplot")
    x = np.array([25, 26, 27, 28, 29, 30])
    y = np.random.randint(100,200,6)

    plt.plot(x,y)
    plt.fill_between(x,y,where=(x<28), alpha = .2, interpolate=True) #alpha is the opacity

    plt.title("Title")
    plt.show()

def create_his():

    plt.style.use("ggplot")
    x = np.array([11,12,13,22,28,24,23,45,43,42,12,32,36,37,44,45,30,35,36,47,48,49])
    bins = [10,15,20,25,30,35,40,45,50]
    avg = np.mean(x)


    plt.hist(x,bins = bins,edgecolor = 'black')
    plt.axvline(avg,color = "black")

    plt.show()

def scatter_plot():

    plt.style.use("ggplot")

    x = np.random.randint(1,20,10)
    y = np.random.randint(1,20,10)

    colors = np.random.randint(1,20,10)

    plt.scatter(x,y, c = colors, s = 50,cmap= "Oranges")
    cbar = plt.colorbar()
    cbar.set_label("Cbar")

    plt.show()

def dates():

    plt.style.use("ggplot")

    x = [
        datetime(2022,1,10),
        datetime(2022,1,15),
        datetime(2022,1,20),
        datetime(2022,1,22),
        datetime(2022,1,29),
        ]

    y = np.random.randint(1,10,5)

    plt.plot_date(x,y,linestyle = "solid")
    plt.gcf().autofmt_xdate()
    plt.title("Title")
    formatted_date = mpl_dates.DateFormatter("%d %b")
    plt.gca().xaxis.set_major_formatter(formatted_date)

    plt.show()

def subplots():

    plt.style.use("ggplot")

    fig, (ax1,ax2) = plt.subplots(nrows = 2, ncols = 1, sharex=True)
    fig2, axb = plt.subplots()


    x = [1, 5, 10, 15, 20]
    y = np.random.randint(1,100,5)

    ax1.plot(x,y)
    ax1.set_title("Title 1")
    ax2.plot(x, y)


    axb.plot(x,y)
    axb.set_title("Title 2")

    plt.show()


def main():
    #create_plot()
    #bar_chart()
    #pie_chart()
    #fill_chart()
    #create_his()
    #scatter_plot()
    #dates()
    subplots()

if __name__ == "__main__":
    main()

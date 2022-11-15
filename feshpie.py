import matplotlib.pyplot as plt

def fesh_pie(labels, values, title, explode=False, legend=True, donut=True):
    """
    Make a pie plot with custom values
    - labels: array of strings or numbers with same length as values
    - values: array of numbers with same length as labels
    - title. str./number title of the chart
    - explode: bool. explode a part of the pie or not
    - legend: bool. add a legend or not.
    - donut: bool. make the pied chart a donut.
    """
    metric = [0 for line in labels] #for explode properties

    if explode and legend:
        metric[1] = 0.1 #explode last item
        explode = tuple(metric)
        plt.pie(values, labels = None, explode=explode, autopct='%1.1f%%', pctdistance=0.9, shadow=True, startangle=140)
        plt.legend(labels)
        #push the legend out
        plt.legend(labels, bbox_to_anchor=(1.1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    elif legend and not explode:
        plt.pie(values, labels = None, autopct='%1.1f%%', pctdistance=0.9, shadow=True, startangle=140)
        plt.legend(labels)
        #push the legend out
        plt.legend(labels, bbox_to_anchor=(1.1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)
    elif not legend and explode:
        metric[1] = 0.1
        explode= tuple(metric)
        plt.pie(values, labels = labels, explode=explode, autopct='%1.1f%%', pctdistance=0.9, shadow=True, startangle=140)
    else:
        plt.pie(values, labels = labels, autopct='%1.1f%%', pctdistance=0.9, shadow=True, startangle=140)
    
    plt.axis('equal')
    plt.suptitle(title, size=16, y=1) #Add space between title and plot      
    
    if donut:
        #Add a circle at the center to transform it in a donut chart
        my_circle=plt.Circle( (0,0), 0.6, color='white')
        p=plt.gcf()
        p.gca().add_artist(my_circle)

    plt.show()

#Example
labels = ["Peter Obi", "Atiku Abubakar", "Mr Ibu", "Bola Tinubu", "Lastus Yakamo"]
values = [90, 19, 100, 20, 1]
title = "This is a title"

fesh_pie(labels, values, title, legend=False, explode=True)

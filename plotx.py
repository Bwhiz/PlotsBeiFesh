import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns
from pandas import DataFrame

def plotx(df, x, y, xlabel=None, ylabel=None, title=None, xticks_range=False, values=None, rotation=None,
         kind=None, decimals=',.0f'):
    """
    This plot is intended to play with pandas dataframes
    Plot a bar chart from a dataframe usind seaborn with bars annotated with values
    -Deps: import seaborn as sns
    """
    
    if (xticks_range and not values) or (values and not xticks_range):
        return f"We will need the values in order to set the xticks_range and vice versa."
    
    try:
        plt.figure(figsize=(20,5))
        #Make the kind of plot specified in 'kind'
        if kind == 'both':
            plots = sns.barplot(x=x,y=y, data=df)
            plots = sns.lineplot(x=x,y=y, data=df)
        elif kind == 'line':
            plots = sns.lineplot(x=x,y=y, data=df)
        else:
            plots = sns.barplot(x=x,y=y, data=df)
            
        if xticks_range and values and rotation:
            plt.xticks(range(xticks_range), values)
            plt.xticks(rotation=rotation)

        elif rotation:
            plt.xticks(rotation=rotation)

        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if title:
            plt.title(title)

        for bar in plots.patches:
            plots.annotate(format(bar.get_height(), decimals),
                       (bar.get_x() + bar.get_width() / 2,
                        bar.get_height()), ha='center', va='center',
                       size=10, xytext=(0, 8),
                       textcoords='offset points')
        plt.show()
    except Exception as e:
        print(f"Error while making your plot...:\n{e}")

#Example
df = DataFrame()
df["dates"] = ["2022-11-01", "2022-11-02", "2022-11-03", "2022-11-04", "2022-11-05", "2022-11-06", "2022-11-07"]
df["purchases"] = [100, 150, 200, 250, None, 200, 220]
title = "What a Title!"
plotx(df, 'dates', 'purchases', rotation='45', title=title)
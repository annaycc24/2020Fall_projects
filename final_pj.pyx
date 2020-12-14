import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def separate_data(data, year: int) -> pd.DataFrame:
    """
    Separate and get the data by a given year
    :param data: indicateing which country's data we want to separate
    :param year: indicateing we need the data from which year
    :return: a new data frame from a given year
    >>> d = {"year": [2019, 2020], "country": ["US", "US"], "cases": [12, 34]}
    >>> df = pd.DataFrame(d)
    >>> separate_data(df, 2020)["year"][1]
    2020
    >>> separate_data(df, 2019)
       year country  cases
    0  2019      US     12
    >>> d = {"year": [2018, 2020, 2020], "country": ["UK", "UK", "UK"], "cases": [10, 24, 3]}
    >>> df = pd.DataFrame(d)
    >>> separate_data(df, 2020)
       year country  cases
    1  2020      UK     24
    2  2020      UK      3
    """

    data_new = data.loc[data["year"] == year]
    return data_new


cpdef void plot_graph3(country: pd.DataFrame, startyear: int, currentyear:int):
    """
    Create plot for the hypothesis 3
    :param country: the country's data we need
    :param startyear: the first plot is from the data in startyear
    :param currentyear: the last plot is from the data in currentyear
    :return: None
    """
    plot_data = []
    flucase = []
    cdef int i
    for i in range(startyear, currentyear + 1):
        plot_data.append(separate_data(country, i))

    # extract data from specific year
    for i in range(len(plot_data)):
        flucase.append(plot_data[i]["flu cases"])

    fig, ax1 = plt.subplots()
    plt.title('the num. of flu cases in '+country["country"][0] + ' in '+str(startyear)+'-'+str(currentyear))
    plt.xlabel('month')
    cdef int time=plot_data[0]['month']
    cdef int time20=plot_data[-1]['month']
    plt.xticks(np.arange(min(time), max(time)+1, 1.0))
    ax1.set_ylabel('num. of cases', color='black')

    for i in range(len(flucase) - 1):
        if i == 0:
            plt.plot(time, flucase[i], color='grey',label=str(startyear)+'~'+str(currentyear))
        else:
            plt.plot(time, flucase[i], color='grey')

    plt.plot(time20, flucase[-1], color='red',label='2020(with mask)')

    plt.axvline(x=4,label='April')
    if country["country"][0]=='UK':
        plt.axvline(x=6,color='orange',label='June')
        plt.text(4.3           ,7500,'2 months',fontsize=9 ,
                 bbox=dict(boxstyle="larrow,pad=0.3", fc="cyan", ec="b", lw=2))
    if country["country"][0]=='US':
        plt.axvline(x=7,color='orange',label='July')
        plt.text(4.5,45000, '3 months' , fontsize=13,
                 bbox=dict(boxstyle="larrow,pad=0.3", fc="cyan", ec="b", lw=2))



    plt.legend(loc="upper right")

    plt.show()
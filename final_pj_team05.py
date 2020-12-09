import pandas as pd
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
import doctest
# data source:
# TODO: function to read csv
# put csv in "__init__ main" to execute
def load_flu_file(file: str) -> pd.DataFrame:
    """
    Load flu data
    :param file: the name of the file
    :return: a flu data in a data frame format
    """
    flu_df = pd.read_csv(file, header = 2)
    # print(flu_df)
    return flu_df

# data source: https://trends.google.com/trends/explore?date=2019-01-01%202020-10-27&geo=US&q=mask
# TODO: function to analyze mask google trend
# read and clean
def load_mask_file(file: str) -> pd.DataFrame:
    """
    Load mask search trend data
    :param file: the name of the file
    :return: a mask search trend data in a data frame format
    """
    new_header = ['Date', 'mask_interested_in_percentage']
    mask_df = pd.read_csv(file, header = 1, names = new_header)
    return mask_df


def get_covid_cases(country_name: str, data) -> pd.Series:
    """
    Get the new covid cases of each month in a given country's data.
    :param country_name: a string of a country name
    :return: a Pandas Series contained year-month and the sum of the new cases
    >>> df = pd.DataFrame({'year': [2020, 2020, 2020, 2020],\
                   'month': [8, 8, 7, 5],\
                   'day': [4, 5, 23, 7]})
    >>> df1 = pd.to_datetime(df)
    >>> df2 = pd.DataFrame({"dateRep": df1, "cases": [3, 6, 5, 23], "countriesAndTerritories": ["China", "China", "China", "United_Kingdom"]})
    >>> df2.to_excel("test.xlsx", index = False)
    >>> d = pd.read_excel('test.xlsx')
    >>> get_covid_cases("China", d)
    yearmonth
    2020-07-01    5
    2020-08-01    9
    Name: cases, dtype: int64
    """

    if country_name == "US":
        country_name = "United_States_of_America"
    elif country_name == "UK":
        country_name = "United_Kingdom"
    country = data.loc[data["countriesAndTerritories"] == country_name]
    # country_new = country.groupby(["year", "month"]).sum()["cases"]
    # print(df)
    country["yearmonth"] = country["dateRep"].map(lambda dt: dt.replace(day=1))
    country_new = country.groupby(["yearmonth"]).sum()["cases"]
    return country_new


def get_total_flu_case_by_month(file: pd.DataFrame) -> pd.Series:
    """
    Get the total flu case of every month
    :param file: file of flu data
    :return: a Pandas Series contained year-month and the sum of the flu cases by month
    >>> d = {"EDATE":['2015-01-04', '2015-01-11', '2015-01-18'], "ALL_INF":(2400, 3314, 3319)}
    >>> df = pd.DataFrame(data=d)
    >>> get_total_flu_case_by_month(df)['2015-01-01']
    9033
    >>> d2 = {"EDATE":['2020-11-01', '2020-11-08', '2020-11-15', '2020-11-22'], "ALL_INF":(9, 5, 15, 12)}
    >>> df2 = pd.DataFrame(data=d2)
    >>> get_total_flu_case_by_month(df2)['2020-11-01']
    41
    """

    file["yearmonth"] = pd.to_datetime(file["EDATE"]).map(lambda dt: dt.replace(day=1))
    file_new = file.groupby(["yearmonth"]).sum()["ALL_INF"]
    return file_new

def get_mask_search_trend_by_month(file: pd.DataFrame) -> pd.Series:
    """
    Get the mean mask search trend of every month
    :param file: file of the mask search trend data
    :return: a Pandas Series contained year-month and the mean of the mask search trend by month
    """

    file["yearmonth"] = pd.to_datetime(file["Date"]).map(lambda dt: dt.replace(day=1))
    file_new = file.groupby(["yearmonth"]).mean()["mask_interested_in_percentage"]
    return file_new

# aggregrate everything by country
# columns: year, month, mask, flu, covid
def aggregrate_data(flu_data: pd.Series, mask_data: pd.Series, covid_cases:pd.Series, country_name: str) -> pd.DataFrame:
    """
    Combine all the data we need in a new data frame
    :param flu_data: flu data we extracted and group by year and month
    :param mask_data: mask search trend we got, which are grouped by year and month
    :param: covid_cases: covid cases we got, which are grouped by year and month
    :param country_name: name of the country indicating which data we are going to use
    :return: a new data frame with all the useful data we need
    """
    merge = pd.concat([flu_data, mask_data, covid_cases], axis = 1).reset_index()
    merge["year"] = merge["yearmonth"].dt.year
    merge["month"] = merge["yearmonth"].dt.month
    merge["country"] = country_name
    merge = merge[["year", "month", "yearmonth", "country", "ALL_INF", "mask_interested_in_percentage", "cases"]]
    merge = merge.rename(columns = {"ALL_INF": "flu cases"})
    return merge


def extract_info(country: str, data) -> pd.DataFrame:
    """
    Extract useful information from a given country name
    :param country: country name that we want to get data from
    :return: a new data frame with all the useful data we need
    """
    flu = "FluNetInteractiveReport_" + country + ".csv"
    mask = "multiTimeline_" + country + ".csv"

    fludata = load_flu_file(flu)
    mask_trend = load_mask_file(mask)
    fludata_new = get_total_flu_case_by_month(fludata)
    mask_trend_new = get_mask_search_trend_by_month(mask_trend)
    covid_case = get_covid_cases(country, data)
    # print(fludata_new)
    result_data = aggregrate_data(fludata_new, mask_trend_new, covid_case, country)
    # print(type(fludata))
    return result_data


def separate_data(data, year: int) -> pd.DataFrame:
    """
    Separate and get the data by a given year
    :param data: indicateing which country's data we want to separate
    :param year: indicateing we need the data from which year
    :return: a new data frame from a given year
    >>> separate_data(us, 2020).values[1][0]
    2020
    """

    data_new = data.loc[data["year"] == year]
    return data_new


# Data visualization
def plot_graph(country: pd.DataFrame, startyear: int, currentyear: int, status: int):
    """
    Create plots for hypothesis one and two
    :param country: the country's data we need
    :param startyear: the first plot is from the data in startyear
    :param currentyear: the last plot is from the data in currentyear
    :param status: which kind of plot we need(ex: status = 1: plots for the hypothesis 1)
    :return: None
    """
    for year in range(startyear, currentyear + 1):

        plot_data = separate_data(country, year)  # extract data from specific year
        covidcase = plot_data['cases']
        flucase = plot_data['flu cases']
        mask_trend = plot_data["mask_interested_in_percentage"]
        fig, ax1 = plt.subplots()
        plt.title(country["country"][0] + str(year))
        plt.xlabel('month')
        time = plot_data['month']
        plt.xticks(np.arange(min(time), max(time) + 1, 1.0))
        ax2 = ax1.twinx()

        if status == 1:
            yaxis_ax1 = flucase
            yaxis_ax2 = mask_trend
            ax1.set_ylabel('num. of cases', color='black')
            ylabel_ax2 = 'mask trend'
            ax2.set_yticks(range(1, 101, 10))
            ax2.set_ylim([1, 100])
        elif status == 2:
            yaxis_ax1 = covidcase
            yaxis_ax2 = flucase
            ax1.set_ylabel('num. of covid cases', color='black')
            ylabel_ax2 = 'num. of flu cases'

        ax1.plot(time, yaxis_ax1, color='black')
        ax2.set_ylabel(ylabel_ax2, color='red')
        ax2.plot(time, yaxis_ax2, color='red')
        ax1.tick_params(axis='y', labelcolor='black')
        ax2.tick_params(axis='y', labelcolor='red')
        fig.tight_layout()

        plt.show()

def plot_graph3(country: pd.DataFrame, startyear: int, currentyear:int):
    """
    Create plot for the hypothesis 3
    :param country: the country's data we need
    :param startyear: the first plot is from the data in startyear
    :param currentyear: the last plot is from the data in currentyear
    :return: None
    """
    plot_data = []
    flucase = []
    for i in range(startyear, currentyear + 1):
        plot_data.append(separate_data(country, i))

    # extract data from specific year
    for i in range(len(plot_data)):
        flucase.append(plot_data[i]["flu cases"])

    fig, ax1 = plt.subplots()
    plt.title('the num. of flu cases in '+country["country"][0] + ' in '+str(startyear)+'-'+str(currentyear))
    plt.xlabel('month')

    time=plot_data[0]['month']
    time20=plot_data[-1]['month']
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

if __name__ == "__main__":
    # data source: https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide
    # function to analyze covid case
    # read and clean

    covid = pd.read_excel('COVID-19-worldwide.xlsx')
    # covid.groupby(["year", "month"]).sum()["cases"]
    china = extract_info("China", covid)
    us = extract_info("US", covid)
    uk = extract_info("UK", covid)

    us_graph2019 = plot_graph(us, 2019, 2020, 1)
    uk_graph2019 = plot_graph(uk, 2019, 2020, 1)
    china_graph2019 = plot_graph(china, 2019, 2020, 1)

    us_graph2019 = plot_graph(us, 2020, 2020, 2)

    uk_graph2019 = plot_graph(uk, 2020, 2020, 2)

    china_graph2019 = plot_graph(china, 2020, 2020, 2)

    us_graph3 = plot_graph3(us, 2015, 2020)
    china_graph3 = plot_graph3(china, 2015, 2020)
    uk_graph3 = plot_graph3(uk, 2015, 2020)
# 2020Fall_projects
Presentation Link: https://youtu.be/ozZB7kaQOQk  
  
Title: The Spreading of Influenza with Worldwide Masks Required  
Project Type: Type II Projects  
Instructor: Mr. John Weible  
Group: Team 05  
Team Members:
- Enshi Wang (enw12) 664221142  
- Vivian Liao (yhliao4) 661311697
- Cheng Chen Yang (ccy3) 657920840
# Contribution
We worked together via zoom discussion and each of us handled one hypothesis. We collected data and completed doctests together.
- Cheng-Chen Yang:  
Extracted the information we need from the specific data to a new data frame.
- Vivian Liao:  
Loaded data of flu cases, covid cases, and mask searching trend to the file, and made the plots for the hypothesis 2.
- Enshi Wang:   
Collected data and made the plots for hypothesis one and hypothesis three.

# Research Background
During the covid-19 pandemic, wearing a mask is recommended or required in many countries. Since influenza has a very similar way of spreading, we want to know how the masks could influence the spreading of influenza. Intuitionally, people tend to take off the masks if the increase of new cases of covid-19 could slow down, but this might affect the spreading of influenza. The datasets were obtained from WHO and Google Trend which could help us find the relationship between the covid-19 and influenza.

# Hypothesis
1) During the pandemic, the global influenza cases may decrease, because people wear face masks everywhere.  
2) In countries where the COVID-19 is abating, the confirmed cases of influenza may be increased, since people start not to wear face masks.  
3) The peak of the spread of influenza may delay due to the pandemic since people wear masks.  

# Data Source
- The google trend of mask in the US:  
https://trends.google.com/trends/explore?date=2019-01-01%202020-10-27&geo=US&q=mask  
  
- The google trend of mask(口罩) in China:  
https://trends.google.com/trends/explore?date=2019-01-01%202020-10-27&geo=CN&q=%E5%8F%A3%E7%BD%A9  
  
- The google trend of mask in UK:  
https://trends.google.com/trends/explore?date=2019-01-01%202020-10-27&geo=GB&q=mask  
  
- The influenza data of US,UK and China between 2015-2020:  
https://apps.who.int/flumart/Default?ReportNo=12  
 
- The daily number of new reported cases of COVID-19 by country worldwide:
https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide
  
# Research Methods
### Hypothesis 1 
Analysis:  
The amount of flu cases for each country during the pandemic is much less than the previous year.  
 
In the US, the mask search trend keeps low in 2019, and the flu cases surged during the
first 3 months. In 2020, the peak occurred in February and decreased dramatically with the mask trend going up.  
 
In China, the number of flu cases generally decreased during the first 3 quarters due to higher temperature and the mask trend is extremely low. In 2020, the cases decreased at the beginning of the year with a high mask trend.  

In the UK, the number of flu cases shows a similar pattern to the US in 2019. In 2020, with the mask trend keeping high, the flu cases decreased at the beginning of the year and got nearly 0 in April. 

The result shows that the masks have great effects on reducing the cases of influenza in 2020.


<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h1_US_19.png?raw=true" width="450" />  
The total flu cases in 2019 in the US is 268524.  
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h1_US_20.png?raw=true" width="450" />  
The total flu cases in 2020 in the US is 228600.  
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h1_C_19.png?raw=true" width="450" />  
The total flu cases in 2019 in China is 122757.  
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h1_C_20.png?raw=true" width="450" />  
The total flu cases in 2020 in China is 31051.  
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h1_UK_19.png?raw=true" width="450" />  
The total flu cases in 2019 in UK is 42447.  
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/%20h1_UK_20.png?raw=true" width="450" />  
The total flu cases in 2020 in UK is 14046.  
  
  
### Hypothesis 2
Analysis:  
From the graphs, we can see that although the COVID-19 is abating in China, the influenza case does not increase even in November 2020 
when the temperature is pretty low. It may be that people are aware of the pandemic outside their country and they still wear masks. For the US and the UK, masks are 
still required in the public area due to the pandemic.

We can not prove the hypothesis 2 is true.   
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h2_US_20.png?raw=true" width="450" />
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h2_UK_20.png?raw=true" width="450" />
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h2_C_20.png?raw=true" width="450" />  
  
 
### Hypothesis 3  
Analysis:  
We then studied the influence of masks on the duration of influenza. We found that the number of cases decreases earlier with masks in 2020. 
In the three countries, the number of new cases decreased to 0 in April.   
In the US, it is 3 months earlier than normal.  

In the UK, it is 2 months earlier than normal.  

It is also the earliest month in China in the recent 5 years.     

The finding strongly indicates that masks could shorten the duration of influenza, 
which provides positive evidence to support our hypothesis 3.
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h3_US.png?raw=true" width="450" />
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h3_UK.png?raw=true" width="450" />
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h3_C.png?raw=true" width="450" />
  


# Conclusion
Our outcome supports hypothesis 1 and has strong evidence for hypothesis 3. The global flu cases decrease because people are more likely to wear masks during the pandemic. Moreover, the peak of the flu would delay because people wear masks.  

However, our result does not support our hypothesis 2. What we expected is that the countries with only a few new cases each day would have an increase of flu cases because people are optimistic about the pandemic and tend to not wear masks. From our research, the flu cases in China didn't increase even the pandemic is abating. It might be people are more aware of the situation and remain wearing masks even the pandemic isn't serious now.
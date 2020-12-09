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
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h1_US_19.png?raw=true" width="450" />
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h1_US_20.png?raw=true" width="450" />
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h1_C_19.png?raw=true" width="450" />
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h1_C_20.png?raw=true" width="450" />
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h1_UK_19.png?raw=true" width="450" />
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/%20h1_UK_20.png?raw=true" width="450" />
  
The flu cases from each country during the pandemic are less than the previous year. In the previous year, the mask search trend did not change a lot, so the flu cases were more related to the weather.
In 2020, although they still seem like related to the weather, we can check the flu cases in the beginning of the year.
Apparently, when the mask searching trend goes up, the flu cases decrease obviously.  
### Hypothesis 2  
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h2_US_20.png?raw=true" width="450" />
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h2_UK_20.png?raw=true" width="450" />
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h2_C_20.png?raw=true" width="450" />  
  
From the plot based on China’s influenza and COVID data in 2020, we can see that although the COVID-19 is abating, the influenza case does not increase.
It may because people are still aware of the pandemic outside their country.  
### Hypothesis 3  
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h3_US.png?raw=true" width="450" />
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h3_UK.png?raw=true" width="450" />
<img src="https://github.com/yihsuanliao/2020Fall_projects/blob/main/plot/h3_C.png?raw=true" width="450" />
  
We found that we cannot study the possible delay of the peak month since the peak occurs in winter but we do not have these data for the year of 2020.
We then studied the influence of masks to the influenza. We found that the number of cases decreses eariler with masks in 2020. 
In the three countries, the number of new cases decreased to 0 in April, which is 3 months earlier than normal in the US; 
2 months earlier than normal in UK; and also the earliest month in China among the years we studied. 
The finding strongly indicates that masks could shorten the duration of influenza, which is a positive evidence to support our hypothesis.

# Conclusion
Our outcome supports hypothesis 1 and hypothesis 3. The global flu cases decreases because people are more likely to wear masks during pandemics. Moreover, the peak of the flu would delay because people are wearing masks.  
However, our result does not support our hypothesis, countries where COVID-19 cases are decreasing supposed to increase flu cases because people are optimistic with the pandemic and tend to not wear masks. From our research, the flu cases in China didn't increase even the pandemic is abating. It might be people are more aware of the situation and remain wearing mask even the pandemic isn't serious now.

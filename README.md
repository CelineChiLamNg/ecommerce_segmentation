# Ecommerce Segmentation Analysis
*Celine - 2025*

## Objective 
For the purpose of this project, let's imagine this data was collected by a
small regional shopping site with both online and physical stores. The task 
is to apply RFM segmentation method to help  
identify high-value customer segments and understand their
demographics and behavior. With the goal of personalizing marketing
strategies that increase customer engagement, loyalty, and revenue.
Answering main questions like:
- Who are our best customers?
- How can we reach them better?

## Data 
This dataset was obtained from
[Kaggle](https://www.kaggle.com/datasets/salahuddinahmedshuvo/ecommerce-consumer-behavior-analysis-data?resource=download),
in April 2025. This data contains 1000 rows and 28 columns including
information on purchasing patterns, demographics, product preferences,
customer satisfaction, and more.


## Technology Used
1. Python
2. Pandas
3. Matplotlib
4. Seaborn
5. Google Sheets
6. PowerBI


## Results

RFM analysis in [Google Sheets](https://docs.google.com/spreadsheets/d/1XJ93vgaaLXZJuY4I7Avh4-zQIvFcPu0qcsWSmEUVSsU/edit?usp=sharing)
</br>PowerBI dashboard in [pdf](https://drive.google.com/file/d/1B4mSj_4IcPPq9nLoHhVHgDqbzOUf4kAE/view?usp=sharing)
</br></br>
After RFM, 26% of customers are Top, Solid, and Regular customer combined, and 
20% are 
customers
who used to be frequent high spenders, with the rest being low value
spenders.

**Business strategy for each segment**<br>
1. Top + Solid → Retain
2. Regular → Upsell
3. Can't lose + At risk → Recover

These 5 segments cover the 46.3% of customers who are/were frequent high
value customers. Other segments were not further analyzed as they were not 
as relevant for this case.


## Challenges & Learnings
While applying the RFM segmentation method in Google Sheets, I initially 
chose an approach that I only later realized wasn't ideal when revisiting 
the project.

1. I started by calculating each RFM score using percentiles, creating 5 
bins to assign scores.

2. Later, I realized I could have used PERCENTRANK, which assigns scores 
   based on 
rank and handles duplicates more consistently. It also emphasized 
   how values compared to each other, rather than percentile thresholds.

One thing I did well: instead of summing R, F, and M into a single final 
score, I kept Recency and Frequency & Monetary separate. This added an extra dimension to better understand different customer behaviors.



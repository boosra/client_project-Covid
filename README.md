# Project Name: Infected Tweets -- Analysis of Randomly Sampled Tweets to Determine COVID-19 Subject Matter  
  
### Problem Statement:  
When the COVID-19 pandemic is running rampant, current information is paramount for staying safe. Graphs and models are created daily, producing figures relied on by hospitals and government agencies. Although this data is official, it does not tell the entire story of outbreak impact. On social media, specifically Twitter, people are talking about their experience with COVID-19, potentially indicating COVID impact sites before they become apparent medically.

As a team of data scientists working for New Light Technologies, we are tasked with creating a model that can dynamically classify Tweets as COVID-related. To solve this unsupervised learning problem we will train a w2v vectorizer on COVID-19 related tweets and use the weights of those words in a DBscan cluster. We will then check the Tweet clusters to assess relationships, and determine which clusters are our targets and where the Tweets originated from.

### Executive Summary  
Our data was pulled from Twitter using the twitterscraper Python library and a custom wrapper function. We prepared two datasets separately, one with high bias based on targeted terms to get 100k tweets specifically related to COVID-19, and one with high variance using 50 randomly generated terms to get 200k "random" sampling of Tweets, then combined the bias and variance sets to create a final testing set. We additionally ran the two datasets through two cleaners, one to purge duplicate tweets that may have been caught multiple times during the query process, and one to remove common stopwords from the tweet text.  
  
Once our datasets were gathered, we ran a word2vec vectorizer on every word in the corpus. Using that guidance, we then ran a word2vec vectorizer on each Tweet, and then used those vectors in a DBScan model to determine clusters that were related to personal COVID tweets (our identification target), tweets about COVID (such as news tweets, or tweets about political figures central to the COVID response), and noise or other clusters our model decided to create. We used a K-means clusterizer in the early stages of our modeling, but since we didn't know how many clusters we were targeting with our larger sets, we couldn't properly use the model anymore.   
  
Our final model was able to successfully determine our target as Cluster 0, though there were some patterns that showed up that with more optimization we could likely remove. For example, our model created unique clusters for spam tweets (unique tweets of copy-and-pasted text), that for all intents and purposes are duplicates but which our cleaner didn't catch because each one had a unique Tweet ID. The data collection tool includes geolocation functions that we didn't utilize fully in this proof-of-concept, but those tools if utilized correctly could allow this model to be scaled from a municipality all the way to national level.  
  
### Table of Contents:  
 - **[Problem Statement](#Problem-Statement)**.
 
 - **[Executive Summary](#Executive-Summary)**.  
   
 - **[Data Dictionary](#Data-Dictionary)**.
   
 - **[Project Files](#Project-Files)**.   

- **[Conclusions and Recommendations](#Conclusions-and-Recommendations)**.  

- **[References](#References)**.

### Data Dictionary:  
| Data Name | Data Type | Description |
|---|---|---|
| tweet_id | int64 | The unique identifier of a given tweet. |
| username | object | The username of the tweet's poster. |
| text | object | The text of the tweet. |
| tweet_date | object | The date the tweet was posted. |
| search_term | object | The term being queried when the tweet was scraped. |  
| city | object | The city or area corresponding to the lat/long coordinates used in the query that yielded the tweet. |  
| lat | float64 | Latitude coordinate used during the query. |  
| long | float64 | Longitude coordinate used during the query. |  
| radius | object | The radius around the lat/long point used during the query. |  
| query_start | object | The date used in the query. The scraper then works in 3-day increments from the query_start date to the present date. |
| token_text | object | The tokenized version of the text column. |  
| stop_text | list | The tokenized text with stopwords removed. |  
| cluster | int64 | The DBScan cluster the tweet was assigned to. |  
  
### Project Files:
Here is the workflow order to follow when running through the notebooks, which can be found in the code folder:  
1) Run TwitterScraperP5.ipynb. This is a modified version of the script we wrote that removes most user prompt inputs to run faster.
2) Run MainNotebook.ipynb. This notebook will import the datasets from the TwitterScraperP5 and model them.
  
#### Datasets:  
1) Full_dataset.csv is the concatenated "high variance" dataset.  
2) scrape_5.12.csv is the initial high-bias dataset generated from targeted terms.  
3) test_5.14.csv is the maximum-variance dataset generated from random words.  
  
### Conclusion and Recommendations:  
Thus Social media posts can be used to determine whether or not covid is in an are.  
This unsupervised data set can be clustered and assessed  
- Word2Vec Cosine Similar words  
- Weighted Tweet Vectorizer  
- DBscan autonomous clustering  
Using this process we can:  
- Separate covid tweets from any area  
- Determine severity of outbreak  
- Concentration of covid tweets  
- Heatmap the locations of virus hotspots  
Make a world a better place!  
  
### References:  
[COVID-19 Molecule](https://www.statnews.com/2020/02/11/disease-caused-by-the-novel-coronavirus-has-name-covid-19/)  
[Word2Vec Image](https://hackernoon.com/word2vec-part-1-fe2ec6514d70)  
[Black Twitter bird Image] (https://webstockreview.net/explore/twitter-bird-png-transparent/)
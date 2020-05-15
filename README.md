# Project Name: Infected Tweets -- Analysis of Randomly Sampled Tweets to Determine COVID-19 Subject Matter  
  
## Table of Contents
### Team:
### Problem Statement  
When the COVID-19 pandemic is running rampant, current information is paramount for staying safe. Graphs and models are created daily, producing figures relied on by hospitals and government agencies. Although this data is official, it does not tell the entire story of outbreak impact. On social media, specifically Twitter, people are talking about their experience with COVID-19.  
  
As a team of data scientists working for the CDC, we are tasked with creating a model that can dynamically classify Tweets as COVID-related. To solve this unsupervised learning problem we will train a w2v vectorizer on COVID-19 related tweets and use the weights of those words in a DBscan cluster. We will then check the Tweet clusters to assess relationships, and determine which clusters are our targets.  
  
### Executive Summary  
Our data was pulled from Twitter using the twitterscraper Python library and a custom wrapper function. We prepared two datasets separately, one with high bias based on targeted terms to get 100k tweets specifically related to COVID-19, and one with high variance using 50 randomly generated terms to get 200k "random" sampling of Tweets, then combined the bias and variance sets to create a final testing set. We additionally ran the two datasets through two cleaners, one to purge duplicate tweets that may have been caught multiple times during the query process, and one to remove common stopwords from the tweet text.  
  
Once our datasets were gathered, we ran a word2vec vectorizer on every word in the corpus. Using that guidance, we then ran a word2vec vectorizer on each Tweet, and then used those vectors in a DBScan model to determine clusters that were related to personal COVID tweets (our identification target), tweets about COVID (such as news tweets, or tweets about political figures central to the COVID response), and noise or other clusters our model decided to create. We used a K-means clusterizer in the early stages of our modeling, but since we didn't know how many clusters we were targeting with our larger sets, we couldn't properly use the model anymore.   
  
Our final model was able to successfully determine our target as Cluster 0, though there were some patterns that showed up that with more optimization we could likely remove. For example, our model created unique clusters for spam tweets (unique tweets of copy-and-pasted text), that for all intents and purposes are duplicates but which our cleaner didn't catch because each one had a unique Tweet ID. The data collection tool includes geolocation functions that we didn't utilize fully in this proof-of-concept, but those tools if utilized correctly could allow this model to be scaled from a municipality all the way to national level.  
  
### Project Files
Here is the workflow order to follow when running through the notebooks, which can be found in the code folder:  
-

### Data Dictionary:  
  
### Conclusion and Recommendation 
### Reference 

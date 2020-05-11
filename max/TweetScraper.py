#Import requisite modules
import sys
import pandas as pd
import numpy as np
import datetime
from os import path #Library module for .csv file check
from twitterscraper import query_tweets #if you haven't installed this module, run 'pip install twitterscraper' in your notebook
#---------------------------------------------------------------------
query_list = [ #This is our sample list, add or subtract as you see fit!
    'COVID',
    'COVID-19',
    'Corona',
    'Coronavirus',
    'Rona',
    'Quarantine',
    '#COVID',
    '#COVID-19',
    '#quarantine',
    '#Quarantine',
    '#covid19'
]
#--------------------------------------------------------------------
#Credit to Danielle Medellin, DSI11-NYC for the below implementation of custom parameter dictionary support
custom_params = {'Houston':{'city' : 'Houston',
                         'lat'  : 29.760427,
                         'long' : -95.369804,
                         'radius': '15mi',
                         'queries' : ['rona','corona','covid']},
              'Detroit': {'city' : 'Detroit',
                          'lat'  : 42.331429,
                          'long' : -83.045753,
                          'radius' : '10mi',
                         'queries': ['stonks','tom nook','animal crossing']}
             }
#--------------------------------------------------------------------
#Get tweets without geolocation
def get_tweets(query):
    tweets = {}
    count = 0 #Sets the index generator
    for tweet in query_tweets(query,begindate=datetime.date(2019,12,1)):
        chirp = {}
        chirp['tweet_id'] = tweet.tweet_id
        chirp['username'] = tweet.username
        chirp['text'] = tweet.text
        chirp['tweet_date'] = tweet.timestamp
        chirp['search_term'] = query
        chirp['city'] = np.NaN #Fills columns with NaNs for data cleaning at a later point. Rather than having to replace string values
        chirp['lat'] = np.NaN #These values can be replaced with fillna.
        chirp['long'] = np.NaN
        chirp['radius'] = np.NaN
        tweets.update({count : chirp})
        count += 1
    return tweets
#--------------------------------------------------------------------
#Get tweets with geolocation
def get_tweets_geoloc(query, city, lat, long, radius): #Geolocation parameters defined by user in master function or dictionary
    tweets = {}
    count = 0
    for tweet in query_tweets(f"{query}, geocode:{lat},{long},{radius}",begindate=datetime.date(2019,12,1)):
        chirp = {} #Generates tweet dictionary by calling on generated 'tweet' object attributes
        chirp['tweet_id'] = tweet.tweet_id
        chirp['username'] = tweet.username
        chirp['text'] = tweet.text
        chirp['tweet_date'] = tweet.timestamp
        chirp['search_term'] = query
        chirp['city'] = city
        chirp['lat'] = lat
        chirp['long'] = long
        chirp['radius'] = radius
        tweets.update({count : chirp})
        count += 1 #increments index up by 1 for later dataframe implementation
    return tweets
#--------------------------------------------------------------------
#Generate dataframe from "tweets" dictionary generated after each query
def make_dataframe(dictionary):
    df = pd.DataFrame.from_dict(dictionary, orient='index')
    return df
#--------------------------------------------------------------------
#Query function using custom parameters
#Credit Danielle Medellin for this code block section
def get_query_dataframe_cp(custom_params):
    query_df = pd.DataFrame() #instantiate an empty dataframe
    for key in custom_params.keys():
        for query in custom_params[key]['queries']:
            tweets = get_tweets_geoloc(query,custom_params[key]['city'],custom_params[key]['lat'],custom_params[key]['long'],custom_params[key]['radius'])
            df = make_dataframe(tweets)
            query_df = pd.concat([query_df,df],ignore_index = True)
    return query_df
#---------------------------------------------------------------
#Query function with geolocation but no custom parameters
def get_query_dataframe_geo(list_of_queries):
    query_df = pd.DataFrame() #instantiate an empty dataframe
    for query in list_of_queries:
            tweets = get_tweets_geoloc(query,lat,long,radius)
            df = make_dataframe(tweets)
            query_df = pd.concat([query_df,df],ignore_index = True)
    return query_df
#-------------------------------------------------------------------
#Query function with no custom anything
def get_query_dataframe(list_of_queries):
    query_df = pd.DataFrame() #instantiate an empty dataframe
    for query in list_of_queries:
            tweets = get_tweets(query)
            df = make_dataframe(tweets)
            query_df = pd.concat([query_df,df],ignore_index = True)
    return query_df
#------------------------------------------------------------------
#Master function
def get_dataset():
    #Paramter switches
    custom_params_switch = input("Are you using a custom parameter dictionary?")
    export_csv_switch = input("Do you want to export the final dataframe to csv?")
    #Custom parameter switch block
    if str.lower(custom_params_switch) == 'yes':
        dataset = get_query_dataframe_cp(custom_params)
    else:
        geo_switch = input("Are you using geolocation?")
        if str.lower(geo_switch) == 'yes':
            lat = float(input("Input Latitude:")) #Converts string input latitude to float value
            long = float(input("Input Longitude:"))
            radius = input("Input radius and unit:")
            dataset = get_query_dataframe_geo(query_list, lat, long, radius)
        else:
            dataset = get_query_dataframe(query_list)
    #CSV export switch block
    if str.lower(export_csv_switch) == 'yes':
        custom_csv_name = input("Input CSV export file name:") #user input line for export name
        #Check if datasets folder exists. If not, create folder.
        #Create timestamp for unique file naming after Input
        datetime_now = datetime.now()
        timestamp = strftime("%d%b%Y%H%M%S%f")

        #Add timestamp to custom_csv_name before it is saved to file Geolocation
        custom_csv_name = custom_csv_name+"_"+timestamp

        if os.path.exists('datasets') == True:
            pass
        else:
            os.mkdir('datasets')
        #Check if file has already been created. If yes, prompt user to overwrite or make new file.
        if os.path.exists(f'datasets/{custom_csv_name}.csv') == True:
            overwrite_check = input ("File already exists--do you want to overwrite?")
            if str.lower(overwrite_check) == 'yes':
                pass #skips through checks and overwrites file name
            else:
                new_csv_name = custom_csv_name #creates new_csv_name variable = to old name
                while new_csv_name == custom_csv_name: #continues to reject file name until a unique name is created
                    new_csv_name = input("Input new output file name:")
                custom_csv_name = new_csv_name
        else:
            pass
        dataset.to_csv(f"./datasets/{custom_csv_name}.csv", index = False) #write csv to datasets folder
        print(f"Export complete, scraped {len(dataset.index)} tweets")
    else:
        return dataset

if __name__ == '__main__':
    get_dataset()

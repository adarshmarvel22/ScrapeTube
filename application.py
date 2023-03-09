from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
# from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import pymongo
# save file and import modules --> extract number is a custom function to extract the view count
import os,sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),'..')))
from utility import extract_number
# scrapetube for utube scraping and other imports
import scrapetube
from datetime import datetime
import pandas as pd
import requests

# for debugging
import logging
logging.basicConfig(filename='utube.log',level=logging.INFO, format="%(asctime)s %(name)s %(message)s")

application = Flask(__name__) # initializing a flask app
app=application

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/review',methods=['POST','GET']) # route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            logging.info("channel name")
            channel_name = request.form['content'].replace(" ","")
            # set limit of videos to scrap = 5
            limit=5

            if channel_name == "":
                return render_template("index.html")

            channel_url=f"https://www.youtube.com/@{channel_name}/videos"

            # debugging
            logging.info("Searching {} videos for {}".format(limit, channel_url))
            
            videos = scrapetube.get_channel(channel_url=channel_url, limit=limit)
            # print(next(videos))
            now = datetime.now()
            videos_data = []
            x = -1
            for video in videos:
                # extract video id
                video_id = video['videoId']
                # extract video title
                title = video['title']['runs'][x+1]['text']
                # extract thumbnail url
                thumbnail_url = video['thumbnail']['thumbnails'][-1]['url']
                view_count = extract_number(video['viewCountText']['simpleText'])
                # Extract time of posting
                post_time_text = video['publishedTimeText']['simpleText']
                # Extract video URL
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                videos_data.append((now, video_id,video_url, title,thumbnail_url,view_count,post_time_text))

                response = requests.get(thumbnail_url)

            videos_data.reverse()
            df = pd.DataFrame(videos_data, columns=['date_time', 'video_id','video_url','title','thumbnail_url','view_count','post_time_text'])

            # converting to list of dictionary/records 
            mydict=df.to_dict('records')

            # Save file
            if os.path.isfile('videos_data.csv'):
                existing_df = pd.read_csv('videos_data.csv', nrows=1)
                existing_columns = set(existing_df.columns)
                new_columns = set(df.columns)
                if existing_columns == new_columns:
                    df.to_csv('videos_data.csv', mode='a', header=False, index=False)
                else:
                    missing_columns = new_columns.difference(existing_columns)
                    raise ValueError(f"Columns {missing_columns} do not match between new DataFrame and existing csv file.")
            else:
                df.to_csv('videos_data.csv', index=False)
            
            # save to database mongoDB
            # client = pymongo.MongoClient("mongodb+srv://adarshmsd1:adarshmsd1@cluster0.zak3an8.mongodb.net/?retryWrites=true&w=majority")
            # db=client['UTubeData']
            # utube_col=db['utube_col']
            # utube_col.insert_many(mydict)
            
            data=[mydict,channel_name]
            return render_template("results.html",mydata=data)
        except Exception as e:
            print('The Exception message is: ',e)
            return render_template("error.html",msg="Something is Wrong")

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
	#app.run(debug=True)
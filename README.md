# lab-flask

<!-- ![image](https://user-images.githubusercontent.com/115451707/196919992-edcfea8b-e3f6-4f35-9398-43be66b5622d.png) -->
- The url or channel name can be hard coded but not done to make it more flexible and available
- To fix channel name , go to application.py file and replace the channel_name with the given name:
Like for example in the url:  "https://www.youtube.com/@PW-Foundation/videos" , replace channel name with "PW_Foundation"
- Enter the name of channel whose latest 5 videos content (video url, video id, datetime of scraping, date of video posted, views count, video thumbnail url) you want to scrape.
- libraries used are mentioned in the requirements.txt
- The website is hosted on Microsoft Azure 
(The link is temporarily down/not working....will fix it soon)
- Link : ```scrutube2.azurewebsites.net ```

```
You Tube Videos Scraper using Flask (Python) : ScrapeTube 1.0
```
To run flask application :
1. Install the requirements.txt file for the python libraries:
```
pip install -r requirements.txt
```
2. Run the app:
```
python application.py
```

To access your flask application open new tab in and paste the url:
```
https://{your_url}.pwskills.app:5000/
```
- Home Page: Search Channel Name
![ytHome](https://user-images.githubusercontent.com/87609950/224355814-54333778-18e5-4505-832c-3b6cbd1cf5ec.jpg)
- Results :
![yt_res1](https://user-images.githubusercontent.com/87609950/224355846-c7bb6e54-1f6e-45ed-9f3f-4ece5c41329f.jpg)
- Database :
![yt_db](https://user-images.githubusercontent.com/87609950/224382808-3792b942-743b-43f8-add0-4f9bf2d7a83c.jpg)

- according to ques:

- url: https://www.youtube.com/@PW-Foundation/videos
- input channel name: PW-Foundation
![PW-Foundation](https://user-images.githubusercontent.com/87609950/224506388-292f4021-e958-41bb-896b-4a04fb478e38.jpg)
![pwss2](https://user-images.githubusercontent.com/87609950/224506408-31e79fb9-7f9b-494a-ac05-196c0b58eb75.jpg)

data is saved in the csv file: https://github.com/adarshmarvel22/ScrapeTube/blob/main/videos_data.csv

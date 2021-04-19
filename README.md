# yahoo_finance_news_data_collection
yahoo finance news data collection using selenium and bs4

In [data collection using bs4 and selenium article](https://zzhu17.medium.com/web-scraping-yahoo-finance-news-a18f9b20ee8a), gathering article's URLs is done in a for loop and defining webdriver several times. we have used another approach: Scrolling down a page to find an element by XPATH. Therefore, we could gather 50 links.

Of course we do not claim that it's the best approach but if you suggest any better solution, please share it with us.

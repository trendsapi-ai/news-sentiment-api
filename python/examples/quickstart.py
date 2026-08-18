from trendsapi_news_sentiment import TrendsAPI

client = TrendsAPI()                    # TRENDSAPI_KEY
# client = TrendsAPI(api_key="YOUR_KEY")

series = client.get_time_series("nvidia")
print(series[-1].date, series[-1].value)

growth = client.get_growth("nvidia", percent_growth=["3M", "12M"])
print(growth.results[0].growth, growth.results[0].direction)

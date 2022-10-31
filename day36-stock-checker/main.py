from datetime import datetime, timedelta
from numpy import diff
import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.getenv('STOCK_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
PHONE_NUMBER  = os.getenv("PHONE_NUMBER")
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
# e.g. 2022-10-28
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "symbol":"TSLA",
    "apikey":STOCK_API_KEY,
    "function":"TIME_SERIES_DAILY",
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()
yst_closing_stock_price = stock_data["Time Series (Daily)"][yesterday]["4. close"]

two_days_ago =  (datetime.now() - timedelta(2)).strftime('%Y-%m-%d')
#TODO 2. - Get the day before yesterday's closing stock price
two_ago_closing_stock_price = stock_data["Time Series (Daily)"][two_days_ago]["4. close"]
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yst_closing_stock_price) - float(two_ago_closing_stock_price))
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage = difference / float(two_ago_closing_stock_price)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage > 0.05 or True:
    print("Get News")
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    news_params = {
    "q":COMPANY_NAME,
    "apiKey":NEWS_API_KEY,
    "from":yesterday,
    "sortBy":"publishedAt",
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"][:3]
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 
    messages = [(article['title'], article['description']) for article in articles]
#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    if float(yst_closing_stock_price) - float(two_ago_closing_stock_price) > 0:
        emoji = '🔺'
    else:
        emoji = '🔻'
        
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    print("Twilio MSG(s) sent")
    for message in messages:
        message = client.messages \
                    .create(
                        body=f"""{COMPANY_NAME}: {emoji}{int(percentage*100)}%
                        Headline: {message[0]}
                        Brief: {message[1]}
                        """,
                        from_=TWILIO_NUMBER,
                        to=PHONE_NUMBER,
                    )
        print(message.sid)
#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


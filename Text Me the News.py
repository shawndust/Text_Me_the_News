while True:
    # code goes here
    

    import requests
    from bs4 import BeautifulSoup

    page = requests.get('https://www.nytimes.com')

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')

    article_list = soup.find(class_='story-heading')
    article_list_items = article_list.find_all('a')

    for article in article_list_items:
        names = article.contents[0]
        print(names)
       # print(article.prettify())

    # Download the Python helper library from twilio.com/docs/python/install
    from twilio.rest import Client
    import time

    cellNum = "+xxxx"
    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "xxxx"
    auth_token = "xxxx"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
            "%s" % (cellNum),
            body="%s" % (names),
            from_="+xxxx")
    #    ,
    #        media_url="http://www.example.com/hearts.png")

    print(message.sid)
    
    time.sleep(3600)

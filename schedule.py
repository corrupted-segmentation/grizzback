import requests
from datetime import datetime
from bs4 import BeautifulSoup


def nextGame(team):
    if(team != "now"):
        url = "https://www.google.ca/search?q=" + 'when is the next ' + team + ' game'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/39.0.2171.95 Safari/537.36'}

        # gets the html of a website
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # finds the appropriate date
        dateString = soup.find("span", {"class": "imso_mh__lr-dt-ds"}).text

        # initializing date variables
        year = int(datetime.now().strftime('%Y'))
        month = int(datetime.now().strftime('%m'))
        day = int(datetime.now().strftime('%d'))

        if dateString.find("today") != -1:
            time = dateString.split(', ')[1].split(' ')

            if time[1] == 'AM':
                hour = int(time[0].split(':')[0])
                minute = int(time[0].split(':')[1])
            else:
                hour = int(time[0].split(':')[0]) + 12
                minute = int(time[0].split(':')[1])

            return datetime(year, month, day, hour, minute)

        elif dateString.find("tomorrow") != -1:
            time = dateString.split(', ')[1].split(' ')

            if time[1] == 'AM':
                hour = int(time[0].split(':')[0])
                minute = int(time[0].split(':')[1])
            else:
                hour = int(time[0].split(':')[0]) + 12
                minute = int(time[0].split(':')[1])

            return datetime(year, month, day + 1, hour, minute)

        else:
            month = int(dateString.split(', ')[1].split('/')[0])
            day = int(dateString.split(', ')[1].split('/')[1])

            time = dateString.split(', ')[2].split(' ')

            if time[1] == 'AM':
                hour = int(time[0].split(':')[0])
                minute = int(time[0].split(':')[1])
            else:
                hour = int(time[0].split(':')[0]) + 12
                minute = int(time[0].split(':')[1])

        return datetime(year, month, day, hour, minute)
    else:
        return "now"


#print(nextGame("rams"))

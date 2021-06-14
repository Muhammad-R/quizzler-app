import requests

parameters = {
    'amount' : 10,
    'type' : 'boolean',
    'categroy' : 18
}


r=requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean",params=parameters)

data=r.json()

x=data["results"]

question_data=data["results"]


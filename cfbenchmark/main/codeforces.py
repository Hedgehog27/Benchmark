import json
import requests as rq

def getDetail(username1,username2):

    page1 = rq.get(f'https://codeforces.com/api/user.info?handles={username1}')
    page2 = rq.get(f'https://codeforces.com/api/user.info?handles={username2}')
    userInfo = []
    userInfo.append(json.loads(page1.content.decode())['result'][0]) 
    userInfo.append(json.loads(page2.content.decode())['result'][0])

    for i in range(2):
        if 'firstName' not in userInfo[i]:
            userInfo[i]['firstName']= ""
        if 'lastName' not in userInfo[i]:
            userInfo[i]['lastName'] = ""
        if 'country' not in userInfo[i]:
            userInfo[i]['country'] = ""
        if 'organization' not in userInfo[i]:
            userInfo[i]['organization']=""
        if 'contribution' not in userInfo[i]:
            userInfo[i]['contribution']='0'
        if 'rank' not in userInfo[i]:
            userInfo[i]['rank'] = "NIL"
        if 'maxRating' not in userInfo[i]:
            userInfo[i]['maxRating']='0'
        if 'rating' not in userInfo[i]:
            userInfo[i]['rating']='0'
        if 'maxRank' not in userInfo[i]:
            userInfo[i]['maxRank'] = '0'
        if 'friendOfCount' not in userInfo[i]:
            userInfo[i]['friendOfCount']='0'

    detail = {
        'username1':{
            'Username' : userInfo[0]['handle'],
            'Name' : str(userInfo[0]['firstName'] + ' ' + userInfo[0]['lastName']),
            'Country' : userInfo[0]['country'],
            'Organization' : userInfo[0]['organization'],
            'Contribution' : userInfo[0]['contribution'],
            'Rank' : userInfo[0]['rank'],
            'Rating' : userInfo[0]['rating'],
            'Maximum Rank' : userInfo[0]['maxRank'],
            'Maximum Rating' : userInfo[0]['maxRating'],
            'Friend Of' : str(str(userInfo[0]['friendOfCount']) + ' users')
        },
        'username2':{
            'Username' : userInfo[1]['handle'],
            'Name' : str(userInfo[1]['firstName'] + ' ' + userInfo[1]['lastName']),
            'Country' : userInfo[1]['country'],
            'Organization' : userInfo[1]['organization'],
            'Contribution' : userInfo[1]['contribution'],
            'Rank' : userInfo[1]['rank'],
            'Rating' : userInfo[1]['rating'],
            'Maximum Rank' : userInfo[1]['maxRank'],
            'Maximum Rating' : userInfo[1]['maxRating'],
            'Friend Of' : str(str(userInfo[1]['friendOfCount']) + ' users')
        }
    }

    return detail
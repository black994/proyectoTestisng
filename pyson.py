import sqlite3
import requests
#import json

conn =sqlite3.connect('D:/jp949/Documents/Cali rec/proyecto/base_proy.s3db')
def LeerURL():
    url= "https://la1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/6VwWJ3bgVMf3X7TqZgE0auUVOULT7ybPTUHPSZ0sNXvSShg?api_key=RGAPI-213fa414-3a82-43e0-90df-5d96c1d98233"
    return  requests.get(url)

def insertdata(p_championId,p_championLevel,p_championPoints,p_lastPlayTime,p_championPointsSinceLastLevel):
    #project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30'); 
    ourvalues = (p_championId,p_championLevel,p_championPoints,p_lastPlayTime,p_championPointsSinceLastLevel)
    #Cursor Object
    conn =sqlite3.connect('D:/jp949/Documents/Cali rec/proyecto/base_proy.s3db')
    cursor=conn.cursor()
    query = ('INSERT INTO Campeon (championId,championLevel,championPoints,lastPlayTime,championPointsSinceLastLevel) '
         'VALUES (?,?,?,?,?)')
    params = {
        'championId': p_championId,
        'championPoints': p_championLevel,
        'championPoints': p_championPoints,
        'lastPlayTime': p_lastPlayTime,
        'championPointsSinceLastLevel': p_championPointsSinceLastLevel
    }
    cursor.execute(query,ourvalues)
   #conn.execute(query, params)
   # conn.execute("INSERT INTO Campeon (championId,championLevel,championPoints,lastPlayTime,championPointsSinceLastLevel) VALUES (221, 5, 44, 5454545, 454)")
    #conn.execute("INSERT INTO Campeon (championId,championLevel) VALUES (p_championId,p_championLevel)")

    conn.commit()
    conn.close()
#url= "https://la1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/6VwWJ3bgVMf3X7TqZgE0auUVOULT7ybPTUHPSZ0sNXvSShg/by-champion/19?api_key=RGAPI-213fa414-3a82-43e0-90df-5d96c1d98233"

Respuesta = LeerURL()
datos= Respuesta.json()
#with open(datos):

for campeones in datos :
    insertdata(campeones['championId'],campeones['championLevel'],campeones['championPoints'],campeones['lastPlayTime'],campeones['championPointsSinceLastLevel'])
    print('championId', campeones['championId'])
    print('champeonLevel', campeones['championLevel'])
        
    print('')



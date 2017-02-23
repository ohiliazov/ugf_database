from requests import post
import os, re

path = 'D:/Python/data/'
tournament_dir_list = os.listdir(path)
file = open(path+'rivne.csv')
response = post(url='http://127.0.0.1:8000/api/upload/ufgo_ratings/', files={'file': file})
print(response.text)

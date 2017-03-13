import os
import re

from requests import post

path = 'D:/Python/egd_data_manager/tables/'
tournament_dir_list = os.listdir(path)
for directory in tournament_dir_list:
    if directory == '2015':
        tournament_path = path + directory + '/'
        tournament_list = os.listdir(tournament_path)
        for name in tournament_list:
            reg_name = re.match(r"(?P<code>[\w\d]+)", name)
            file = open(tournament_path + name)
            response = post(url='http://127.0.0.1:8000/api/upload/egd_tournament/', files={'file': file})
            print(response.text)

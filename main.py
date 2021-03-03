import re
import datetime
from configparser import ConfigParser
from googlesearch import search

config_ini = ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

DOMAIN = config_ini.get('DEFAULT','domain')
TODAY = datetime.datetime.today().strftime("%Y-%m-%d")
KEYWORD_FILE = open('./src/keywords.txt', 'r')
KEYWORDLIST = KEYWORD_FILE.readlines()

def Results(query):
    Results= search(query, num_results=30)
    for i in range(len(Results)):                        
        x = re.search(DOMAIN, Results[i])
        if x:
            y = Results.index(Results[i])
            return y + 1
        else:
            continue
    

if __name__ == '__main__':
    
    for i in range(len(KEYWORDLIST)):
        rank = ''
        query = KEYWORDLIST[i]
        rank = Results(query)
        if rank != '':
            data = f"{query},{rank}"
            with open(f"./output/{TODAY}.txt", "a") as myfile:
                myfile.write(data)
        
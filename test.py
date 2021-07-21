#url =  'https://www.securitylab.ru//news/521972.php'

#article_id = article_id[:-4]
#print(article_id)
import json

with open('news_dict.json') as file:
    news_dict = json.load(file)

search_id = '5224427888'

if search_id in news_dict:
    print('The news is already in the dictionary')

else:
    print('Fresh news')
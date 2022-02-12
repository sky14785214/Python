import json 

with open('F:\GitHub\CodeCaseCrawler\FB.json',encoding="utf-8") as f:
    data = json.load(f)

print(type(data))
print(type(data[0]))
print(data[0]['text'])

for i in data:
    #print(i)
    print("text:" + i['text'])
    # print("age:" + str(i['age']))

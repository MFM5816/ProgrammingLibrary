import json

# 把列表或字典保存到json文件中
d = {'app':'微信','link':'www.weixin.com'}
with open('app.json','w') as f:
    json.dump(d,f,ensure_ascii=False)














from facepy import GraphAPI
import json
import pickle

access = 'EAACEdEose0cBALMlBlQKBpAPi9ERs8QRfXdTG747iP33cvuaBQYzKdMuhpG8h2FmUXZBCG04OCMuHHDZCkMwFkPerAnJdw9KZBumv67zD6zXegSZCU7ZBZBaef6RF9QN4WL7ndCH8XRWSRZBVsZBS7zKECAcYdcY544n3AonygsI7QZDZD'

graph = GraphAPI(access)
page_id= '821396057905476'
datas= graph.get(page_id+'/posts?fields=message', page=True, retry=5)

posts=[]

for data in datas:
    posts.append(data)
    



file=open('face.txt','w')
pickle.dump(posts,file)
file.close()

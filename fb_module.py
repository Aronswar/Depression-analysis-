from facepy import GraphAPI
import json
import pickle

access = ''
page_id= '821396057905476'
datas= graph.get(page_id+'/posts?fields=message', page=True, retry=5)

posts=[]

for data in datas:
    posts.append(data)
    



file=open('face.txt','w')
pickle.dump(posts,file)
file.close()

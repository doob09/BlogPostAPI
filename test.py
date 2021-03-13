import requests
''' 
please change different parameters for params to test the api call
'''
url = 'http://127.0.0.1:5000/api/posts'

params = dict(
    tag='tech',
    sortBy= 'likes',
    direction = 'desc'
)

#-----------------------
#test case 1:
# params = dict(
#     tag='',
#     sortBy= '',
#     direction = ''
# )

#------------------------
#test case 2:
# params = dict(
#     tag='health',
# )

#------------------------
#test case 3:
# params = dict(
#     tag='health,tech'
# )

#------------------------
#test case 4:
# params = dict(
#     tag='health,tech'
# )

#------------------------
#test case 5:
# params = dict(
#     tag='health,tech',
#     sortBy= ''
# )

#------------------------
#test case 6:
# params = dict(
#     tag='health,tech',
#     sortBy= 'id'
# )

#------------------------
#test case 7:
# params = dict(
#     tag='health,tech',
#     sortBy= 'id',
#     direction=''
# )

resp = requests.get(url=url,params=params)
data = resp.json()
print(data)
from flask import Flask,request,jsonify
from flask_api_cache import ApiCache
import requests


app = Flask(__name__)

#route handler
@app.route('/')
def welcome():
    return{'message':'Welcome'}

#Route 1
@app.route('/api/ping')
def ping():
    return {'success':'true'},200

#Route 2
#add cache 
@app.route('/api/posts')
@ApiCache(expired_time=180)
def post_query():
    #list of params from client-query
    args = request.args
    all_posts = []
    temp_check = []
    sorted_posts = []
    url= 'https://api.hatchways.io/assessment/blog/posts'
    # do the fetch if there is a valid tag
    try:
        if 'tag' in args:
            # seperate each tag to do single fetch 
            tag= request.args['tag']
            list_tags= tag.split(',')
            
            for each_tag in list_tags:
                params= dict( 
                        tag=each_tag,
                )
                raw_response = requests.get(url,params=params)
                posts_json = raw_response.json()
                # add all post together after doing fetch seperatly 
                for each_post in (posts_json['posts']):
                    if each_post['id'] not in temp_check:
                        temp_check.append(each_post['id'])
                        all_posts.append(each_post)
            # sort by Id by default
            sorted_posts = sorted(all_posts, key=lambda x:x['id'])
            #handle different sorts as requested
            if 'sortBy' in args:
                asc = False 
                if 'direction' in args:
                    if args['direction'] == 'desc':
                        asc= True
                    else:
                        return {"error": "direction parameter is invalid"},400
                #direction is asc by default
                if args['sortBy'] == 'id':
                    sorted_posts = sorted(all_posts, key=lambda x:x['id'],reverse=asc)
                elif args['sortBy'] == 'reads':
                    sorted_posts = sorted(all_posts, key=lambda x:x['reads'],reverse=asc)
                elif args['sortBy'] == 'likes':
                    sorted_posts = sorted(all_posts, key=lambda x:x['likes'],reverse=asc)
                elif args['sortBy'] == 'popularity':
                    sorted_posts = sorted(all_posts, key=lambda x:x['popularity'],reverse=asc)
                else:
                    return {"error": "sortBy parameter is invalid"},400
  
        return jsonify({'posts':sorted_posts})

    except:

        return {"error": "Tags parameter is required"}

if __name__ == '__main__':
    app.run(debug=True)
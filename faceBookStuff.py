
import facebook
import requests
import nltk
def some_action(post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    """
    print(post['name'])



access_token = 'EAACEdEose0cBAADhR1WdlEf8iQbofctvdDP8xriZC0zqBcMXTmf3kv5vpZCRTdqq0SOjtnXh20LXq1ZAt7yBJwZBifvQo2iEvYmRwBwh5HXQddJZC1IDGImAQJkWnepCCpYoMCRa1vDaOv1WMYmLtsJca0OADFjx78mGPewpOTAZDZD'
user = '10154393450720798'

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts')
while True:
    try:
        # Perform some action on each post in the collection we receive from
        # Facebook.
        [some_action(post=post) for post in posts['data']]
        # Attempt to make a request to the next page of data, if it exists.
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
	break
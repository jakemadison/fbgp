__author__ = 'Madison'

import facebook

graph = facebook.GraphAPI(access_token='your_token')

post = graph.get_object(id='post_id')
print(post['message'])



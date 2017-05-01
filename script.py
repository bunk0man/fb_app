import facebook

graph = facebook.GraphAPI(access_token='your_token', version='2.9')
# Get all the comments from a post
comments = graph.get_connections(id='post_id', connection_name='comments')

import facebook

graph = facebook.GraphAPI(access_token='your_token', version='2.9')
# Get all the comments from a post
comments = graph.get_connections(id='post_id', connection_name='comments')

# Write 'Hello, world' to the active user's wall.
graph.put_object(parent_object='me', connection_name='feed',
                 message='Hello, world')

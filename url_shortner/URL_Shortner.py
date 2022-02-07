import bitly_api 
BITLY_ACCESS_TOKEN ="e2f3f71a12977f3b0bf9fe6219c8e8c28dc55313"
access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
full_link = input()
short_url = access.shorten(full_link) 
print('Short URL = ',short_url['url'])
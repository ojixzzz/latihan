import falcon
from user import userResource, userResourceid
from book import bookResource, bookResourceid
from item import itemResource, itemResourceid

app = falcon.API()
user	= userResource()
userid  = userResourceid()

book   = bookResource()
bookid = bookResourceid()

item   = itemResource()
itemid = itemResourceid()

app.add_route('/user', user)
app.add_route('/user/{id}', userid)

app.add_route('/book', tes2)
app.add_route('/book/{id}', bookid)

app.add_route('/item', item)
app.add_route('/item/{id}', itemid)


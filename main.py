import falcon
import mongoengine as mongo

from wsgiref.simple_server import make_server
from resources.CustomerResource import CustomerResource

from falcon_swagger_ui import register_swaggerui_app

mongo.connect(
    'jadb',
    host='mongodb+srv://lechatong:Sandreen6@jadb.xc0t6.mongodb.net/test?retryWrites=true&w=majority',
    port=27017,
    username='lechatong',
    password='Sandreen6'
)


class MainResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = (''
                     'LeChatong is Here')

SWAGGERUI_URL = '/swagger'

SCHEMA_URL = 'swagger.json'

page_title = 'Falcon Swagger Doc'
favicon_url = 'https://falconframework.org/favicon-32x32.png'

app = falcon.API(cors_enable=True)

main = MainResource()
customer = CustomerResource()

app.add_route('/', main)
app.add_route('/customer', customer)
app.add_route('/customer/{fiscal_number}', customer, suffix='id')

register_swaggerui_app(app, SWAGGERUI_URL, SCHEMA_URL, page_title=page_title,
                       favicon_url=favicon_url,
                       config={'supportedSubmitMethods': ['get', 'post', 'put', 'delete'], })

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print("Loading port 8000")
        httpd.serve_forever()

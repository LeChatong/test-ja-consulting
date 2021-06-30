import json

import falcon

from models.customer import Customer

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict


class BaseResource(object):

    def success(self, resp, data=None):
        resp.status = falcon.HTTP_200
        obj = OrderedDict()
        obj['status'] = 200
        obj['data'] = data
        obj['message'] = 'OK'
        resp.body = json.dumps(obj)


class CustomerResource(BaseResource):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        customers = Customer.objects()

        resp.body = customers.to_json()

    def on_get_id(self, req, resp, fiscal_number):

        try:
          cust_obj= Customer.objects.get(fiscal_number=fiscal_number)

          resp.body = cust_obj.to_json()
          resp.status = falcon.HTTP_200
        except Exception as e:
          resp.status = falcon.HTTP_404
          resp.body = json.dumps({
            'message': 'Not a client !',
            'status': 404,
            'data': {}
            })

    def on_post(self, req, resp):
        doc = req.context['doc']
        customer = Customer(fiscal_number=doc['fiscal_number'])
        customer.save()
        self.success(resp, "Customer created with success")

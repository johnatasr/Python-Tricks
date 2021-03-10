from .framework_json import request_in_json
from .framework_soap import request_in_soap
from .helpers.adapter import Adapter


def main():
    # SOAP -> JSON
    request_soap = request_in_soap()
    adapter = Adapter(request_soap)
    response_json = adapter.trasnform_to_json()

    # JSON -> SOAP
    request_json = request_in_json()
    adapter = Adapter(request_json)
    response_soap = adapter.transform_to_soap()






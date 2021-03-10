
class Adapter:

    def __init__(self, request):
        self.request = request

    def trasnform_to_json(self):
        """
            Here occours the transformation of SOAP to JSON
        """
        ...

    def transform_to_soap(self):
        """
            Here occours the transformation of JSON to SOAP
        """
        ...

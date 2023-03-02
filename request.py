from exceptions import InvalidRequest, InvalidStorageName

class Request():
    def __init__(self, storage_list:list, request_text:str):
        try:
            divided_request = request_text[10:]
            divided_request = divided_request.split(' в ')
            self.destination = divided_request[1].lower()
            divided_request= divided_request[0].split(' из ')
            self.departure = divided_request[1].lower()
            divided_request = divided_request[0].split(' ', 1)
            self.amount = int(divided_request[0])
            self.product = divided_request[1].lower()
        except:
            raise InvalidRequest


        if self.departure not in storage_list or self.destination not in storage_list:
            raise InvalidStorageName


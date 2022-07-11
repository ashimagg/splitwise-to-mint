
from requests import request


request_headers_path = 'data/request_headers.txt'

def curl_request(payload):
        # construct the curl command from request
        
        url = 'https://mint.intuit.com/pfm/v1/transactions'
        # header = get_headers()
        header = construct_headers()

        return f"curl '{url}' {header}--data-raw '{payload}' --compressed"      

def construct_headers():

    headers = ""
    for line in open(request_headers_path, 'r').readlines():
        headers = headers + f"-H '{line[:-1]}' "

    return headers
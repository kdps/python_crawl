import urllib
import requests
import concurrent
from bs4 import BeautifulSoup as bs

def getRequest(method = "get", url = "", parameters = {}, proxies = {}):
   encodedParameter = urllib.parse.urlencode(parameters)
   response = getattr(requests, method)(url, proxies=proxies)
   return response
# end def

response = getRequest("get", "https://www.google.com")
response = bs(response.text, "html.parser")


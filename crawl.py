import urllib
import requests
import concurrent
from bs4 import BeautifulSoup as bs
from requests.adapters import HTTPAdapter, Retry
from urllib.parse import urlparse
from requests.exceptions import ProxyError, SSLError, ConnectTimeout

def getRequest(method = "get", url = "", parameters = {}, proxies = {}, headers = {}):
   try:
      with requests.Session() as session:
         retries = Retry(total = 5, backoff_factor = 1, status_forcelist = [502, 503, 504])
         parsedUri = urlparse(url)
         session.mount(parsedUri.scheme + '://', HTTPAdapter(max_retries=retries))
         
         encodedParameter = urllib.parse.urlencode(parameters)
         response = getattr(session, method)(url, proxies=proxies, headers=headers)
         return response
   except (ProxyError, SSLError, ConnectTimeout) as e:
      print(e)
# end def

response = getRequest("get", "https://www.google.com")
response = bs(response.text, "html.parser")

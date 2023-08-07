import urllib
import requests
import concurrent
from bs4 import BeautifulSoup as bs
from requests.adapters import HTTPAdapter, Retry
from urllib.parse import urlparse
from requests.exceptions import ProxyError, SSLError, ConnectTimeout
from urllib.parse import parse_qs

def getRequest(method = "get", url = "", parameters = {}, proxies = {}, headers = {}):
   try:
      with requests.Session() as session:
         retries = Retry(total = 5, backoff_factor = 1, status_forcelist = [502, 503, 504])
         parsedUri = urlparse(url)
         session.mount(parsedUri.scheme + '://', HTTPAdapter(max_retries=retries))
         
         concatParameters = parse_qs(parsedUri.query)
         concatParameters.update(parameters)
         
         encodedParameter = urllib.parse.urlencode(concatParameters)
         requestUrl = url.split('?')[0].split('#')[0]
         
         if (encodedParameter != ''):
             requestUrl = requestUrl + '?' + encodedParameter
         # end if
         
         response = getattr(session, method)(requestUrl, proxies=proxies, headers=headers)
         return response
   except (ProxyError, SSLError, ConnectTimeout) as e:
      print(e)
# end def

response = getRequest("get", "https://section.cafe.naver.com/ca-fe/home/search/combinations?q=%EA%B0%80", parameters = {'test': 'test'})
response = bs(response.text, "html.parser")

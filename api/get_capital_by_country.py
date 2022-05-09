from ast import parse
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    url_components = parse.urlsplit(self.path)
    query_string_list = parse.parse_qsl(url_components)
    dic = dict(query_string_list)

    try:
      if "country" is dic:
        base_url = "https://restcountries.com/v3.1/name/"
        query_string = dic["country"]
        full_url = base_url + query_string
        response = requests.get(full_url)
        country_data = response.json()
        capital_city = 
    except(Exception):
      message = "Valid country required to discover the capital city."

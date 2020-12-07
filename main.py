#encoding=utf8
import requests
from bs4 import BeautifulSoup
import webbrowser
from wox import Wox,WoxAPI




class CurrencyConvert(Wox):

  def request(self,url):
    #If user set the proxy, you should handle it.
    if self.proxy and self.proxy.get("enabled") and self.proxy.get("server"):
      proxies = {
        "http":"http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port")),
        "https":"http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port"))}
      return requests.get(url,proxies = proxies)
    else:
      return requests.get(url)

   def query(self,key):
       proxies = {}
       if self.proxy and self.proxy.get("enabled") and self.proxy.get("server"):
           proxies = {
             "http": "http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port")),
             "http": "https://{}:{}".format(self.proxy.get("server"),self.proxy.get("port"))
           }
		
		url = "https://currency-exchange.p.rapidapi.com/exchange"

		querystring = {"from":"eur","to":"usd","q":"1.0"}	

		headers = {
    		'x-rapidapi-key': "f68436e819mshabf74cd59d589ccp145898jsnbfa75c621668",
    		'x-rapidapi-host': "currency-exchange.p.rapidapi.com"
    		}

		response.text = requests.request("GET", url, headers=headers, params=querystring)

		return response


  
  def openUrl(self,url):
    webbrowser.open(url)
    WoxAPI.change_query(url)		





if __name__ == "__main__":
    CurrencyConvert()
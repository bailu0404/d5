from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.perigold.com/'
url1 = 'https://www.baidu.com/'
url2 = 'https://www.google.com/'

#headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

#req = Request(url=url2, headers=headers)

html = urlopen(url)

bs_obj = BeautifulSoup(html.read(),'html.parser')

test_list_1 = bs_obj.find_all('a','Header-deptLinks-link')
test_list_2 = bs_obj.find_all('a','Header-dropdown-link--heading')
test_list_3 = bs_obj.find_all('a','Header-dropdown-link')

print(test_list_1)
print(test_list_2)
print(test_list_3)


html.close()
import requests
#import urllib.requests
#opener=urllib.request.build_opener()
#response=opener.open('https://httpbin.org/get')
#print(response.read())
res_parse_list=[]
response=requests.get('https://coinmarketcap.com/')
response_text=response.text
response_parse=response_text.split('<span>')
print(response.text)
for parse_ele_1 in response_parse:
    if parse_ele_1.startswith('$'):
        for parse_ele_2 in parse_ele_1.split('</span>'):
            if parse_ele_2.startswith('$') and parse_ele_2[1].isdigit():
                res_parse_list.append(parse_ele_2)
bitcoin_exchange_rate=res_parse_list[0]
print(bitcoin_exchange_rate)
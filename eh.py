import requests
res_parse_list=[]
response=requests.get('https://coinmarketcap.com/')
response_text=response.text
response_parse=response_text.split('<span>')
for parse_ele_1 in response_parse:
    if parse_ele_1.startswith('$'):
        for parse_ele_2 in parse_ele_1.split('</span>'):
            if parse_ele_2.startswith('$') and parse_ele_2[2].isdigit():
                res_parse_list.append(parse_ele_2)
uniswap_exchange_rate=res_parse_list[1]
print(uniswap_exchange_rate)


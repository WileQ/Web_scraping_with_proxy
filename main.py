import requests
import random


def get_random_proxy():
    url = 'https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc'
    response = requests.get(url, timeout=10)
    data = response.json()

    proxy = {}
    proxy_list = []
    for cos in data.get("data"):
        print(f"IP:{cos.get('ip')} Port: {cos.get('port')} Country: {cos.get('country')} Protocol: {cos.get('protocols')}")
        proxy_list.append(f"{cos.get('ip')}:{cos.get('port')}")

    proxy["http"] = random.choice(proxy_list)
    print(proxy)

    return proxy

def accesing():
    proxy = get_random_proxy()
    url = "Put your link here"
    response = requests.get(url, proxies=proxy, timeout=10)
    print(response.text)

accesing()
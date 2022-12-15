import requests
import csv


def export():
    cookies = {
        '_t': '2058cb22c74774f0f299206749a2debe281940309cdfb2bf22573067d9710d62a%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22_t%22%3Bi%3A1%3Bs%3A32%3A%22JFpNY9ScNZtfK-qIgP0wTdi0pkzZ031y%22%3B%7D',
        'szsid': '1f5pbecmiibgfued5hjrhmtmsh',
        '_identity': '34ee76fd8242a60ace3dc5c6f6990ea20c7474c64283f760b1f549ea562a25dca%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B24800%2C%2284V5ks0RA0mvaJFRHaLInmHh-6zspoDV%22%2C2592000%5D%22%3B%7D',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-CSRF-Token': 'QH-kVeAI7tgnO6cGnuvp1R71fGIX1F44KOU0GfhBpMQKOdQbuTG9u2lh02DVxpiceaVMFUOwNwhYjk5DyHKVvQ==',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.spamzilla.io',
        'Connection': 'keep-alive',
        'Referer': 'https://www.spamzilla.io/domains/?page=11&per-page=25',
        # 'Cookie': '_t=2058cb22c74774f0f299206749a2debe281940309cdfb2bf22573067d9710d62a%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22_t%22%3Bi%3A1%3Bs%3A32%3A%22JFpNY9ScNZtfK-qIgP0wTdi0pkzZ031y%22%3B%7D; szsid=1f5pbecmiibgfued5hjrhmtmsh; _identity=34ee76fd8242a60ace3dc5c6f6990ea20c7474c64283f760b1f549ea562a25dca%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B24800%2C%2284V5ks0RA0mvaJFRHaLInmHh-6zspoDV%22%2C2592000%5D%22%3B%7D',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    # first 10k
    # data = {
    #     'type': 'csv',
    #     'domainsCount': '10000',
    #     'params': 'a:2:{s:6:"filter";a:0:{}s:5:"query";a:2:{s:4:"page";s:1:"1";s:8:"per-page";s:3:"500";}}',
    # }

    # second 10k
    data = {
        'type': 'csv',
        'domainsCount': '10000',
        'params': 'a:2:{s:6:"filter";a:0:{}s:5:"query";a:2:{s:4:"page";s:2:"21";s:8:"per-page";s:3:"500";}}',
    }

    response = requests.post('https://www.spamzilla.io/expired-domains/export/',
                             cookies=cookies, headers=headers, data=data)

    return response.text


def download(url):
    print(url)
    cookies = {
        '_t': '2058cb22c74774f0f299206749a2debe281940309cdfb2bf22573067d9710d62a%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22_t%22%3Bi%3A1%3Bs%3A32%3A%22JFpNY9ScNZtfK-qIgP0wTdi0pkzZ031y%22%3B%7D',
        'szsid': '1f5pbecmiibgfued5hjrhmtmsh',
        '_identity': '34ee76fd8242a60ace3dc5c6f6990ea20c7474c64283f760b1f549ea562a25dca%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B24800%2C%2284V5ks0RA0mvaJFRHaLInmHh-6zspoDV%22%2C2592000%5D%22%3B%7D',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://www.spamzilla.io/domains/',
        # 'Cookie': '_t=2058cb22c74774f0f299206749a2debe281940309cdfb2bf22573067d9710d62a%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22_t%22%3Bi%3A1%3Bs%3A32%3A%22JFpNY9ScNZtfK-qIgP0wTdi0pkzZ031y%22%3B%7D; szsid=1f5pbecmiibgfued5hjrhmtmsh; _identity=34ee76fd8242a60ace3dc5c6f6990ea20c7474c64283f760b1f549ea562a25dca%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B24800%2C%2284V5ks0RA0mvaJFRHaLInmHh-6zspoDV%22%2C2592000%5D%22%3B%7D',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'file': url,
    }

    response = requests.get('https://www.spamzilla.io/expired-domains/download',
                            params=params, cookies=cookies, headers=headers)

    return response.content


url = export()
content = download(url)
content = content.decode('utf-8')
cr = csv.reader(content.splitlines(), delimiter=',')

my_list = list(cr)
for row in my_list[:10]:
    print(row)

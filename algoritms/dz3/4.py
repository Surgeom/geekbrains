import hashlib
cache = {}
url = 'https://geekbrains.ru'


def urls_cache(url):
    salt = 'something'
    urls_hash = hashlib.sha256(salt.encode() + f'{url}'.encode()).hexdigest()
    if urls_hash not in cache.values():
        cache[url] = urls_hash
    else:
        print('already in cache')


urls_cache(url)
print(cache)

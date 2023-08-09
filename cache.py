import requests

cache = dict()

def get_article_from_server(url):
    print("Fetching article from server...")
    response = requests.get(url)
    # print(response.text)
    return response.text

def get_article(url):
    print("Getting article...")
    if url not in cache:
        cache[url] = get_article_from_server(url)
        print(cache)

    return cache[url]

get_article("https://realpython.com/sorting-algorithms-python/")
get_article("https://realpython.com/sorting-algorithms-python/")
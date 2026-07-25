import requests

def get_quote(author="any"):
    try:
        url = "https://zenquotes.io/api/random"
        response = requests.get(url) 

        if response.status_code == 200:
              data = response.json()
              quote_text = data[0]["q"]
              quote_author = data[0]["a"]

              print(f'"{quote_text}" — {quote_author}')


    except requests.exceptions.RequestException:
        print("Unable to reach the quote service. Check your internet connection!")


get_quote()
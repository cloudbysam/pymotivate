import requests
import random

LOCAL_QUOTES = {
    "uncle iroh": [
        "Failure is only the opportunity to begin again, only this time more wisely.",
        "Good tea is its own reward.",
        "Sometimes life is like this dark tunnel. You can’t always see the light at the end of the tunnel, but if you just keep moving you will come to a better place."
    ],
    "da vinci": [
        "Learning never exhausts the mind.",
        "Simplicity is the ultimate sophistication.",
        "It has long since come to my attention that people of accomplishment rarely sat back and let things happen to them. They went out and happened to things."
    ],
    "machiavelli": [
        "Everyone sees what you appear to be, few experience what you really are.",
        "The first method for estimating the intelligence of a ruler is to look at the men he has around him."
    ]
}

def get_quote(author="any"):
        clean_author = author.lower()
        
        if clean_author in LOCAL_QUOTES:
             quote = random.choice(LOCAL_QUOTES[clean_author])
             print(f"{quote} - {author.title()}")

        else:
            try:

                if clean_author != "any":
                    print(f'"{author.title()}" isn\'t in our local database yet. Here is a random quote for you:\n')
                    
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
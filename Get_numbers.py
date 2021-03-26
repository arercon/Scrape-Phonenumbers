import requests, bs4, re, sys

def get_phonenumbers(url):
    if url == "e":
        print("Goodbye!")
        sys.exit()
    user_agent = "Mozilla/5.0"
    # Creating a variable that will store the content of the page
    r = requests.get(url, headers={'User-Agent': user_agent})
    if r.status_code == 404:
        print("Sorry, unable to find the page with url " + url)
    # Using BeautifulSoup() class to create a parse tree of our page.
    soup = bs4.BeautifulSoup(r.content, "html.parser")(["a", "p"])
    for x in soup:
        # Using regex to filter the phone numbers out of the data.
        potential_numbers = re.findall(r"((?:\+4|0[1-9])[\d] ?[\d\ (\–\-][\d\ \-\/)][\d\ \–\-\/)(]{6,21})",str(x))
        if potential_numbers:
            for num in potential_numbers:
                print(num)
    print("\b")

url = None
while url != "e":
    url = input("Enter URL from which you want to extract the phone numbers(Type e for exit): \n")
    get_phonenumbers(url)

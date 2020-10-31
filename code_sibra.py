from bs4 import BeautifulSoup

import requests

import json


def get_dic_of_stops(source):
    dic_stops = {}
    soup = BeautifulSoup(source,features="html.parser")
    # driver.find_element_by_xpath("//select[@id='filtres']/option[text()='A']").click()
    with open("stops.json", "w") as f:
        for j in range(1,22):
            lis = soup.find("ul", id = f"a{j}").find_all("li")
            for i in lis:
                dic_stops[i.text] = "https://m.sibra.fr" + i.a["href"]
        f.write(json.dumps(dic_stops, indent=4, sort_keys=True))

def main():
    url = "https://m.sibra.fr/temps-reel-mobile"
    page = requests.get(url)
    get_dic_of_stops(page.text)

if __name__ == "__main__":main()
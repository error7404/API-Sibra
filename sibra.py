from bs4 import BeautifulSoup
import os.path
import requests

import json

def get_info(source):
    ret = []
    soup = BeautifulSoup(source,features="html.parser")
    if soup.find("div", class_ = "content").h2 == None:
        divs = soup.find_all("div", class_ = "resultats-recherche-horaires-tempsreel")
        with open("return", "w", encoding="utf-8") as f:
            for i in divs:
                i = i.ul.li.a.span
                spans = i.find_all("span")
                # f.write(str(i) + "\n\n")
                ret.append({"number" : spans[1].text, "time" : spans[2].strong.text, "Direction" : spans[2].find_all('strong')[1].text})
            f.write(json.dumps(ret, indent=4))
    else:
        print("probleme page")


if __name__ == "__main__":
    if not os.path.isfile('stops.json'):
        import code_sibra
        code_sibra.main()
    
    with open("stops.json", "r") as f:
        stops = json.loads(f.read())
        page = requests.get(stops["ALERY BANQUE DE FRANCE"]).text
    # for i in range(10):
    #     driver.refresh()
    get_info(page)

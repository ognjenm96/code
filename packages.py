# pypi.org ovde mozemo skinuti dodatne pakete za pajton
# python ima svoj paket meneager pip
# python has requests librery for API usage can be installed with pip

# USING API request to get a song information form itunes
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
    
i = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
n = i.json()
# loop da izlista 10 imana pesama zadatok benda od strane korisnika
for final in n["results"]:
    print(final["trackName"])
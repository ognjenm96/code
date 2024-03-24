# Lista dictionera, kombinavanje lista i kolekcija

ucenici = [
    {"ime": "Hari", "kuca": "Hony", "patronas": "Lane"},
    {"ime": "Ron", "kuca": "Grifi", "patronas": "Jelen"},
    {"ime": "Drako", "kuca": "Slit", "patronas": None}
]

for studenti in ucenici:
    print(studenti["ime"], studenti["kuca"], studenti["patronas"], sep=", ")
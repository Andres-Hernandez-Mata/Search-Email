"""
Uso: Email
Creador: Andrés Hernández Mata
Version: 1.1.0
Python: 3.9.1
Fecha: 17 Abril 2020
"""

import requests
import re
import os

os.system("cls")

url = 'https://www.themoscowtimes.com/page/moscow-times'

response = requests.get(url)
if response.status_code != 200:
    exit()

# a set of crawled emails
regExMail = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
new_emails = set(re.findall(regExMail, response.text, re.I))
for i in new_emails:
    print(i)
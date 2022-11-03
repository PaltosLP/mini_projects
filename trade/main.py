import re
import yaml
from scrape import login

with open('config.yaml', 'r') as file:
    conf = yaml.safe_load(file)
# conf = yaml.load(open('config.yml'))
email = conf['user']['email']
password = conf['user']['password']


source = login("https://mail.google.com", "identifierId", email, "Passwd", password, "identifierNext", "passwordNext")
source = str(source)
#print(source)

location = re.search("Meldung:", source)
span = location.span()

loc_0 = int(span[0])
loc_1 = int(span[1]) + 50

print(type(loc_0), "types", type(loc_1))

text = source[loc_0:loc_1]


print("\n---------\n")

print(text)

import requests
import time
import re
import sys
import random
import names
#reload(sys)
#sys.setdefaultencoding('utf-8')

url = 'https://nakedcph.typeform.com/app/form/submit/d4h3LI'
print"---------------------------"
print"NakedCPH Script for Off White"
print"---------------------------"
print"FOR STRIKE SHOES MEMBERS ONLY"
print"---------------------------"

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
sizes = ['36','36,5', '37,5', '38', '38,5', '39', '40' ,'40,5' ,'41']

def main(limit):
    for i in range(0, limit):
        firstName = names.get_first_name(gender='male')
        lastName = names.get_last_name()
        payload ={
            'form[email:DbejoTewn3KY]': '{}.{}@vapegod.net'.format(firstName, lastName), # replace this with your catchall domain or replace @vapegod.net with +youremail@gmail.com so it reads '{}.{}+youremail@gmail.com' where your email is your gmail username.
            'form[landed_at]': '1522177248',
            'form[language]': 'en',
            'form[textfield:kzvXmgequ5cj]': firstName,
            'form[textfield:osX4pAneqE9T]': lastName,
            'form[dropdown:ZdaAOXNjjTtY]': 'United States of America',
            'form[token]': 'f0541e7bc5b224944625edc924ebb4ed$2y$11$e2dJZC0zIXZQK1pxbSZbL.o6LdYCCu5A2lRBbxuZwyGaOCsAL5c8m'
              }
        resp = requests.post(url, data=payload, headers=headers)
        if any(re.findall(r'succes', str(resp.text), re.IGNORECASE)):
            print(time.strftime("%H:%M:%S") + " ; Successful entry {}/{}".format(i, limit) )
        else:
            print(time.strftime("%H:%M:%S") + " ; Could not enter")

main (1000) #change to the amount of entries you want
exit()

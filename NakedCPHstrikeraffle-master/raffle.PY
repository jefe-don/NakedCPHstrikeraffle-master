import requests
import time
import re
import sys
import random
from random import getrandbits
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

list1 = ["Beck","Glenn","Becker","Carl","Beckett","Samuel","Beddoes","Mick","Beecher","HenryWard","Beethoven","Ludwigvan","Begin","Menachem","Bell","Alexander","Graham","Belloc","Hilaire","Bellow","Saul","Benchley","Robert","Benenson","Peter","BenGurion","David","Benjamin","Walter","Benn","Tony","Bennington","Chester","Benson","Leana","Bent","Silas","Bentsen","Lloyd","Berger","Ric","Bergman","Ingmar","Berio","Luciano","Berle","Milton","Berlin","Irving","Berne","Eric","Bernhard","Sandra","Berra","Yogi","Berry","Halle","Berry","Wendell","Bethea","Erin","Bevan","Aneurin","Bevel","Ken","Biden","Joseph","Bierce","Am","Brose","Biko","Steve","Billings","Josh","Biondo","Frank","Birrell","Augustine","Black","Elk","Blair","Ro","Bert","Blair","Tony","Blake","William","Blakey","Art","Blalock","Jolene","Blanc","Mel","Blanc","Raymond","Blanchet","Cate","Blix","Hans","Blood","Rebecca"]
sizes = ['36','36,5', '37,5', '38', '38,5', '39', '40' ,'40,5' ,'41']

def main(limit):
    for i in range(0, limit):
        payload ={
            'form[email:DbejoTewn3KY]': 'jefe+{}@jefe1.com'.format(getrandbits(50)), #change jefe and jefe1 to fit your email
			'form[list:g6XkmQ6SDr1r][choices]': sizes[random.randint(0, 8)],
            'form[landed_at]': '1522177248',
            'form[language]': 'en',
            'form[textfield:kzvXmgequ5cj]': list1[random.randint(0, 99)],
            'form[textfield:osX4pAneqE9T]': list1[random.randint(0, 99)],
            'form[dropdown:ZdaAOXNjjTtY]': 'United States of America',
            'form[token]': 'f0541e7bc5b224944625edc924ebb4ed$2y$11$e2dJZC0zIXZQK1pxbSZbL.o6LdYCCu5A2lRBbxuZwyGaOCsAL5c8m'
              }
        resp = requests.post(url, data=payload, headers=headers)
        if any(re.findall(r'succes', str(resp.text), re.IGNORECASE)):
            print(time.strftime("%H:%M:%S") + " ; Successful entry" )
        else:
            print(time.strftime("%H:%M:%S") + " ; Could not enter")

main (100) #change to the amount of entries you want
exit()

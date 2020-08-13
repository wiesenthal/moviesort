import requests

URL="https://www.rottentomatoes.com/api/private/v2.0/search"



def checkAll(file):
    f = open(file, 'r')
    f2 = open('rtOut.txt', 'w')
    i = 0
    for line in f.readlines():
        line = line.strip()
        print(line)

        r = requests.get(url=URL, params={'q': line, "limit": 1})
        r.raise_for_status()
        r = r.json()
        f2.write(line + ': ')
        f2.write(str(r['movies'][0]['meterScore']) + '\n')
        f2.flush()
    f.close()
    f2.close()

checkAll('out.txt')

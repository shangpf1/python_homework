"""
a = 'helloworld'

print(a[1:8])
print(a[1:8:2])

for x in range(1,10):
    for y in range(1,x+1):
        print('{}*{}={}\t'.format(y,x,x*y),end='')
    print()


print(3 in [1,2,3])

"""

import requests

url = 'https://api.github.com/user'

r = requests.get(url,auth=('shangpf1','spf123456'))
print(r.json())

print(r.status_code)


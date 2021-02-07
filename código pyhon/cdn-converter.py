import clipboard

print('CDN CONVERTER')
# Variables
url = input('Ingresa URL: ')
urlp = url.split('/')
user = urlp[3]
repo = urlp[4]
di = urlp[6:]
file = '/'.join(di)
dir = f'https://cdn.jsdelivr.net/gh/{user}/{repo}@{file}'

clipboard.copy(dir)
print('\nEste es tu link:')
print(dir)

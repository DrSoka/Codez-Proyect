import clipboard

print('CDN CONVERTER')

# Variables
url = input('Ingresa URL: ')
urlp = url.split('/')
urlp[2] = 'rawgit.com'

user = urlp[3]
proyect = urlp[4]
di = urlp[5:]
d = '/'.join(di)

dir = f'https://cdn.jsdelivr.net/gh/{user}/{proyect}@{d}'

clipboard.copy(dir)
print('\nEste es tu link:')
print(dir)

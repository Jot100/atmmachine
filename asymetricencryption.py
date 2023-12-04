from Crypto.PublicKey import RSA
key = RSA.generate(3072)
file= open('Rsakey.pem','wb')
file.write(key.exportKey('PEM'))
file.close()

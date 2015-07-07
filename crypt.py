from Crypto.Cipher import AES
import base64


secret_key = 'key'.rjust(32) 

cipher = AES.new(secret_key,AES.MODE_ECB) 
def sifrele(x):
    x = x.rjust(32)
    encoded = base64.b64encode(cipher.encrypt(x))
    return encoded
def sifrecoz(x):

    decoded = cipher.decrypt(base64.b64decode(x))
    decoded = decoded.decode("utf-8")
    return decoded.strip()

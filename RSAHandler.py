__author__ = 'Liran & Rotem '

from Crypto.PublicKey import RSA
from Crypto import Random


class RSAHandler:
    def __init__(self):
        self.my_key = RSA.generate(1024, Random.new().read)
        self.public_key = self.my_key.publickey()
        self.dst_public_key = None

    @property
    def dst_public_key(self):
        return self.dst_public_key

    @dst_public_key.setter
    def dst_public_key(self, dst_public_key):
        self.dst_public_key = dst_public_key

    @staticmethod
    def get_enc_message(message, public_key):
        return public_key.encrypt(message, 32)[0]

    @staticmethod
    def get_dec_message(private_key, enc_message):
        return private_key.decrypt(enc_message)

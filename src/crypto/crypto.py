import rsa


class Crypto:
    public_key = None
    private_key = None

    def generate_keys(self):
        (public_key, private_key) = rsa.newkeys(1024)
        self.public_key = public_key
        self.private_key = private_key

        with open('public_key.pem', 'wb') as f:
            f.write(rsa.PublicKey.save_pkcs1(self.public_key, format='PEM'))

        with open('private_key.pem', 'wb') as f:
            f.write(rsa.PrivateKey.save_pkcs1(self.private_key, format='PEM'))

        return public_key, private_key

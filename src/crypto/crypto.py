import rsa


class Crypto:
    public_key = None
    private_key = None

    def generate_keys(self):
        (public_key, private_key) = rsa.newkeys(512)
        self.public_key = public_key
        self.private_key = private_key

        return public_key, private_key

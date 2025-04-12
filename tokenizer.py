
class Encoder:
    def encode(self, data: str):
        data = list(data)
        new_data = []
        for char in data:
            new_data.append(ord(char)+25)
        return new_data

class Decoder:
    def decode(self, data: list):
        decoded_data = []
        for char in data:
            decoded_data.append(chr(char-25))
        return decoded_data


class Tokenizer:
    def __init__(self):
        self.encoder = Encoder()
        self.decoder = Decoder()

    def put_data(self, data: str):
        self.data = data
        self.encoded_data = self.encoder.encode(data)

    def get_encoded_data(self):
        return self.encoded_data

    def get_decoded_data(self, data: list):
        self.data = data
        self.decoded_data = self.decoder.decode(data)
        return self.decoded_data


if __name__ == "__main__":
    tokenzier = Tokenizer()
    action = int(input("Enter 'encode' -> 1 or 'decode' -> 2: "))
    if action == 1:
        tokenzier.put_data(input("Enter a string: "))
        print(f"Tokens: {tokenzier.get_encoded_data()}")
    elif action == 2:
        data = list(map(int, input("Enter a list of tokens: ").split(',')))
        print(data)
        print(f"Decoded data: {''.join(tokenzier.get_decoded_data(data))}")
    else:
        print("Invalid action")
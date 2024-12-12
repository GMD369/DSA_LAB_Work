import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoding:
    def __init__(self):
        self.codes = {}
        self.reverse_mapping = {}

    def build_frequency_table(self, text):
        return Counter(text)

    def build_huffman_tree(self, frequency):
        heap = [Node(char, freq) for char, freq in frequency.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right

            heapq.heappush(heap, merged)

        return heap[0]  # Root of the Huffman tree

    def build_codes(self, root, current_code=""):
        if not root:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.build_codes(root.left, current_code + "0")
        self.build_codes(root.right, current_code + "1")

    def encode(self, text):
        encoded_text = "".join(self.codes[char] for char in text)
        return encoded_text

    def decode(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                decoded_text += self.reverse_mapping[current_code]
                current_code = ""

        return decoded_text

    def compress(self, text):
        frequency = self.build_frequency_table(text)
        root = self.build_huffman_tree(frequency)
        self.build_codes(root)

        encoded_text = self.encode(text)
        return encoded_text

    def decompress(self, encoded_text):
        return self.decode(encoded_text)


# Example Usage
if __name__ == "__main__":
    text = "huffman coding is a compression algorithm"
    huffman = HuffmanCoding()

    # Compress
    encoded_text = huffman.compress(text)
    print("Encoded Text:", encoded_text)

    # Decompress
    decoded_text = huffman.decompress(encoded_text)
    print("Decoded Text:", decoded_text)

    # Check if original and decoded text match
    assert text == decoded_text, "Original and decoded texts do not match!"

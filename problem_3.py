import heapq
import sys


class Node:
    def __init__(self, frequency, character=None):
        self.frequency = frequency
        self.character = character
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __le__(self, other):
        return self.frequency <= other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __ge__(self, other):
        return self.frequency >= other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __ne__(self, other):
        return self.frequency != other.frequency


class HuffmanTree:
    def __init__(self, root=None):
        self.root = root

    def generate_codes(self):
        start_node = self.root

        # special case of one unique character
        if start_node.character:
            return {start_node.character: '0'}

        codes = {}
        stack = [(start_node, '')]

        while stack:
            current_node, current_code = stack.pop()
            if current_node.character:
                codes[current_node.character] = current_code
            else:
                stack.append((current_node.right, current_code + '1'))
                stack.append((current_node.left, current_code + '0'))
        return codes


def huffman_encoding(data):
    if data == '':
        return '', HuffmanTree()

    frequency_dict = {}
    for char in data:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1

    min_heap = [Node(f, c) for c, f in frequency_dict.items()]
    heapq.heapify(min_heap)

    while len(min_heap) > 1:
        left_child = heapq.heappop(min_heap)
        right_child = heapq.heappop(min_heap)

        total_frequency = left_child.frequency + right_child.frequency
        internal_node = Node(total_frequency)
        internal_node.left = left_child
        internal_node.right = right_child

        heapq.heappush(min_heap, internal_node)

    huffman_tree = HuffmanTree(min_heap[0])
    codes = huffman_tree.generate_codes()

    encoded = ''
    for char in data:
        encoded += codes[char]

    return encoded, huffman_tree


def huffman_decoding(data, huffman_tree):
    root = huffman_tree.root

    # special case of empty tree
    if not root:
        return ''

    # special case of one unique character
    if root.character:
        return data.replace('0', root.character)

    decoded = ''
    node = root
    for b in data:
        if b == '0':
            node = node.left
        if b == '1':
            node = node.right
        if node.character:
            decoded += node.character
            node = root
    return decoded


if __name__ == "__main__":
    messages = list()
    messages.append('a')
    messages.append('bbb')
    messages.append("The bird is the word")
    messages.append('AAAAAAABBBCCCCCCCDDEEEEEE')
    messages.append('')
    messages.append(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin maximus nec sem ac gravida. Phasellus "
        "eu libero hendrerit, tincidunt erat nec, luctus metus. Praesent et odio in nisi tempor gravida. Sed eu "
        "sem a libero tempor tempor. Cras ut neque commodo arcu sagittis pharetra. Vivamus at arcu non lorem "
        "sollicitudin sagittis. Vivamus scelerisque ex ac rhoncus faucibus. Sed blandit ante non dolor "
        "fringilla efficitur. In fringilla semper aliquet. Phasellus mattis, ante ac congue feugiat, "
        "felis nisl gravida magna, ac laoreet tortor est id nibh. "
    )
    for message in messages:
        print("The size of the data is: {}".format(sys.getsizeof(message)))
        print("The content of the data is: {}\n".format(message))

        encoded_data, tree = huffman_encoding(message)
        if message:
            encoded_size = int(encoded_data, base=2)
        else:
            encoded_size = sys.getsizeof(message)
        print("The size of the encoded data is: {}".format(sys.getsizeof(encoded_size)))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))

        print()

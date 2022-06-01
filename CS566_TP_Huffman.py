class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        # Probability of the symbol in the data
        self.prob = prob

        # Symbol in the data
        self.symbol = symbol

        # Left Node
        self.left = left

        # Right Node
        self.right = right

        # Tree decision - 0/1
        self.code = ''


# A function to write the code of the symbols by the Huffman tree
codes = dict()


def calc_codes(node, val=''):
    newVal = val + str(node.code)

    if node.left:
        calc_codes(node.left, newVal)
    if node.right:
        calc_codes(node.right, newVal)

    if not node.left and not node.right:
        codes[node.symbol] = newVal

    return codes


# Function to calculate the probabilities of the symbols in the data
def calc_prob(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) is None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols


# Function to compute Encoded data
def output_enc(data, coding):
    encoding_output = []
    for c in data:
        encoding_output.append(coding[c])

    string = ''.join([str(item) for item in encoding_output])
    return string


# Function to calculate the space consumed before and after encoding
def gain(data, coding):
    before_compression = len(data) * 8
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol])
    print("Space before compression :", before_compression, 'bits')
    print("Space after compression :", after_compression, 'bits')


def Huffman_Encoding(data):
    symbol_with_probs = calc_prob(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    print("Symbols in the given Data: ", symbols)
    print("Probabilities of the elements: ", probabilities)

    nodes = []

    # Converting symbols and probabilities into tree nodes
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))

    while len(nodes) > 1:
        # Sort them in ascending order
        nodes = sorted(nodes, key=lambda x: x.prob)

        right = nodes[0]
        left = nodes[1]

        left.code = 0
        right.code = 1

        # combine the two smallest nodes to create new node
        newNode = Node(left.prob + right.prob, left.symbol + right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = calc_codes(nodes[0])
    print("Symbols with codes", huffman_encoding)
    gain(data, huffman_encoding)
    encoded_output = output_enc(data, huffman_encoding)
    return encoded_output, nodes[0]


def Decoding(encoded_data, huffman_tree):
    tree_head = huffman_tree
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            huffman_tree = huffman_tree.right
        elif x == '0':
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.symbol is None and huffman_tree.right.symbol is None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.symbol)
            huffman_tree = tree_head

    string = ''.join([str(item) for item in decoded_output])
    return string


# Input and Explore!
data = input('Enter the data to be coded:')
print('Given Data:', data)
encoding, tree = Huffman_Encoding(data)
print("Encoded output", encoding)
print("Decoded Output", Decoding(encoding, tree))

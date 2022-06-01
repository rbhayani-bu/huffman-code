_**Abstract**_
In information theory, data compression, source coding, or bit-rate reduction is the process of encoding information using fewer bits than the original representation. It can be done with various algorithms according to the purpose and compression output requirements. One of the algorithm that has huge impact in the compression domain is “Huffman Code Algorithm”. Due to its nature of simplicity, it is highly used by many applications and it is widely used to solve the compression problem.

**Problem**
To reduce the size of the data by compression using algorithm and decoding it back to its original format.

**Input**
Raw text data that has alphabets and symbols

**Output**
Compression of the data with the original size and size after compression. Including representation of the symbols and character according to the algorithm steps.
Finally, decoding the data back to the original input.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**o	What is Huffman Code?**

Huffman coding is a lossless data compression algorithm, which is widely used in lots of big applications. Huffman coding (also known as Huffman Encoding) is technology that is the foundation of file compression. It is a technique of compressing data to reduce its size without losing any of the details.
1.	Developed by David Huffman in 1951, this technique is the basis for all data compression and encoding schemes
2.	It is a famous algorithm used for lossless data encoding
3.	It follows a Greedy approach, since it deals with generating minimum length prefix-free binary codes
4.	It uses variable-length encoding scheme for assigning binary codes to characters depending on how frequently they occur in the given text. The character that occurs most frequently is assigned the smallest code and the one that occurs least frequently gets the largest code

**o	How it Works?**

Each character is 8 bits long. Assume that any given string contains n characters in total. As a result, sending the string requires a total of 8 * n bits.
We can compress the string to a smaller size using the Huffman Coding technique.
Huffman coding forms a tree utilizing the character's frequencies before generating code foreach character.
Data must be decoded once it has been encoded. The same tree is used for decoding.
Huffman Coding uses the concept of prefix code to avoid any ambiguity in the decoding process, i.e., a code associated with a character should not appear in the prefix of any other code. The above-mentioned tree aids in the upkeep of the property.

**o	Complexity**

The time complexity for encoding each unique character based on its frequency is O(nlog n).
Extracting minimum frequency from the priority queue takes place 2*(n-1) times and its complexity is O(log n).
Thus, the overall complexity is O(nlog n).

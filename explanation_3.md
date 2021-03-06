The Huffman tree was formed by using min-heap structure that allows extracting the minimum element in O(log(n)) time. Addition of elements require the same time. Therefore, it is the perfect data structure for this problem. All other parts of the code require O(n) time. As a result, the total runtime is bounded by the extraction of n elements from the heap, where n is the number of unique characters in the string.
Encoding runtime: O(k + n*log(n)) where k is length of initial string.
Decoding runtime: O(k)
Space complexity: O(k).  The data compression is about 60% of initial size. 
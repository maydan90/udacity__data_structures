Blockchain was built as a linked list with a pointer to the tail.  Each element (block) of the linked list has pointer to the previous element so that all of them are connected.
Calculating the SHA256 hash takes O(n) time where n is the length of data. So adding k elements to the Blockchain will take O(k*n) time
Space complexity: O(k) where k is the total number of data blocks to store.
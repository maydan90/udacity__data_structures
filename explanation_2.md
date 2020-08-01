After checking initial directory for specific files, the recursion of the same function was called for all sub-folders.
Time complexity: O(n) where n is the total number of files in the folder and all sub-folders.
Space complexity: O(n) each recursive call stores info about current folder. 
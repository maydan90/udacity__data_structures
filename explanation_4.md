I just added users_set into the Group initialization for fast O(1) user lookup.  The rest is similar to the problem 2. The check if user is present was done in recursion for each sub-group.
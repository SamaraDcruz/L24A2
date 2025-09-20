# Given tuple
t = (1, 2, 3, 3, 2, 1)
print("Tuple:", t)

# Reverse the tuple
rev_t = t[::-1]
print("Reversed Tuple:", rev_t)

# Check palindrome
if t == rev_t:
    print("Yes, the tuple is a palindrome.")
else:
    print("No, the tuple is not a palindrome.")
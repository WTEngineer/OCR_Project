import re

def get_longest_word(text):
    # Use regex to find words, considering letters and digits
    words = re.findall(r'\b\w+\b', text)
    
    # Return the longest word or None if no words found
    return max(words, key=len) if words else None
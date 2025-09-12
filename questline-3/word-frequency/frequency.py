
import re
from collections import Counter

def word_frequency(text):
    """text.lower""" #makes every word into lower
    words = re.findall(r'\b\w+\b', text.lower())#counts all words
    
    #counts words
    freq = Counter(words)
    
    """freq.items""" #returns word and its count
        
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0])) #sorts into descending form
    
    for word, count in sorted_freq:
        print(f"{word} → {count}")

if __name__ == "__main__":
    paragraph = input("Enter a text paragraph:\n")
    word_frequency(paragraph)

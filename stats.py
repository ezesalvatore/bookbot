def get_num_words(text):
    words = text.split()
    return len(words)

def get_dict(book):
    freq_map = {}
    book = book.lower()
    for word in book:
        for c in word:
            if c.isalpha():
                if(c in freq_map):
                    freq_map[c] += 1
                else:
                    freq_map[c] = 1
    
    return freq_map
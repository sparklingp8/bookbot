def count_words(file_text):
    num_words = (len(file_text.split()))
    return f"{num_words}"

def characters_count(file_text):
    d={}
    for c in file_text:
        c = c.lower()
        x = d.get(c)
        if x:
            d[c] = x+1
        else:
            d[c]=1
    return d
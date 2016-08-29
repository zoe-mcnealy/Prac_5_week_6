text = "this is a collection of nice words this is a fun thing it is"


individual_words = text.lower() .split(" ")
text_dict = {}
for word in individual_words:
    text_dict[word] = individual_words.count(word)
print(text_dict)
sorted(text_dict)
for k,v in text_dict.items():
    print("{:{}}:{:{}}".format(k,10,v,2))

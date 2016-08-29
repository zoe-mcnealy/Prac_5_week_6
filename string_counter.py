text = "this is a collection of nice words this is a fun thing it is"

individual_words = text.lower() .split(" ")
text_dict = {}
for word in individual_words:
    if word in text_dict:
        text_dict[word] + 1
    else:
        text_dict[word] = 1
print(text_dict)


def create_sentence(indexes, words_string): 
    words_list = words_string.split() 
    new_sentence = ' '.join(words_list[i-1] for i in indexes) 
    return new_sentence.capitalize() 
indexes = [2, 4, 1, 3] 
words_string = "это предложение из примера"  
new_sentence = create_sentence(indexes, words_string) 
print(new_sentence) 

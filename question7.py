#Problem 7: Function-Based Word Frequency Analyzer
#Take a sentence from the user.
def count_words(sentence):
    words = sentence.lower().split()
    
    word_frequency = {}  
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1    
    return word_frequency
    
user_input = input()
result_dic = count_words(user_input)

words_list = user_input.lower().split()
total_words = len(words_list)
unique_words = len(result_dic)

most_frequency_word = None
max_frequency = 0

for word in words_list:
    if result_dic[word] > max_frequency:
        max_frequency = result_dic[word]
        most_frequency_word = word

print(f"Word Frequencies: {result_dic}")
print(f"Total Number of Words: {total_words}")
print(f"Number of Unique Words: {unique_words}")
print(f"Most Frequent Word: {most_frequency_word}")
import operator

def word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
        return num_words
    
def count_chars(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        lower_file_contents = file_contents.lower()
        count_of_chars = {}
        for char in lower_file_contents:
            if char.isalpha() == True:
                counter = lower_file_contents.count(char)
                count_of_chars[char] = counter
        return count_of_chars
    
def sort_count(count_of_chars):
    list_of_dict = []
    for char in count_of_chars:
        temp_dict={}
        count=count_of_chars[char]
        temp_dict["char"] = char
        temp_dict["num"] = count
        list_of_dict.append(temp_dict)
    def sort_on(list_of_dict):
        return list_of_dict["num"]
    sorted_list = list_of_dict.sort(reverse=True,key=sort_on)
    return list_of_dict


        
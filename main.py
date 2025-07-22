from stats import word_count, count_chars, sort_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    args = sys.argv
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = args[1] 
    num_words = word_count(file)
    print("============= BOOKBOT ============")
    print(f"Analyzing book found at {file}")
    print("----------- Word Count ----------")
    result_words = f"Found {num_words} total words"
    print(result_words)
    print("--------- Character Count -------")
    result_chars = count_chars(file)
    sorted_list = sort_count(result_chars)
    for item in sorted_list:
        letter = item["char"]
        number = item["num"]
        print(f"{letter}: {number}")
    print("============= END ===============") 



if __name__ == "__main__":
    main()
def main(): 
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
        lower_case_content = file_contents.lower()

        print("--- Begin report of books/frankenstein.txt ---")
        print(num_words, "words found in the document")

        char_count = {}

        for char in lower_case_content: 
            if char.isalpha():
                if char in char_count: 
                    char_count[char] += 1
                else: 
                    char_count[char] = 1

        for char, count in char_count.items(): 
            print(f"The '{char}' was foun {count} times ")
        print("--- End report ---")

main()

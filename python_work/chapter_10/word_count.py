
def count_word(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry,the file {filename} does not exist. ")
        with open('missing_files.txt', 'a', encoding='utf-8') as f:
            f.write(filename)
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words. ")


filename = 'alice.txt'
count_word(filename)

filenames = ['alice.txt', 'siddhartha1.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_word(filename)


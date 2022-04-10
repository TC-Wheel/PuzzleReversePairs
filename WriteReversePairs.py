def file_process(file_name):
    # this opens the english_dict.txt and returns a list
    with open(file_name, "r", encoding="utf8") as f:
        all_words = {}
        word_list = f.read().splitlines()
        for word in word_list:
            all_words[word] = True
    return all_words


def find_reverse_pairs(all_words):
    reverse_pairs = []
    for word in all_words:
        if word[::-1] in all_words:
            reverse_pairs.append((word, word[::-1]))
    return reverse_pairs


def main():
    all_words = file_process("english_dict.txt")
    reverse_pairs = sorted(
        find_reverse_pairs(all_words), key=lambda x: len(x[0]), reverse=True
    )
    with open("answers.txt", "w", encoding="utf8") as w:
        for pair in reverse_pairs:
            new_line = f"{pair[0].title()} & {pair[1]}\n"
            w.write(new_line)
        w.write(
            f"The total number of reverse pairs in English is: {len(reverse_pairs)}"
        )


if __name__ == "__main__":
    main()

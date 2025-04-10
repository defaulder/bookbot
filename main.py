from stats import *
import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	print("============ BOOKBOT ============")
	book_text = get_book_text(sys.argv[1])
	print("----------- Word Count ----------")
	num_words = get_number_of_words(book_text)
	print("Found 75767 total words")
	print("--------- Character Count -------")
	num_chars = get_number_of_characters(book_text)
	sorted = sort_dictionary(num_chars)
	for item in sorted:
		if item["key"].isalpha():
			print(f"{item["key"]}: {item["count"]}")


def get_book_text(path_to_file):
	with open(path_to_file) as f:
		print(f"Analyzing book found at {path_to_file}")
		file_content = f.read()
		return file_content


main()
def get_number_of_words(book_text):
	return len(book_text.split())


def get_number_of_characters(book_text):
	char_stat = {}
	book_text = book_text.lower()
	for char in book_text:
		if char not in char_stat:
			char_stat[char] = 0
		char_stat[char] += 1
		
	return char_stat

def sort_dictionary(dictionary):
	list = []
	for entry in dictionary:
		list.append({"key":entry, "count":dictionary[entry]})
	return list
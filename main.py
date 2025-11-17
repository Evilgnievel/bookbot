import sys

from stats import get_num_words
from stats import statistics
from stats import sorting

def get_book_text(path):
	with open(path) as text:
		file_contents = text.read()
	return file_contents


def main():
	
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		return sys.exit(1)

	path = sys.argv[1]
	content = get_book_text(path)
	words   = get_num_words(content)
	counts  = statistics(content)
	sorted  = sorting(counts)
	
	sorted_stats = sorting(counts)  # sortierte Liste aus deiner Funktion

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {words} total words")
	print("--------- Character Count -------")
	for entry in sorted_stats:
		char = entry["char"]
		if char.isalpha():
			print(f"{entry['char']}: {entry['num']}")
	print("============= END ===============")


main()
	




def get_num_words(content):
        words = content.split()
        return len(words)

def statistics(content):
	counts  = {}
	content = content.lower()
	
	for char in content:
		if char in counts:
			counts[char] += 1
		else:
			counts[char]  = 1
	return counts

def sorting(count):
	def get_num(entry):
		return entry["num"]

	stats_list = []
	for char, num in count.items():
		stats_list.append({"char": char, "num": num})

	stats_list.sort(key=get_num, reverse=True)

	return stats_list
	

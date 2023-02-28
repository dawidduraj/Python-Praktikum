# Zusammenarbeit mit folgenden Teilnehmern:
def comprehend(a):
	result = [[item.upper() for item in sub if item.upper()[0] != "Z"] for sub in a]
	return result
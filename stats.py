def spliting_text(text):
    # defining the file_contents to be empty first
    file_contents = ""
    # opening the file in read mode with utf-8 encoding
    with open(text, "r", encoding="utf-8") as f:
        # reading the contents of the file
        file_contents = f.read()
        # splitting the contents into words
        words = file_contents.split()
        # counting the number of words
        num_words = len(words) 
        # printing the number of words
        return num_words

""" Count how many times each character appears in the given text.
    Converts all characters to lowercase to avoid duplicates.
    Returns a dictionary mapping character -> count."""
def character_count(text: str,) -> dict[str, int]:
    # Convert the text to lowercase to ensure case insensitivity
    text = text.lower()

    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_characters(counts: dict[str, int]) -> list[dict[str, int]]:
    """
    Convert a dictionary of character counts into a sorted list of dictionaries.
    Each dictionary has keys 'character' and 'count'.
    Sorted in descending order by count.
    """
    # Convert dictionary items into list of dicts
    char_list = [{"character": char, "count": count} for char, count in counts.items()]
    
    # Sort the list by count (highest first)
    char_list.sort(key=lambda item: item["count"], reverse=True)  

    return char_list


def duplicate_count(text):
    text = text.lower()
    chars = {char: text.count(char) for char in text}
    return len([char for char in chars if chars[char] >=2 ])

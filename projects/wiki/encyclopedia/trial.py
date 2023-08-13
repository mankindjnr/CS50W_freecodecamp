def title_str(string):
    words = string.split()
    modified = [word.title() for word in words]
    return "_".join(modified)

print(title_str("amos"))
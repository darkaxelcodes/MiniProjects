text = str(input("Enter the text to convert to Acronym : "))
ignore = ["of", "on", "and", "for", "the", "is", "a", "an"]
full_form = text.split()
acronym = ""
for word in full_form:
    if word.lower() not in ignore:
        acronym += str(word[0]).upper() + "."
print(acronym)
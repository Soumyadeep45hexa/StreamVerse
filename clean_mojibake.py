import codecs

with codecs.open('c:/Snap Syntax/index.html', 'r', 'utf-8') as f:
    text = f.read()

replacements = [
    ('ðŸ’¡ ', 'Fact: '),
    ('ðŸ’¡', 'Fact: '),
    ('Â°', '°'),
    ('Ã©', 'é'),
    ('Ã¥', 'å'),
    ('â€”', '—'),
    ('â˜…', '★'),
    ('â˜†', '☆')
]

for old, new in replacements:
    text = text.replace(old, new)

with codecs.open('c:/Snap Syntax/index.html', 'w', 'utf-8') as f:
    f.write(text)

print("Done replacing.")

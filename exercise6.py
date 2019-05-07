def wrap_text(text1, text2):
    return f'{text2}{text1}{text2[::-1]}'

print(wrap_text('hello', '==='))
print(wrap_text('hello', '---===###'))
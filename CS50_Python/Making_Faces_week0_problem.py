def converter(text):
    return text.replace(":)", "[smile]").replace(":(", "[sad]")

def main():
    text = input()
    print(converter(text))


main()
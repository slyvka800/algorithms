
def create_position_dict(pattern):

    position = dict()

    for i in range(len(pattern)):
        position[pattern[i]] = i

    return position


def search(pattern, text):

    position = create_position_dict(pattern)

    text_len = len(text)
    pattern_len = len(pattern)

    text_index = pattern_len-1
    found_flag = False
    output = []

    while text_index < text_len:

        pattern_index = pattern_len-1
        while pattern_index >= 0:
            if pattern[pattern_index] != text[text_index]:
                break
            pattern_index -= 1
            text_index -= 1

        if pattern_index == -1:
            output.append(f'Found "{pattern}" in "{text}"')
            # print("Found", f'"{pattern}"', "in", f'"{text}"')
            found_flag = True
            text_index += pattern_len + 1
        else:
            shift = pattern_index+1
            if text[text_index] in position:
                shift = max(1, pattern_index - position[text[text_index]])
            text_index += (pattern_len - 1 - pattern_index + shift)

        if text_index >= text_len and not found_flag:
            # print("Not found", f'"{pattern}"', "in", f'"{text}"')
            output.append(f'Not found "{pattern}" in "{text}"')

    return output


if __name__ == '__main__':
    pattern = input()
    text = input()
    for i in search(pattern, text):
        print(i)

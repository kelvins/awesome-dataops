
def check_order(lines, match_pattern, stop_pattern):
    """Check the order based on the patterns."""
    data = list()
    for line in lines:
        if line.startswith(match_pattern):
            data.append(line)
        elif line.startswith(stop_pattern):
            if data != sorted(data, key=str.casefold):
                print(data)
                print(sorted(data, key=str.casefold))
                raise Exception('The content is not alphabetically sorted!')
            data = list()


def check_menu(lines, level):
    """Check if menu is alphabetically sorted."""
    match_pattern = f'{" " * level}-'
    stop_pattern = ('---', '- [')
    check_order(lines, match_pattern, stop_pattern)


def check_content(lines):
    """Check if content is alphabetically sorted."""
    match_pattern = '* ['
    stop_pattern = ('## ', '### ')
    check_order(lines, match_pattern, stop_pattern)


def main(path):
    """Check if menus are alphabetically sorted."""
    data = list()
    with open(path, 'r') as f:
        lines = f.readlines()
    check_menu(lines, level=4)
    check_menu(lines, level=8)
    check_content(lines)


if __name__ == '__main__':
    main('README.md')

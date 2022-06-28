formatted_string = []

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            formatted_string = format_string(i, j, major, minor)
    return len(major_colors) * len(minor_colors)

def format_string(i, j, major, minor):
    formatted_string.append('{:<15} | {:<15} | {:<15}.format(i, j, major, minor)')
    return formatted_string

result = print_color_map()
assert(result == 25)
assert(formatted_string[0].find("|") == formatted_string[24].find("|"))
print("All is well (maybe!)\n")

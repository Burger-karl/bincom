#Define the color lists for each day
monday_colors = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]
tuesday_colors = ["ASH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLUE", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE"]
wednesday_colors = ["GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE"]
thursday_colors = ["BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN"]
friday_colors = ["GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"]

all_days_colors = monday_colors + tuesday_colors + wednesday_colors + thursday_colors + friday_colors

#create a dictionary to count each color occurrence
color_counts = {}

#Count the occurrences of each color
for color in all_days_colors:
    if color in color_counts:
        color_counts[color] += 1
    else:
        color_counts[color] = 1

# Find the color with the highest count
most_worn_color = max(color_counts, key=color_counts.get)

print(f"The most worn color throughout the week is {most_worn_color}.")

# Create a dictionary to map color names to numerical values
color_dict = {
    'GREEN': 1,
    'YELLOW': 2,
    'BROWN': 3,
    'BLUE': 4,
    'PINK': 5,
    'ORANGE': 6,
    'CREAM': 7,
    'RED': 8,
    'WHITE': 9,
    'ASH': 10,
    # 'BLEW': 11,
    'BLACK': 11
}

#create the color series for each day
days = [
    ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    ['ASH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLUE', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE'],
    ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE'],
    ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']
]

#convert d color names to numerical values
color_values = [color_dict[color] for day in days for color in day]

#calculate mean
mean_color_value = sum(color_values) / len(color_values)

#calculate the variance
variance = sum((x - mean_color_value) ** 2 for x in color_values) / (len(color_values) - 1)

print(f"The variance of the colors is: {variance}")

def color_to_value(color):
    color_values = {
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
        'BLUE': 11, 
        'BLACK': 12
    }
    return color_values.get(color, 0)

def calculate_mean_color(colors):
    color_values = {
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
        'BLUE': 11, 
        'BLACK': 12
    }
    total_value = sum(color_to_value(color) for color in colors)
    mean_value = total_value / len(colors)
    for color, value in color_values.items():
        if value == round(mean_value):
            return color

#Define the color values for each day
days = {
    'MONDAY': ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    'TUESDAY': ['ASH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLUE', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE'],
    'WEDNESDAY': ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE'],
    'THURSDAY': ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    'FRIDAY': ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']
}

#Calculate the mean color for each day
for day, colors in days.items():
    mean_color = calculate_mean_color(colors)
    print(f'{day}: {mean_color}')

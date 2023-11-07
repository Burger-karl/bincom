import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    database="bincomdb",
    user="postgres",
    password="C1h2a3r4l5e6s7",
    host="localhost",
    port=""
)

# Create a cursor object
cur = conn.cursor()

# Define the color data
color_data = {
    "MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "FRIDAY": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
}

# Create the colors table
create_table_query = '''
    CREATE TABLE IF NOT EXISTS colors (
        id SERIAL PRIMARY KEY,
        day VARCHAR(10),
        color VARCHAR(20)
    )
'''

# Execute the SQL statement
cur.execute(create_table_query)

# Commit the changes
conn.commit()

# Iterate through the days and colors, and insert them into the database
for day, colors in color_data.items():
    color_list = colors.split(", ")
    for color in color_list:
        cur.execute("INSERT INTO colors (day, color) VALUES (%s, %s)", (day, color))

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

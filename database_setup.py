import sqlite3

# Connect to the database
conn = sqlite3.connect('live-notify.db')
cursor = conn.cursor()

# Create the table structure
cursor.execute('''
    CREATE TABLE IF NOT EXISTS twitch_users (
        user_id INTEGER PRIMARY KEY,
        twitch_username TEXT,
        notify_role_id INTEGER
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

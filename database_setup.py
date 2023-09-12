import sqlite3

# Connect to the database
conn = sqlite3.connect('live-notify.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS config (
        notify_channel_id INTEGER
    )
''')

# Create the table if it doesn't exist or modify it to match the expected structure
cursor.execute('''
    CREATE TABLE IF NOT EXISTS twitch_users (
        user_id INTEGER PRIMARY KEY,
        twitch_username TEXT,
        notify_channel_id INTEGER,
        notify_role_id INTEGER,
        oauth_token TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

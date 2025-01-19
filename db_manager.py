def create_database_if_not_exist(conn, cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS activity (
    activity_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    UNIQUE(title));""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS activity_log (
    activity_log_id INTEGER PRIMARY KEY,
    date DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    activity_id INTEGER NOT NULL,
    finished INTEGER NOT NULL DEFAULT 0 CHECK (finished IN (0, 1)),
    time_goal REAL CHECK (time_goal >= 0),
    time_spent REAL CHECK (time_spent >= 0),
    UNIQUE(date, activity_id),
    FOREIGN KEY (activity_id) REFERENCES activity(activity_id));""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS note_log (
    note_log_id INTEGER PRIMARY KEY,
    date DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    text TEXT NOT NULL,
    category INTEGER NOT NULL DEFAULT 0 CHECK (category IN (0, 1, 2)));""")
    
    conn.commit()

def get_daily_activity_logs(cursor, date):
    cursor.execute(f"""SELECT activity.title
    FROM activity_log
    JOIN activity ON activity_log.activity_id = activity.activity_id
    WHERE activity_log.date = '{date}'""")
    
    return cursor.fetchall()

def get_daily_note_logs(cursor, date):
    cursor.execute(f"""SELECT note_log.text
    FROM note_log
    WHERE note_log.date = '{date}'""")
    
    return cursor.fetchall()
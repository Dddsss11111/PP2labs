import psycopg2

def _connect():
    return psycopg2.connect(
        dbname="lab10_snake",
        user="postgres",
        password="Gitler1939",
        host="localhost",
        port=5432
    )

def init_db():
    conn = _connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            user_id INT REFERENCES users(id) ON DELETE CASCADE,
            score INT DEFAULT 0,
            level INT DEFAULT 1,
            PRIMARY KEY (user_id)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def find_or_create_player(name):
    conn = _connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (name,))
    row = cur.fetchone()
    if row:
        uid = row[0]
        cur.execute("SELECT score, level FROM user_score WHERE user_id = %s", (uid,))
        r = cur.fetchone()
        if r:
            score, level = r
        else:
            cur.execute("INSERT INTO user_score (user_id) VALUES (%s)", (uid,))
            conn.commit()
            score, level = 0, 1
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (name,))
        uid = cur.fetchone()[0]
        cur.execute("INSERT INTO user_score (user_id) VALUES (%s)", (uid,))
        conn.commit()
        score, level = 0, 1
    cur.close()
    conn.close()
    return uid, score, level

def persist_progress(user_id, score, level):
    conn = _connect()
    cur = conn.cursor()
    cur.execute("UPDATE user_score SET score=%s, level=%s WHERE user_id=%s", (score, level, user_id))
    conn.commit()
    cur.close()
    conn.close()

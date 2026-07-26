import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

DB_NAME = "careerpilot.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        email TEXT UNIQUE,

        password TEXT

    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS analysis_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        email TEXT,

        ats_score INTEGER,

        matched_skills TEXT,

        missing_skills TEXT,

        optimized_resume TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()
    conn.close()


def create_user(name,email,password):

    conn=get_connection()

    cur=conn.cursor()

    try:

        cur.execute("""

        INSERT INTO users(name,email,password)

        VALUES(?,?,?)

        """,(name,email,generate_password_hash(password)))

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()


def verify_user(email,password):

    conn=get_connection()

    cur=conn.cursor()

    cur.execute("""

    SELECT *

    FROM users

    WHERE email=?

    """,(email,))

    user=cur.fetchone()

    conn.close()

    if user and check_password_hash(user["password"],password):

        return dict(user)

    return None


def save_analysis(

    email,

    ats_score,

    matched,

    missing,

    optimized

):

    conn=get_connection()

    cur=conn.cursor()

    cur.execute("""

    INSERT INTO analysis_history(

    email,

    ats_score,

    matched_skills,

    missing_skills,

    optimized_resume

    )

    VALUES(?,?,?,?,?)

    """,(

    email,

    ats_score,

    matched,

    missing,

    optimized

    ))

    conn.commit()

    conn.close()


def get_history(email):

    conn=get_connection()

    cur=conn.cursor()

    cur.execute("""

    SELECT *

    FROM analysis_history

    WHERE email=?

    ORDER BY created_at DESC

    """,(email,))

    rows=cur.fetchall()

    conn.close()

    return rows


init_db()
import sqlite3

def init_db():
    conn = sqlite3.connect('math_definitions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS definitions
                 (id INTEGER PRIMARY KEY, term TEXT, definition TEXT)''')
    # Sample data
    c.execute("INSERT OR IGNORE INTO definitions (term, definition) VALUES (?, ?)",
              ("Set", "A collection of distinct objects, considered as an object in its own right."))
    c.execute("INSERT OR IGNORE INTO definitions (term, definition) VALUES (?, ?)",
              ("Graph", "A structure consisting of vertices and edges connecting pairs of vertices."))
    conn.commit()
    conn.close()

def search_definitions(query):
    conn = sqlite3.connect('math_definitions.db')
    c = conn.cursor()
    c.execute("SELECT term, definition FROM definitions WHERE term LIKE ?", ('%' + query + '%',))
    results = c.fetchall()
    conn.close()
    return results
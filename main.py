from fastapi import FastAPI
import sqlite3


def get_vocabularies():
    conn = sqlite3.connect('dictionary.db')
    cursor = conn.cursor()

    cursor.execute('SELECT k, v FROM my_vacabulary order by cdt desc')
    data = cursor.fetchall()
    conn.close()
    return dict(data)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/vocabularies")
async def read_vocabularies():
    return get_vocabularies()

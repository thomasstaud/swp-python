from flask import Flask, request
import sqlite3
import yaml

app = Flask(__name__)

config = yaml.safe_load(open('config.yml'))
database = config['database']
table = config['table']


def setup_db(columns):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    query = 'CREATE TABLE IF NOT EXISTS statistics ('
    for column in columns:
        query += f'{column} INTEGER, '
    query = query[:-2] + ')'

    print("executing: ", query)
    cursor.execute(query)


def update_table(columns):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    try:
        cursor.execute(f'SELECT * FROM {table}')
    except sqlite3.OperationalError:
        setup_db(columns)
        cursor.execute(f'SELECT * FROM {table}')
    existing_columns = [description[0] for description in cursor.description]

    # magic???
    if all(item in existing_columns for item in columns):
        print('all columns exist')
        return

    # add columns
    base_query = f'ALTER TABLE {table} ADD COLUMN '
    for column in columns:
        if column not in existing_columns:
            query = base_query + column
            print("executing: ", query)
            cursor.execute(query)


def store_statistics(stats):
    columns = list(stats.keys())
    update_table(columns)

    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    # save data to db
    query = 'INSERT INTO statistics ('
    for key in stats.keys():
        query += f'{key}, '
    query = query[:-2] + ') VALUES ('
    for key in stats.keys():
        query += f'{stats[key]}, '
    query = query[:-2] + ')'

    print("executing: ", query)
    cursor.execute(query)
    connection.commit()


@app.route('/statistics', methods=['POST'])
def post_statistics():
    if request.is_json:
        store_statistics(request.json)
        return 'Success!'
    else:
        return 'Error: Body must be JSON object'


if __name__ == '__main__':
    app.run(debug=True)

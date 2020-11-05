# this code will help in making a simple database with CRUD operations using sqlite3 in python

import sqlite3

def insert(db, row):
    """
    Insert a new database

    Args:
        db: (todo): write your description
        row: (int): write your description
    """
    db.execute('insert into test (t1, i1) values (?, ?)', (row['t1'], row['i1']))
    db.commit()

def retrieve(db, t1):
    """
    Retrieve a cursor from the database.

    Args:
        db: (todo): write your description
        t1: (str): write your description
    """
    cursor = db.execute('select * from test where t1 = ?', (t1,))
    return cursor.fetchone()

def update(db, row):
    """
    Update the database

    Args:
        db: (todo): write your description
        row: (int): write your description
    """
    db.execute('update test set i1 = ? where t1 = ?', (row['i1'], row['t1']))
    db.commit()

def delete(db, t1):
    """
    Delete the database.

    Args:
        db: (todo): write your description
        t1: (str): write your description
    """
    db.execute('delete from test where t1 = ?', (t1,))
    db.commit()

def disp_rows(db):
    """
    Disp_rows

    Args:
        db: (todo): write your description
    """
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print('  {}: {}'.format(row['t1'], row['i1']))

def main():
    """
    Main function.

    Args:
    """
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row
    print('Create table test')
    db.execute('drop table if exists test')
    db.execute('create table test ( t1 text, i1 int )')

    print('Create rows')
    insert(db, dict(t1 = 'one', i1 = 1))
    insert(db, dict(t1 = 'two', i1 = 2))
    insert(db, dict(t1 = 'three', i1 = 3))
    insert(db, dict(t1 = 'four', i1 = 4))
    disp_rows(db)

    print('Retrieve rows')
    print(dict(retrieve(db, 'one')), dict(retrieve(db, 'two')))

    print('Update rows')
    update(db, dict(t1 = 'one', i1 = 101))
    update(db, dict(t1 = 'three', i1 = 103))
    disp_rows(db)

    print('Delete rows')
    delete(db, 'one')
    delete(db, 'three')
    disp_rows(db)

if __name__ == "__main__": main()

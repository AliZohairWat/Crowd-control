import sqlite3

conn = sqlite3.connect('backend_python.sqlite3')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Data_Sheet ')

cur.execute('CREATE TABLE Data_Sheet (PNumber INTEGER, Queue INTEGER, Status BOOLEAN)')

cur.execute('INSERT INTO Data_Sheet (PNumber, Queue, Status) VALUES ( ?, ?, ? )', 
    ( 12345678, 1, False ) )
cur.execute('INSERT INTO Data_Sheet (PNumber, Queue, Status) VALUES ( ?, ?, ? )', 
    ( 1233567, 2, True ) )
cur.execute('INSERT INTO Data_Sheet (PNumber, Queue, Status) VALUES ( ?, ?, ? )', 
    ( 123456, 1, False ) )
cur.execute('INSERT INTO Data_Sheet (PNumber, Queue, Status) VALUES ( ?, ?, ? )', 
    ( 12345, 4, False ) )
cur.execute('INSERT INTO Data_Sheet (PNumber, Queue, Status) VALUES ( ?, ?, ? )', 
    ( 1234, 1, True ) )


def step8(Number_of_people, Queue_number):
    total = 0
    cur.execute('SELECT PNumber FROM Data_Sheet WHERE Status = 0 AND Queue = %s' % Queue_number)
    cur.execute('SELECT * FROM Data_Sheet WHERE Status = 0 AND Queue = %s'
                % Queue_number)
    for row in cur:
        total += 1
        return (list(row))
        if total >= Number_of_people:
            break
    cur.execute('UPDATE Data_Sheet SET Status = 1 WHERE Status = 0 AND Queue = %s' % Queue_number)
    cur.execute('DELETE FROM Data_Sheet WHERE Status = 1')
    
    
step8(2, 1)
    
    
    
    
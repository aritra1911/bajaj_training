import psycopg2

def main() -> None:
    con = psycopg2.connect('dbname=bajaj user=postgres password=Finserv@2023')
    cur = con.cursor()
    cur.execute('drop table if exists test;')
    cur.execute('''
        create table test (
            id serial primary key,
            num integer,
            data varchar
        );
    ''')
    cur.execute(
        'insert into test (num, data) values (%s, %s);', (101, 'maths')
    )
    cur.execute(
        'insert into test (num, data) values (%s, %s);', (102, 'computer')
    )
    cur.execute('update test set data = \'chemistry\' where id = 1;')
    cur.execute('select * from test;')
    #print(cur.fetchone())
    print(cur.fetchall())
    #print(cur.fetchmany())
    cur.execute('delete from test where id = 2;')
    con.commit()
    cur.close()
    con.close()

if __name__ == '__main__':
    main()
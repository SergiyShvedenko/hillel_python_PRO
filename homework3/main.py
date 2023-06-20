import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/phone/create')
def phone_create():
    phone = request.args.get('phone')
    phoneValue = request.args.get('phoneValue')
    con = sqlite3.connect("example.db")
    cur = con.cursor()

    sql = f'''
    INSERT INTO Phones (contactName, phoneValue)
    VALUES ('{phone}', '{phoneValue}')
    '''
    cur.execute(sql)

    con.commit()
    con.close()

    return 'phone_create'


@app.route('/phone/read')
def phone_read():
    con = sqlite3.connect("example.db")
    cur = con.cursor()

    sql = f'''
    SELECT * FROM Phones;
        '''
    cur.execute(sql)

    result = cur.fetchall()
    con.close()
    return str(result)


@app.route('/phone/update')
def phone_update():
    phone = request.args.get('phone')
    phoneValue = request.args.get('phoneValue')
    con = sqlite3.connect("example.db")
    cur = con.cursor()

    sql = f'''
    UPDATE Phones
    SET phoneValue = '{phoneValue}'
    WHERE contactName = '{phone}'
    '''
    cur.execute(sql)

    con.commit()
    con.close()

    return 'phone_update'


@app.route('/phone/delete')
def phone_delete():
    phone = request.args.get('phone')
    con = sqlite3.connect("example.db")
    cur = con.cursor()

    sql = f'''
    DELETE FROM Phones
    WHERE contactName = '{phone}'
    '''
    cur.execute(sql, (phone,))

    con.commit()
    con.close()

    return 'phone_delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
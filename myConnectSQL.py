import MySQLdb
import sys

if __name__ == '__main__':
    print 'input info: host|port|user|passwd|database|sql'
    argv_len = len(sys.argv) - 1
    if argv_len != 6:
        print 'invalid argv!'
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        user = sys.argv[3]
        passwd = sys.argv[4]
        database = sys.argv[5]
        sql = sys.argv[6]
        print 'try to connect...'
        db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=database, port=port)
        print 'connected successfully!'
        cursor = db.cursor()
        print "execute sql: %s" % sql
        cursor.execute(sql)
        for row in cursor.fetchall():
            print row

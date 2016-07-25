import pg

db = pg.DB(dbname='github_db')

query = db.query('select * from coder')
print query

named_result = query.namedresult()
for coder in named_result:
  print "Coder: %s, ID: %r" % (coder.name, coder.id)

# insert new rows db.insert('database', key1="value1", key2="value2")
# db.insert('coder', name='Riri Williams', email='riri@smail.com')

# db.update('coder', {'id': 14, 'email': ''})

# db.delete('coder', {'id': 13})

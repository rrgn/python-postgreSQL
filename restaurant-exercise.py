import pg

db = pg.DB(dbname="restaurant_db2")

query = db.query('select * from restaurant')
print query

##### insert restaurant #####

# input_name = raw_input('Enter a restaurant name: ')
# input_category = raw_input('Enter category for restaurant: ')
#
# db.insert('restaurant', name=input_name, category=input_category)
#
# query = db.query('select * from restaurant')
# print query

## end of insert restaurant ##

##### update database entry #####

# input_id = int(raw_input('Enter ID of restaurant to update: '))
# input_name = raw_input('Enter an updated restaurant name: ')
# input_category = raw_input('Enter a category for updated restaurant: ')
#
# db.update('restaurant', {'id': input_id, 'name': input_name, 'category': input_category})
#
# query = db.query('select * from restaurant')
# print query

## end of update database ##

##### delete entry from database #####

input_id = int(raw_input('Enter ID of restaurant to delete: '))

db.delete('restaurant', {'id': input_id})

query = db.query('select * from restaurant')
print query

## end of delete entry ##

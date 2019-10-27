# SimpleMySQL

SimpleMySQL is a wrapper for a simple handling of MySQL databases, so you don't have to use MySQL statements anymore.
You can easily handle your database by instances of the tables.

SimpleMySQL doesn't provide full MySQL possibilities and it can only be used for one database.

## Examples

### Frame
```Python
import simple_mysql as sql

database = sql.connect(host = "localhost", user = 'root', passwd = 'yourpassword', database = 'test')  # set login information

employees = database.create_table('employees')  # create an instance for your table
```

### Insert
```Python
employees.insert({'firstname': 'Linus', 'lastname': 'Bartsch'})  # manage the data easy without MySQL query
```

### Get

#### Get one row:
```Python
employees.get('id', 1337)
```
Receive dictionaries instead of tuples:
```json
{"id": 1337, "firstname": "Linus", "lastname": "Bartsch"}
```

#### Fetch more than one row and return only one column
```Python
employee.get('lastname', 'Johnson', fetch='all', only_column='firstname')  # 'fetch' can also be an integer
```
```
['John', 'Jake']
```


#### Get all rows without filter:
```python
employees.get_all()  # you could also use the 'only_column' parameter here
```
```json
[{"id": "1", "firstname": "Chuck", "lastname": "Norris"}, {"id": "42", "firstname": "John", "lastname": "Johnson"}, {"id": "1337", "firstname": "Linus", "lastname": "Bartsch"}, {"id": "9001", "firstname": "Jake", "lastname": "Johnson"}]
```

### Update
```Python
employees.update('id', 1337, {'lastname': 'Torvalds'})
```

### Delete
```Python
employees.delete('id', 1337)
```

### Create new table
```Python
from variables import *
table = sql.create_table("customers",
            Column("firstname", TEXT, not_null=True),
            Column("lastname", TEXT, not_null=True),
            Column("email", TEXT, not_null=True, unique=True),
            Column("prime_member", INTEGER, default=0),
            Column("delivery_address", TEXT)
            )
```

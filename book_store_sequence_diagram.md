<!-- cmd + shift + v to open the diagram preview -->
```mermaid
sequenceDiagram
    participant t as terminal
    participant app as Main program <br /> (in app.py)
    participant ar as BookRepository class <br /> (in lib/books.py)
    participant db_conn as DatabaseConnection class <br /> (in lib/book_store.py)
    participant db as Postgres database

    Note left of t: Flow of time <br />⬇ <br /> ⬇ <br /> ⬇ 

    t->>app: Runs `python app.py`
    app->>db_conn: Opens connection to database by calling connect method on Database Connection
    db_conn->>db_conn: Opens database connection using PG and stores the connection
    app->>ar: Calls all method on BookRepository
    ar->>db_conn: Sends SQL query by calling execute method on DatabaseConnection
    db_conn->>db: Sends query to database via the open database connection
    db->>db_conn: Returns a list of dictionaries, one for each row of the books table

    db_conn->>ar: Returns a list of dictionaries, one for each row of the books table
    loop 
        ar->>ar: Loops through list and creates a Book object for every row
    end
    ar->>app: Returns list of Book objects
    app->>t: Prints list of books to terminal
```
<!-- ```mermaid First Challenge, Correct the code. 
sequenceDiagram
    participant t as terminal
    participant app as Main program (in app.py)
    participant ar as ____ class <br /> (in lib/____.py)
    participant db_conn as ____ class in (in lib/____.py)
    participant db as Postgres database

    Note left of t: Flow of time <br />⬇ <br /> ⬇ <br /> ⬇ 

    t->>app: Runs `python ____`
    app->>db_conn: Opens connection to database by calling ____ method on ____
    db_conn->>db_conn: Opens database connection using PG and stores the connection
    app->>ar: Calls ____ method on ____
    ar->>db_conn: Sends SQL query by calling ____ method on ____
    db_conn->>db: Sends query to database via the open database connection
    db->>db_conn: Returns an ____ of ____, one for each row of the ____ table

    db_conn->>ar: Returns an ____ of ____, one for each row of the ____ table
    loop 
        ar->>ar: Loops through ____ and creates a ____ object for every row
    end
    ar->>app: Returns ____ of ____ objects
    app->>t: Prints list of ____ to terminal
``` -->
<!-- Create a sequence diagram for the album_repository. Make sure your diagram includes all of the challenge you completed in the previous section. Once you finish, upload your diagram and video to Aptem.

Make sure your diagram includes the following:
--The terminal
--The main program (app.py)
--The repository class
--The database connection class
--The database -->

```mermaid 
sequenceDiagram
    participant t as Terminal <br /> external actor, trigger point <br /> does not think
    participant app as Main Program app.py <br /> orchestrator, does not know SQL, <br /> does not know database details
    participant rep as AlbumRepository <br /> translates database rows <br />into domain objects
    participant db_conn as DatabaseConnection Class <br /> it opens and manages the connection <br /> and it executes the SQL
    participant db as Postgres Database <br /> an external system, it never initiates <br /> only responds and returns raw data.  

    t->>app: terminal triggers program <br /> runs 'python app.py'
    app->>db_conn: opens connection to db <br /> calls method on DatabaseConnection
    db_conn->>db_conn: opens database connection using PG and stores the connection
    app->>rep: the app asks the repository for all the albums
    rep->>db_conn: repository sends SQL query the database via a db connection
    db_conn->>db: DatabaseConnection is open <br /> and sends query to database
    db->>db_conn: database returns a list of dicts <br /> one for each row of the album table
    db_conn->>rep: DatabaseConnection Class now has control and returns a list of dict <br /> one dict for each row in album table
    loop
        rep->>rep: AlbumRepository Class Loops through list <br /> to create an Album object for every row
    end
    rep->>app: repository converts rows <br /> returns list of Album objects
    app->>t: prints list of albums to terminal 

```
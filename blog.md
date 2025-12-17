TWO TABLES DESIGN RECIPE

USER STORIES:
----analyse only the relevant part(s)
As a blogger
--So I can write interesting stuff
--I want to write posts having a title.

As a blogger
--So I can write interesting stuff
--I want to write posts having a content.

As a blogger
--So I can let people comment on interesting stuff
--I want to allow comments on my posts.

As a blogger
--So I can let people comment on interesting stuff
--I want the comments to have a content.

As a blogger
--So I can let people comment on interesting stuff
--I want the author to include their name in comments.

USER NOUNS: posts, title, content, comments, content, author_name

INFERED TABLE:
| Record            | Properties                    |
|--------------     |-----------------              |
| post              | title, post_content           |
| comment           | comment_content, author       |

FIRST TABLE NAME:(always plural)
posts
TABLE COLUMNS: (column name and data type)
    id: SERIAL
    title: text
    post_content: text
    comment: text

SECOND TABLE NAME:(always plural)
comments
TABLE COLUMNS: (column name and data type)
    id: SERIAL
    comment_content: text
    author: text

TABLES RELATIONSHIP
----If one-to-many, to work out which one has foreign key ask 
----can one thing1 have many thing2's? and visa versa. 

Check you can articulate
Option 1 : a post can have many comments, so comments belong to posts
Option 2 : a comment can have many posts... does not make sense. 

As such the foreign key will be on comments. 

WRITE SQL
    file: blog_basic.sql
---- parent table, create table without foreign key first
    CREATE TABLE posts (
        id SERIAL PRIMARY KEY,
        title text,
        post_content text,
        comment text,
    );

    CREATE TABLE comments (
        id SERIAL PRIMARY KEY,
        comment_content text,
        author text,
        post_id datatype,
        constraint fk_post foreign key(post_id)
            references posts(id)
            on delete cascade
    );

----constraint configures the database to delete related records
----so there are no orphan records, done using an on delete cascade SQL option

INPUT file.SQL CODE
INPUT SEED INFO

RUN SQL
    psql blog_basic < seeds/blog_basic.sql


DIAGRAMMING IF USEFUL e.g. 
--------------------    -------------------
|   concerts        |   |      venues      |
|                   |   |                  |
| id                | ->|   id             |
| artist_name       |   |   name           |
| scheduled_date    |   |   capacity       |
| venue_id          |   |                  |
_____________________   ___________________
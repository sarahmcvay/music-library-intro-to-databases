USER STORIES:
-- as a coach (user)
    So I can get to know all students,
    I want to see a list of students names. 

-- as a coach (user)
    so I can get to know all students, 
    I want to see a list of their cohorts. 

USER NOUNS: name, cohort

DATA OVERVIEW:

| Record           | Properties         |
|--------------    |-----------------   |
| student          | name, cohort       |

TABLE NAME:(always plural)
    students 

TABLE COLUMNS: (column name and data type)
    id: SERIAL
    name: text
    cohort: int

WRITE SQL
    file: student_directory_1.sql
    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        name text,
        cohort int
    );

INPUT file.SQL CODE
INPUT SEED INFO

RUN SQL
    psql student_directory_1 < path/student_directory_1.sql



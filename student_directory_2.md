TWO TABLES DESIGN RECIPE

USER STORIES:
(analyse only the relevant part(s))
As a coach
--So I can get to know all students
--I want to see a list of students' names.

As a coach
--So I can get to know all students
--I want to see a list of cohorts' names.

As a coach
--So I can get to know all students
--I want to see a list of cohorts' starting dates.

As a coach
--So I can get to know all students
--I want to see a list of students' cohorts.

USER NOUNS: students, names, cohorts, starting-dates

INFERED TABLE:
| Record            | Properties         |
|--------------     |-----------------   |
| student           | name, cohort       |
| cohort            | starting_date      |

FIRST TABLE NAME:(always plural)
students
TABLE COLUMNS: (column name and data type)
    id: SERIAL
    name: text
    cohort: text

SECOND TABLE NAME:(always plural)
cohorts
TABLE COLUMNS: (column name and data type)
    id: SERIAL
    starting_date: date

RELATIONSHIP
Option 1 - A student can be part of many cohorts, the cohort does not belong to the student.
Option 2 - A cohort will contain many students, the students belong to a cohort.

As such I would put the foreign key on the students. 

#Is there an argument for a many to many here?  
#Where you can answer yes to both sides a Many-to-Many relationsihp is implemented which requires a join table

WRITE SQL
    file: student_directory_2.sql
(create table without foreign key first)

    CREATE TABLE cohorts (
        id SERIAL PRIMARY KEY,
        starting_date date
    );

    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        name text,
        cohort text,
        cohort_id datatype,
        constraint fk_cohort foreign key(cohort_id)
            references cohorts(id)
            on delete cascade
    );

INPUT file.SQL CODE
INPUT SEED INFO

RUN SQL
    psql student_directory_2 < seeds/student_directory_2.sql

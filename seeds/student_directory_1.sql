CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        name text,
        cohort int
)

INSERT INTO students (name, cohort) VALUES ('Sarah', 2025);
INSERT INTO students (name, cohort) VALUES ('Kathleen', 2025);
INSERT INTO students (name, cohort) VALUES ('Mitch', 2025);
INSERT INTO students (name, cohort) VALUES ('Will', 2024);
INSERT INTO students (name, cohort) VALUES ('Tariq', 2023);
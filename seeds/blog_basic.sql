-- file: blog_basic.sql

DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;


CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    post_content text,
    comment text
);

CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    comment_content text,
    author text,
    post_id int,
    constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);


INSERT INTO posts (title, post_content) VALUES ('Makers', 'Homework Complete!');
INSERT INTO posts (title, post_content) VALUES ('Challenge', 'This was fun');

INSERT INTO comments (comment_content, author, post_id) VALUES ('great work', 'Hunor', 1);
INSERT INTO comments (comment_content, author, post_id) VALUES ('I liked it too', 'Jack', 2);





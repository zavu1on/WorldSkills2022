CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL
);
CREATE TABLE newspapers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(128) NOT NULL,
    user_id INT FOREIGN KEY REFERENCES users(id)
);

INSERT INTO users (username, password) VALUES ('John', 'J0hn');
INSERT INTO newspapers (title, user_id) VALUES ('Hello World!', 1)

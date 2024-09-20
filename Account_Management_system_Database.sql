CREATE DATABASE account_management_system;
USE account_management_system;

CREATE TABLE companies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    role ENUM('main-admin', 'owner', 'admin', 'user'),
    company_id INT,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

ALTER TABLE companies 
ADD owner_id INT;

CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT,
    income FLOAT DEFAULT 0,
    expenses FLOAT DEFAULT 0,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT,
    user_id INT,
    amount FLOAT,
    is_approved BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (company_id) REFERENCES companies(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO companies (name) 
VALUES ('Enigmatix'), ('Googly');

INSERT INTO users (name, role, company_id) 
VALUES 
('Usman', 'main-admin', 1), 
('Arslan', 'owner', 1),
('Abdul_Rehman', 'admin', 2),
('Ahmad', 'user', 2);

UPDATE companies 
SET owner_id = 2
WHERE id = 1;

UPDATE companies 
SET owner_id = 4
WHERE id = 2;

INSERT INTO accounts (company_id, income, expenses)
VALUES 
(1, 10000, 5000),
(2, 20000, 8000);

INSERT INTO expenses (company_id, user_id, amount, is_approved)
VALUES
(1, 1, 300, TRUE),
(2, 3, 150, FALSE);

SELECT * FROM companies;
SELECT * FROM users;
SELECT * FROM accounts;
SELECT * FROM expenses;
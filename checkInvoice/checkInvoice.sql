-- 產生資料表發票本(invoice_books)
-- CREATE TABLE invoice_books (
--     id SERIAL PRIMARY KEY,
--     track VARCHAR(2) NOT NULL,
--     begin_number INT NOT NULL,
--     end_number INT NOT NULL,
--     year INT NOT NULL,
--     month INT NOT NULL,
--     created_at TIMESTAMP NOT NULL,
--     updated_at TIMESTAMP NOT NULL
-- );

-- 填入資料表發票本(invoice_books)正確資料 
-- INSERT INTO invoice_books (track, begin_number, end_number, year, month, created_at, updated_at) VALUES
-- ('AA', 12345600, 12345649, 113, 3, '2024-03-01 00:00:00', '2024-03-10 12:00:00'),
-- ('AB', 98765400, 98765449, 113, 3, '2024-03-01 00:00:00', '2024-03-15 12:00:00'),
-- ('AC', 45678900, 45678999, 113, 3, '2024-03-01 00:00:00', '2024-03-20 12:00:00');

-- 填入資料表發票本(invoice_books)錯誤資料 
-- INSERT INTO invoice_books (track, begin_number, end_number, year, month, created_at, updated_at) VALUES
-- ('1A', 12345600, 12345649, 113, 3, '2024-03-01 00:00:00', '2024-03-10 12:00:00'),
-- ('2B', 98765400, 98765449, 113, 3, '2024-03-01 00:00:00', '2024-03-15 12:00:00'),
-- ('3C', 45678900, 45678999, 113, 3, '2024-03-01 00:00:00', '2024-03-20 12:00:00');

-- 產生每張發票開立的紀錄表 (invoices)
-- CREATE TABLE invoices (
--     id SERIAL PRIMARY KEY,
--     invoice_number VARCHAR(15) NOT NULL,
--     invoice_date DATE NOT NULL,
--     created_at TIMESTAMP NOT NULL,
--     updated_at TIMESTAMP NOT NULL
-- );

-- 填入每張發票開立的紀錄表 (invoices) 正確資料 
-- INSERT INTO invoices (invoice_number, invoice_date, created_at, updated_at) VALUES
-- ('AA-12345600', '2024-03-01', '2024-03-01 09:00:00', '2024-03-01 09:00:00'),
-- ('AA-12345601', '2024-03-01', '2024-03-01 09:10:00', '2024-03-01 09:10:00'),
-- ('AB-98765400', '2024-03-02', '2024-03-02 10:00:00', '2024-03-02 10:00:00'),
-- ('AC-45678900', '2024-03-03', '2024-03-03 11:00:00', '2024-03-03 11:00:00'),
-- ('AC-45678901', '2024-03-04', '2024-03-04 12:00:00', '2024-03-04 12:00:00'),
-- ('AC-45678988', '2024-03-31', '2024-03-31 22:10:30', '2024-03-31 22:10:30');

-- 填入每張發票開立的紀錄表 (invoices) 錯誤資料 
-- INSERT INTO invoices (invoice_number, invoice_date, created_at, updated_at) VALUES
-- ('1A-12345600', '2024-03-01', '2024-03-01 09:00:00', '2024-03-01 09:00:00'),
-- ('2A-12345601', '2024-03-01', '2024-03-01 09:10:00', '2024-03-01 09:10:00'),
-- ('3B-98765400', '2024-03-02', '2024-03-02 10:00:00', '2024-03-02 10:00:00'),
-- ('1C-45678900', '2024-03-03', '2024-03-03 11:00:00', '2024-03-03 11:00:00'),
-- ('2C-45678901', '2024-03-04', '2024-03-04 12:00:00', '2024-03-04 12:00:00'),
-- ('3C-45678988', '2024-03-31', '2024-03-31 22:10:30', '2024-03-31 22:10:30');

-- 查詢正確和錯誤的發票號碼
WITH correct_invoices AS (
    SELECT 
        'AA' AS track, generate_series(12345600, 12345649) AS number
    UNION ALL
    SELECT 
        'AB' AS track, generate_series(98765400, 98765449) AS number
    UNION ALL
    SELECT 
        'AC' AS track, generate_series(45678900, 45678999) AS number
)

-- 找出所有已開立的發票號碼，並將其拆分為 track 和 number
, issued_invoices AS (
    SELECT 
        split_part(invoice_number, '-', 1) AS track,
        CAST(split_part(invoice_number, '-', 2) AS INTEGER) AS number
    FROM invoices
    WHERE invoice_number SIMILAR TO '[A-Z]{2}-[0-9]{8}'
)

-- 找出錯誤的發票號碼
SELECT 
    *
FROM invoices
WHERE invoice_number NOT IN (
    SELECT 
        track || '-' || LPAD(number::TEXT, 8, '0') AS invoice_number
    FROM correct_invoices
)

UNION ALL

SELECT 
    *
FROM invoices
WHERE invoice_number NOT SIMILAR TO '[A-Z]{2}-[0-9]{8}'
ORDER BY invoice_number;
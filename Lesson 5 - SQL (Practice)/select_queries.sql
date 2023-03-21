
-- 1.	Таблиця Employees. Отримати список з інформацією про всіх співробітників
SELECT * FROM employees;

-- 2.	Таблиця Employees. Отримати список всіх співробітників з ім'ям 'David'
SELECT * FROM employees WHERE first_name = 'David'; 

-- 3.	Таблиця Employees. Отримати список всіх співробітників з 20го і з 30го відділу (department_id) 
-- (20 та 30 замінив на 2 та 3, щоб не інсертити багато даних)
SELECT * FROM employees WHERE department_id IN (2, 3);

-- 4.	Таблиця Employees. Отримати список всіх співробітників з 50го і з 80го відділу (department_id) у яких є бонус (значення в колонці commission_pct не порожнє)
-- (50 та 80 замінив на 2 та 3, щоб не інсертити багато даних)
SELECT * FROM employees WHERE department_id IN (2, 3) AND commission_pct != 0;

-- 5.	Таблиця Employees. Отримати список всіх співробітників які прийшли на роботу в перший день місяця (будь-якого)
SELECT * FROM employees WHERE hire_date LIKE '%01'; 

-- 6.	Таблиця Employees. Отримати список всіх співробітників які прийшли на роботу в 2008ом році
-- (2008 замінив на 2022 щоб не інсертити багато даних)
SELECT * FROM employees WHERE hire_date LIKE '2022-%'; 

-- 7.	Таблиця DUAL. Показати завтрашню дату в форматі: Tomorrow is Second day of January
SELECT CONCAT('Tomorrow is ', DATE_FORMAT(DATE_ADD(NOW(), INTERVAL 1 DAY), '%D day of %M')) AS tomorrow_date FROM DUAL;

-- 8.	Таблиця Employees. Отримати список всіх співробітників і дату приходу на роботу кожного в форматі: 21st of June, 2007
SELECT DATE_FORMAT(hire_date, '%D of %M, %Y') AS hire_date_formatted FROM employees; 

-- 9.	Таблиця Employees. Отримати список працівників зі збільшеними зарплатами на 20%. Зарплату показати зі знаком долара
-- (20% замінив на 11% щоб не інсертити багато даних)
SELECT first_name, last_name, CONCAT(salary, '$') as salary, commission_pct FROM employees WHERE commission_pct = 11; 

-- 10.	Таблиця Employees. Отримати список всіх співробітників які прийшли на роботу в лютому 2007го року.
-- (2007 замінив на 2021 щоб не інсертити багато даних)
SELECT * FROM employees WHERE hire_date LIKE '2021-02-%';

-- 11.	Таблиця DUAL. Вивезти актуальну дату, + секунда, + хвилина, + годину, + день, + місяць, + рік
SELECT NOW() AS current_datetime, SECOND(NOW()) AS current_second, MINUTE(NOW()) AS current_minute, HOUR(NOW()) AS current_hour, DAY(NOW()) AS current_day, MONTH(NOW()) AS current_month, YEAR(NOW()) AS current_year FROM DUAL;

-- 12.	Таблиця Employees. Отримати список всіх співробітників з повними зарплатами (salary + commission_pct (%)) в форматі: $ 24,000.00
SELECT first_name, last_name, CONCAT(FORMAT(salary + (salary * commission_pct/100), 2), '$') AS full_salary FROM employees;

-- 13.	Таблиця Employees. Отримати список всіх співробітників і інформацію про наявність бонусів до зарплати (Yes / No)
SELECT first_name, last_name, IF(commission_pct > 0, 'Yes', 'No') AS has_bonus FROM employees;
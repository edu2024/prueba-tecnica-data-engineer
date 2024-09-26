-- Archivo consultas.sql: Consultas SQL para la prueba técnica

-- Consulta 1: Clientes que han gastado más de 110€
SELECT 
    c.first_name AS nombre,
    c.last_name AS apellido,
    SUM(r.rental_amount) AS total_gastado
FROM 
    customers c
JOIN 
    rentals r ON c.customer_id = r.customer_id
GROUP BY 
    c.first_name, c.last_name
HAVING 
    SUM(r.rental_amount) > 110;

-- Consulta 2: Clientes que nunca hicieron una compra
SELECT 
    c.first_name AS nombre,
    c.last_name AS apellido
FROM 
    customers c
LEFT JOIN 
    rentals r ON c.customer_id = r.customer_id
WHERE 
    r.rental_id IS NULL;

-- Consulta 3: Ventas de 2022 por empleado 345, por meses
SELECT 
    EXTRACT(MONTH FROM r.rental_date) AS mes,
    SUM(r.rental_amount) AS total_ventas
FROM 
    rentals r
JOIN 
    staff s ON r.staff_id = s.staff_id
WHERE 
    s.staff_id = 345
    AND EXTRACT(YEAR FROM r.rental_date) = 2022
GROUP BY 
    EXTRACT(MONTH FROM r.rental_date)
ORDER BY 
    mes;

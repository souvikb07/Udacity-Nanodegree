/* Extracting the Data
Write a SQL query below

Use the SQL Workspace below to extract data from the temperatures database, then download the results to a CSV. Then you can open it up in a spreadsheet program in order to analyze it.
The Database Schema

There are three tables in the database:

    city_list - This contains a list of cities and countries in the database. Look through them in order to find the city nearest to you.
    city_data - This contains the average temperatures for each city by year (ºC).
    global_data - This contains the average global temperatures by year (ºC).
*/
/* To check if Delhi is in city_data */
SELECT *
FROM city_data
WHERE city IN ('Delhi');

/* To download th desired data */

SELECT global_data.year, global_data.avg_temp, city_data.city_avg_temp

/* to inner join the data of city and global using year */
FROM global_data INNER JOIN city_data
ON global_data.year=city_data.year
WHERE city like 'Delhi';

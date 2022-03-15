-- This command displays the max temperature of each state ordered by state name ascending
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC;

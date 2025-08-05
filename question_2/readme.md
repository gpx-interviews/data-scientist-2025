# Question 2

For each hour of each day for the BPAT power region in the US, we'd like to calculate the carbon intensity (co2e per kwh).

For context: we use this in our calculations (multiplying by the kwh of a resource) to calculate the co2e.

In answer_q3.py, fuel type data from eia.gov is requested – this is requested from the same portal we looked at in the previous interview.

Please process the data from this API to produce a CSV named hourly_carbon_intensity_july_2025.csv in the current directory with the following columns:

- year (string as 2025)
- month (string as 01, 02, 03, etc)
- day (string as 01, 02, 03, etc)
- hour (string as 01, 02, 03, etc)
- tonnes_co2e_per_kwh (float)

The CSV must be sorted by year, month, day, hour in ascending order.

## Tests

Tests can be ran by running `pytest` in your terminal.

Good luck!

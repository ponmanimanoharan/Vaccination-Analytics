# Vaccination-Analytics
Vaccination Analytics is a personal data project designed to mirror real-world analytics in global health. It uses live public health API data to analyze vaccination trends across countries, processes the data using Python, stores it in a PostgreSQL database, and visualizes the results using Tableau.
# Extract Data from WHO GHO OData API
This Project begins by pulling real-time data from the WHO Global Health Observatory (GHO) OData API. Using Python, the API response is fetched in JSON format and parsed into a clean dataframe using pandas. The dataset includes vaccination relades information by country and year. 

# Key challenges(from WHO)
In 2023, 14.5 million infants did not receive an initial dose of DTP vaccine, pointing to a lack of access to immunization and other health services, and an additional 6.5 million are partially https://ghoapi.azureedge.net/api/Indicatorvaccinated. Of the 21 million, just under 60% of these children live in 10 countries: Afghanistan, Angola, the Democratic Republic of the Congo, Ethiopia, India, Indonesia, Nigeria, Pakistan, Sudan and Yemen.
Monitoring data at subnational levels is critical to helping countries prioritize and tailor vaccination strategies and operational plans to address immunization gaps and reach every person with life-saving vaccines.

# GHO API Base URL
https://ghoapi.azureedge.net/api
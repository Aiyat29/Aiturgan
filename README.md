Technical Specification (TS)
Objective: Develop an API for managing the inventory in a store.

  Functional Requirements:

 1. CRUD for Categories:
Create a category.
Get a list of categories.
Get details of a specific category.

 2. CRUD for Products:
Create a product.
Get a list of products with filtering options based on price and availability.
Get details of a specific product.
Update product information.
Delete a product.
 3. Product Filtering:
By price (minimum and maximum).
By availability (in stock).


Technologies:

FastAPI for building the API.
SQLAlchemy for interacting with the database.
SQLite as the database.


API Access:

The API will be available via HTTP REST API endpoints.

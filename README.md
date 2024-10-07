# Precipitation Analysis

This project is about analyzing precipitation data from the last 12 months using a SQLite database and visualizing the results with Pandas and Matplotlib. Then using what we calculated and having that displayed on a Flask environment with API calls to each route.

## Table of Contents

1. [Project Structure](#projectstructure)
2. [Prerequisites](#prerequisites)
3. [Data Preparation](#data-preparation)
4. [Main Script](#main-script)
5. [Flask API](#flask-api)
6. [Example Code](#example-code)
    - [Generating a Precipitation Graph](#generating-a-precipitation-graph)
    - [Example Flask API Route](#example-flask-api-route)
7. [Usage](#usage)

## Project Structure

- **hawaii.sqlite**: SQLite database file containing the weather data.
- **main_script.py**: Main Python script for querying the database and plotting the results.
- **app.py**: Flask application using API calls to route the user.
- **README.md**: This file, providing an overview and instructions for the project.

## Prerequisites

Ensure you have the following Python packages installed:

- `numpy`
- `pandas`
- `matplotlib`
- `sqlalchemy`
- `flask`

You can install these packages using pip:

```sh
pip install numpy pandas matplotlib sqlalchemy flask
```

## Data Preparation

The project uses a SQLite database named hawaii.sqlite which contains two tables:

    Measurement: This table contains daily weather measurements.
    Station: This table contains information about the weather stations.

## Data Preparation

The project uses a SQLite database named `hawaii.sqlite` which contains two tables:

- **Measurement**: This table contains daily weather measurements.
- **Station**: This table contains information about the weather stations.

## Main Script

The main script performs the following steps:

1. **Set Up the Database Connection**:
    - Connect to the SQLite database.
    - Reflect the database tables.

2. **Find the Most Recent Date**:
    - Query the database to find the most recent date in the `Measurement` table.

3. **Calculate the Date One Year Ago**:
    - Calculate the date one year prior to the most recent date.

4. **Retrieve Precipitation Data**:
    - Query the database to retrieve the precipitation data for the last 12 months.

5. **Prepare the Data**:
    - Save the query results as a Pandas DataFrame.
    - Convert the `date` column to datetime format.
    - Sort the DataFrame by date.

6. **Plot the Data**:
    - Use Pandas plotting with Matplotlib to create a plot of the precipitation data.

## Flask API

The Flask API provides the following endpoints:

- **/**: Welcome message with a list of available routes.
- **/api/v1.0/precipitation**: Returns precipitation data for the last 12 months.
- **/api/v1.0/stations**: Returns a list of weather stations.
- **/api/v1.0/tobs**: Returns temperature observations for the last 12 months for a specific station.
- **/api/v1.0/<start>**: Returns min, avg, and max temperatures for all dates greater than or equal to the start date.
- **/api/v1.0/<start>/<end>**: Returns min, avg, and max temperatures for dates between the start and end dates inclusive.

## Example Code

### Generating a Precipitation Graph

Here is a simple example snippet of how to generate a precipitation graph using the data from the SQLite database:

```python
# Set up the database connection
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Plot the data
precipitation_df.set_index('date')['precipitation'].plot(figsize=(10, 5), title="Precipitation Over the Last 12 Months", legend=True)
plt.xlabel('Date')
plt.ylabel('Inches')
plt.show()
```
![precipitation](https://github.com/omidk414/sqlalchemy-challenge/blob/main/images/precipitation.png)


### Example Flask API Route

Here is an example of how to use one of the API routes from app.py to get precipitation data for the last 12 months:

python
```
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    one_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    precipitation_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year).all()
    session.close()
    precip = list(np.ravel(precipitation_data))
    return jsonify(precip)
```
When accessing the URL http://127.0.0.1:5000/api/v1.0/precipitation, the following should happen:

   1.  HTTP Request Sent: A GET request is sent to the Flask server running locally on your machine.
   2. Route Handler Invoked: The Flask route handler for /api/v1.0/precipitation is invoked.
   3. Database Query Executed: Inside the route handler, a query is executed on the Measurement table to retrieve precipitation data for the last 12 months.
   4. Data Processing: The query results are processed and converted into a JSON-compatible format.
   5. HTTP Response Returned: The processed data is returned as a JSON response.

![precipitationapi](https://github.com/omidk414/sqlalchemy-challenge/blob/main/images/precipitationapi.png)

## Usage

To run the main script and the Flask application, execute the following commands:

sh
```
python main_script.py
python app.py
```
The main script will output a plot showing the precipitation over the last 12 months. The Flask application will provide API endpoints to access the data.



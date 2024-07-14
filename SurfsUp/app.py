# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Here Is A List Of The Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    one_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    precipitation_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year).all()
    session.close()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()
    station_results = list(np.ravel(results))
    return jsonify(station_results)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    one_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    temperature_data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= one_year).all()
    session.close()
    temps = list(np.ravel(temperature_data))
    return jsonify(temps)

@app.route("/api/v1.0/<start>")

@app.route("/api/v1.0/<start>/<end>")
def stats(start = None, end = None):
    session = Session(engine)
    results = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).filter(Measurement.date <= start).all()
        session.close()
        temps = list(np.ravel(results))
        return jsonify(temps)


if __name__ == '__main__':
    app.run(debug=True)
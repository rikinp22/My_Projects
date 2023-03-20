# import dependencies
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Create an app, being sure to pass __name__
app = Flask(__name__)

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
session = Session(engine)

base = automap_base()
base.prepare(autoload_with=engine)

measurement = base.classes.measurement
station = base.classes.station

# Start at the homepage. 
# List all the available routes.
@app.route("/")
def home():
    # Create a dictionary of available routes
    routes = {
        "Available Routes": [
            "/api/v1.0/precipitation",
            "/api/v1.0/stations",
            "/api/v1.0/tobs",
            "/api/v1.0/start_date",
            "/api/v1.0/start_end"
        ]
    }
    session.close()
      # Return the dictionary as JSON
    return jsonify(routes)

# if __name__ == '__main__':
#     app.run(debug=True)
    
# Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
    sel = [measurement.date,measurement.prcp]
    precipitation_query = session.query(*sel).all()
    
    session.close()

    precipitation = []
    for date, prcp in precipitation_query:
        precipitation_dict = {}
        precipitation_dict["Date"] = date
        precipitation_dict["Precipitation"] = prcp
        precipitation.append(precipitation_dict)

    return jsonify(precipitation)

# if __name__ == "__main__":
#     app.run(debug=True)

# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(station.station, station.name).all()
    station_list = list(np.ravel(results))

    session.close()
    
    return jsonify(station_list)

# if __name__ == '__main__':
#     app.run(debug=True)

# Query the dates and temperature observations of the most-active station for the previous year of data.
# Return a JSON list of temperature observations for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    tobsall = []
    query_observation = session.query(measurement.date).order_by(measurement.date.desc()).first()[0]
    latestdate = dt.datetime.strptime(query_observation, '%Y-%m-%d')
    querydate = dt.date(latestdate.year -1, latestdate.month, latestdate.day)
    sel = [measurement.date,measurement.tobs]
    queryresult = session.query(*sel).filter(measurement.date >= querydate).all()
    
    session.close()
    
    for date, tobs in queryresult:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Tobs"] = tobs
        tobsall.append(tobs_dict)

    return jsonify(tobsall)

# if __name__ == '__main__':
#     app.run(debug=True)
    
# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
# For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
# For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
@app.route("/api/v1.0/<start>")
def start_date(start):
    query_temperatures = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start).all()
    
    session.close()

    temperatures = []
    for min,avg,max in query_temperatures:
        temperatures_dict = {}
        temperatures_dict["min"] = min
        temperatures_dict["average"] = avg
        temperatures_dict["max"] = max
        temperatures.append(temperatures_dict)

    return jsonify(temperatures)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
                filter(measurement.date >= start).\
                filter(measurement.date <= end).all()
    
    session.close()
  
    start_end_TOBS = []
    for min, avg, max in results:
        dict = {}
        dict["min_temp"] = min
        dict["avg_temp"] = avg
        dict["max_temp"] = max
        start_end_TOBS.append(dict) 
    

    return jsonify(start_end_TOBS)

if __name__ == '__main__':
    app.run(debug=True)
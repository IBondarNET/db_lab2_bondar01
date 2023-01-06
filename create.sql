CREATE TABLE circuits (
    circuitId INTEGER PRIMARY KEY,
    circuitRef VARCHAR,
    name VARCHAR,
    location VARCHAR,
    country VARCHAR,
    lat DECIMAL (8, 6),
    lng DECIMAL (9, 6),
    alt INTEGER,
    url VARCHAR);

CREATE TABLE drivers (
    driverId INTEGER PRIMARY KEY,
    driverRef VARCHAR, 
    number VARCHAR, 
    code VARCHAR, 
    forename VARCHAR, 
    surname VARCHAR, 
    dob VARCHAR, 
    nationality VARCHAR, 
    url VARCHAR);

CREATE TABLE races (
    raceId INTEGER PRIMARY KEY,
    year INTEGER,
    round INTEGER, 
    circuitId INTEGER REFERENCES circuits (circuitId),
    name VARCHAR,
    date DATE, 
    time TIME, 
    url VARCHAR);

CREATE TABLE results (
    raceId INTEGER REFERENCES races (raceId),
    driverId INTEGER REFERENCES drivers (driverId), 
    number INTEGER, 
    grid INTEGER, 
    position INTEGER, 
    positionText VARCHAR, 
    positionOrder INTEGER, 
    points INTEGER, 
    laps INTEGER, 
    time VARCHAR, 
    milliseconds INTEGER, 
    fastestLap VARCHAR, 
    rank INTEGER, 
    fastestLapTime VARCHAR, 
    fastestLapSpeed DECIMAL, 
    statusId INTEGER);
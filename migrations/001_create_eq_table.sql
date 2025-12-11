

CREATE TABLE IF NOT EXISTS earthquakes (
    id VARCHAR(50) PRIMARY KEY,
    time DATETIME NULL,
    updated DATETIME NULL,
    latitude DOUBLE,
    longitude DOUBLE,
    depth_km DOUBLE,
    mag DOUBLE,
    magType VARCHAR(20),
    place VARCHAR(255),
    status VARCHAR(50),
    tsunami INT,
    sig INT,
    net VARCHAR(20),
    nst INT,
    dmin DOUBLE,
    rms DOUBLE,
    gap DOUBLE,
    magError DOUBLE,
    depthError DOUBLE,
    magNst INT,
    locationSource VARCHAR(20),
    magSource VARCHAR(20),
    types TEXT,
    ids TEXT,
    sources TEXT,
    type VARCHAR(50),
    country VARCHAR(100),
    year INT,
    month VARCHAR(30),
    day INT,
    day_of_week VARCHAR(20),
    depth_type VARCHAR(30),
    mag_category VARCHAR(30)


);




autossh -M 40000 -XY -f -N -T -R 14000:localhost:22 -R 14001:localhost:5900 thomasm@lheppc46.unibe.ch
autossh -M 42000 -f -N -T -R 14300:localhost:3000 -f -N -T -R 14888:localhost:8765 -f -N -T -R 14881:localhost:8081 thomasm@lheppc46.unibe.ch

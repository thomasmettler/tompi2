from influxdb import InfluxDBClient

#client = InfluxDBClient(host='localhost', port=8086)

#print client.get_list_database()
#getTempInflux()

#select last(value) from Temperature
#{u'series': [{u'values': [[u'2019-06-27T16:19:44.548528195Z', 29.6]], u'name': u'Temperature', u'columns': [u'time', u'last']}], u'statement_id': 0}


def getTempInflux():
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database('mydb')
    temp_results = client.query('SELECT last("value") FROM "Temperature"')
    temp_points = temp_results.get_points()
    for temp_point in temp_points:
	print temp_point['last']
    humi_results = client.query('SELECT last("value") FROM "Humidity"')
    humi_points = humi_results.get_points()
    for humi_point in humi_points:
        print humi_point['last']

    temp_results = client.query('SELECT last("value") FROM "Temperature"')
    temp_points = temp_results.get_points()
    for temp_point in temp_points:
        print temp_point['last']
    humi_results = client.query('SELECT last("value") FROM "Humidity"')
    humi_points = humi_results.get_points()
    for humi_point in humi_points:
        print humi_point['last']
    temp_results = client.query('SELECT last("value") FROM "Temperature"')
    temp_points = temp_results.get_points()
    for temp_point in temp_points:
        print temp_point['last']
    humi_results = client.query('SELECT last("value") FROM "Humidity"')
    humi_points = humi_results.get_points()
    for humi_point in humi_points:
        print humi_point['last']
    temp_results = client.query('SELECT last("value") FROM "Temperature"')
    temp_points = temp_results.get_points()
    for temp_point in temp_points:
        print temp_point['last']
    humi_results = client.query('SELECT last("value") FROM "Humidity"')
    humi_points = humi_results.get_points()
    for humi_point in humi_points:
        print humi_point['last']

    print "test: " + next(humi_points)['last']
    return

getTempInflux()




while true
do
	ssh -XY -f -N -T -R 11000:localhost:22 -R 11001:localhost:5900 thomasm@lheppc46.unibe.ch
	sleep 15m
done

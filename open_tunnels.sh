
#open tunnel for grafana
ssh -f -N -T -R 11300:localhost:3000 thomasm@lheppc46.unibe.ch
#open tunnel for motioneye
#ssh -f -N -T -R 12888:localhost:8765 thomasm@lheppc46.unibe.ch
#open tunnel for webcam stream
#ssh -f -N -T -R 12882:localhost:8082 thomasm@lheppc46.unibe.ch
#open tunnel for webcam2
#ssh -f -N -T -R 12881:localhost:8081 thomasm@lheppc46.unibe.ch

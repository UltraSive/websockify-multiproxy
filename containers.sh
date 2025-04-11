sudo docker run --rm --name novnc --add-host=host.docker.internal:host-gateway -p 8034:6080 -e AUTOCONNECT=true -e VNC_PASSWORD=dQio5HUE -e VNC_SERVER=host.docker.internal:5934 bonigarcia/novnc:1.2.0

sudo docker run -it --rm --add-host=host.docker.internal:host-gateway -p 7033:80 --name websockify efrecon/websockify 80 host.docker.internal:5933
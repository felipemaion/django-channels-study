from channels.routing import route
from example.consumers import ws_connect, ws_disconnect

ASGI_APPLICATION = "example_channels.routing.application"

channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
]
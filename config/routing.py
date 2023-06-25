from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import auction.routing
from channels.security.websocket import OriginValidator

application = ProtocolTypeRouter({
    'websocket': OriginValidator(
        URLRouter(
            auction.routing.websocket_urlpatterns
        ),
        ['*']
    ),
})

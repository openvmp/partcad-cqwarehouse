if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    HexHeadScrew,
)

size = "M3-0.5"
simple = False
length = 10
socket_clearance = 6

screw = HexHeadScrew(
    size=size,
    fastener_type="din931",
    length=length,
    simple=simple,
    socket_clearance=socket_clearance,
)

show_object(screw)

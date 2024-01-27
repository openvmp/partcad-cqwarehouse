if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    HexHeadScrew,
)

size = "M1.6-0.35"
simple = False
length = 10
socket_clearance = 6.0
hand = "right"

screw = HexHeadScrew(
    size=size,
    fastener_type="iso4017",
    length=length,
    simple=simple,
    socket_clearance=socket_clearance,
    hand=hand,
)

show_object(screw)

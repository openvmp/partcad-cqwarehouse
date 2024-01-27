if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    HexHeadWithFlangeScrew,
)

size = "M5-0.8"
simple = False
length = 10
socket_clearance = 6

screw = HexHeadWithFlangeScrew(
    size=size,
    fastener_type="din1665",
    length=length,
    simple=simple,
    socket_clearance=socket_clearance,
)

show_object(screw)

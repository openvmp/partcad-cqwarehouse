if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    HexHeadScrew,
)

if not "size" in locals():
    size = "M1.6-0.35"
if not "simple" in locals():
    simple = False
if not "length" in locals():
    length = 10
if not "socket_clearance" in locals():
    socket_clearance = 6

screw = HexHeadScrew(
    size=size,
    fastener_type="iso4014",
    length=length,
    simple=simple,
    socket_clearance=socket_clearance,
)

show_object(screw)

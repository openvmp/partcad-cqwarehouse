if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    HexHeadWithFlangeScrew,
)

if not "size" in locals():
    size = "M5-0.8"
if not "simple" in locals():
    simple = False
if not "length" in locals():
    length = 10
if not "socket_clearance" in locals():
    socket_clearance = 6

screw = HexHeadWithFlangeScrew(
    size=size,
    fastener_type="din1662",
    length=length,
    simple=simple,
    socket_clearance=socket_clearance,
)

show_object(screw)

if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    SocketHeadCapScrew,
)

if not "size" in locals():
    size = "#0-80"
if not "simple" in locals():
    simple = False
if not "length" in locals():
    length = 10

screw = SocketHeadCapScrew(
    size=size,
    fastener_type="asme_b18.3",
    length=length,
    simple=simple,
)

show_object(screw)

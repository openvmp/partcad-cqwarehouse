if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    SocketHeadCapScrew,
)

size = "#0-80"
simple = False
length = 10
hand = "right"

screw = SocketHeadCapScrew(
    size=size,
    fastener_type="asme_b18.3",
    length=length,
    simple=simple,
    hand=hand,
)

show_object(screw)

if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    PanHeadScrew,
)

size = "M1.6-0.35"
simple = False
length = 10

screw = PanHeadScrew(
    size=size,
    fastener_type="iso1580",
    length=length,
    simple=simple,
)

show_object(screw)

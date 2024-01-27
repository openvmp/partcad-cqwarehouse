if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    PanHeadScrew,
)

size = "M2-0.4"
simple = False
length = 10

screw = PanHeadScrew(
    size=size,
    fastener_type="iso14583",
    length=length,
    simple=simple,
)

show_object(screw)

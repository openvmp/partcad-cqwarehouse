if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    PanHeadScrew,
)

size = "#3-48"
simple = False
length = 10

screw = PanHeadScrew(
    size=size,
    fastener_type="asme_b_18.6.3",
    length=length,
    simple=simple,
)

show_object(screw)

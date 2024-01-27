if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    CheeseHeadScrew,
)

size = "M2-0.4"
simple = False
length = 10

screw = CheeseHeadScrew(
    size=size,
    fastener_type="iso14580",
    length=length,
    simple=simple,
)

show_object(screw)

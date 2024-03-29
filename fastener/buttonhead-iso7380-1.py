if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    ButtonHeadScrew,
)

size = "M6-1"
simple = False
length = 10
hand = "right"

screw = ButtonHeadScrew(
    size=size,
    fastener_type="iso7380_1",
    length=length,
    simple=simple,
    hand=hand,
)

show_object(screw)

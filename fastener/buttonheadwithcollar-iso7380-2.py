if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    ButtonHeadWithCollarScrew,
)

size = "M6-1"
simple = False
length = 10
hand = "right"

screw = ButtonHeadWithCollarScrew(
    size=size,
    fastener_type="iso7380_2",
    length=length,
    simple=simple,
    hand=hand,
)

show_object(screw)

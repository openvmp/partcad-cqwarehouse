if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    RaisedCounterSunkOvalHeadScrew,
)

size = "M1.6-0.35"
simple = False
length = 10
hand = "right"

screw = RaisedCounterSunkOvalHeadScrew(
    size=size,
    fastener_type="iso7047",
    length=length,
    simple=simple,
    hand=hand,
)

show_object(screw)

if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    RaisedCounterSunkOvalHeadScrew,
)

size = "M2-0.4"
simple = False
length = 10

screw = RaisedCounterSunkOvalHeadScrew(
    size=size,
    fastener_type="iso14584",
    length=length,
    simple=simple,
)

show_object(screw)

if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    RaisedCounterSunkOvalHeadScrew,
)

size = "M1-0.25"
simple = False
length = 10

screw = RaisedCounterSunkOvalHeadScrew(
    size=size,
    fastener_type="iso2010",
    length=length,
    simple=simple,
)

show_object(screw)

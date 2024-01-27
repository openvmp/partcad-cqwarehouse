if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    CounterSunkScrew,
)

size = "M2-0.4"
simple = False
length = 10

screw = CounterSunkScrew(
    size=size,
    fastener_type="iso14581",
    length=length,
    simple=simple,
)

show_object(screw)

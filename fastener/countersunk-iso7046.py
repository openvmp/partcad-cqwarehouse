if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    CounterSunkScrew,
)

size = "M1.6-0.35"
simple = False
length = 10

screw = CounterSunkScrew(
    size=size,
    fastener_type="iso7046",
    length=length,
    simple=simple,
)

show_object(screw)

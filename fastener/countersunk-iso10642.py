if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    CounterSunkScrew,
)

size = "M3-0.5"
simple = False
length = 10
hand = "right"

screw = CounterSunkScrew(
    size=size,
    fastener_type="iso10642",
    length=length,
    simple=simple,
    hand=hand,
)

show_object(screw)

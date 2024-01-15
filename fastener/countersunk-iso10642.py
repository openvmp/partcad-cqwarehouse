if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    CounterSunkScrew,
)

if not "size" in locals():
    size = "M3-0.5"
if not "simple" in locals():
    simple = False
if not "length" in locals():
    length = 10

screw = CounterSunkScrew(
    size=size,
    fastener_type="iso10642",
    length=length,
    simple=simple,
)

show_object(screw)

if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    CheeseHeadScrew,
)

if not "size" in locals():
    size = "M2.5-0.45"
if not "simple" in locals():
    simple = False
if not "length" in locals():
    length = 10

screw = CheeseHeadScrew(
    size=size,
    fastener_type="iso7048",
    length=length,
    simple=simple,
)

show_object(screw)

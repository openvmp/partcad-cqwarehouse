if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    PanHeadScrew,
)

if not "size" in locals():
    size = "#3-48"
if not "simple" in locals():
    simple = False
if not "length" in locals():
    length = 10

screw = PanHeadScrew(
    size=size,
    fastener_type="asme_b_18.6.3",
    length=length,
    simple=simple,
)

show_object(screw)

if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    ButtonHeadScrew,
)

if not "size" in locals():
    size = "M6-1"
if not "simple" in locals():
    simple = False
if not "length" in locals():
    length = 10

screw = ButtonHeadScrew(
    size=size,
    fastener_type="iso7380_1",
    length=length,
    simple=simple,
)

show_object(screw)
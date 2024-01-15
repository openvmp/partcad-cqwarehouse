if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    SetScrew,
)

if not "size" in locals():
    size = "M1.4-0.3"
if not "simple" in locals():
    simple = False
if not "length" in locals():
    length = 10

screw = SetScrew(
    size=size,
    fastener_type="iso4026",
    length=length,
    simple=simple,
)

show_object(screw)

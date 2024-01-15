if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    PanHeadWithCollarScrew,
)

if not "size" in locals():
    size = "M3-0.5"
if not "simple" in locals():
    simple = False
if not "length" in locals():
    length = 10

screw = PanHeadWithCollarScrew(
    size=size,
    fastener_type="din967",
    length=length,
    simple=simple,
)

show_object(screw)

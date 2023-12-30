# if __name__ != "__cqgi__":
#     from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    ButtonHeadScrew,
)

if not "size" in locals():
    size = "M6-1"
if not "simple" in locals():
    simple = False

screw = ButtonHeadScrew(
    size=size,
    fastener_type="iso7380_1",
    length=10,
    simple=simple,
)

show_object(screw)

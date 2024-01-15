if __name__ != "__cqgi__":
    from cq_server.ui import ui, show_object

from cq_warehouse.fastener import (
    RaisedCheeseHeadScrew,
)

if not "size" in locals():
    size = "M1.6-0.35"
if not "simple" in locals():
    simple = False
if not "length" in locals():
    length = 10

screw = RaisedCheeseHeadScrew(
    size=size,
    fastener_type="iso7045",
    length=length,
    simple=simple,
)

show_object(screw)

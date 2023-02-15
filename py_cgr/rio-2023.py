import sys
from py_cgr_lib.py_cgr_lib import cgr_yen
from py_cgr_lib.py_cgr_lib import cp_load

source = 1      # source node A
destination = 5 # destination node E
curr_time = 0   # Current time

contact_plan = cp_load('./contact_plans/cgr_tutorial.txt', 5000)
print(contact_plan)

print("---yen---")
for contact in contact_plan:
    contact.clear_dijkstra_working_area()
    contact.clear_management_working_area()
routes = cgr_yen(source, destination, curr_time, contact_plan, 10)
for route in routes:
    print(route)
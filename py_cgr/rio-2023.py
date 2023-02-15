import sys
from py_cgr_lib.py_cgr_lib import cgr_yen
from py_cgr_lib.py_cgr_lib import cp_load
from py_cgr_lib.py_cgr_lib import fwd_candidate
from py_cgr_lib.py_cgr_lib import Bundle

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

print("---forward---")
excluded_nodes = []
bundle = Bundle(src=1, dst=5, size=1, deadline=60, priority=0)
candidate_routes = fwd_candidate(curr_time, source, contact_plan, bundle, routes, excluded_nodes)
print(candidate_routes[0])
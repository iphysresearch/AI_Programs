#!/usr/bin/env python
import sys
import string

last_product_id = None
cur_location = ""
count_locations=0

for line in sys.stdin:
    line = line.strip()
    product_id,location = line.split("\t")
    # if this is the first iteration
    if not last_product_id:
        last_product_id = product_id
        cur_location = location
        count_locations = 1

    if product_id == last_product_id:
        if location != cur_location:
            count_locations = count_locations + 1
            cur_location = location

    # else we're transitioning from the last product to a new one
    else:
        print '%s\t%s' % (last_product_id,count_locations)
        last_product_id = product_id
        cur_location = location
        count_locations = 1

# finally print out the last product / location combo. This is a gotcha! Easy to forget this line :-)
print '%s\t%s' % (product_id,count_locations)
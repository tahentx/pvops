import datetime

def raw_availability(downtime,totaltime):

"""the fraction of a given operating period in
which a component within a PV system is performing within the design specification,16,17 with no
exclusions"""

    raw = 1 - (downtime/totaltime)
    return raw

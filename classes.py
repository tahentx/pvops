class WorkOrder:
    def __init__(self, asset, type, status, description):
        self.asset = asset
        self.type = type
        self.status = status
        self.description = description

    def create_wo(abc):
        print("This work order is for " + abc.asset)

wo_384 = WorkOrder("INV3B", "Corrective", "Ready to Schedule", "Blown Fuse")
wo_384.create_wo()

class PMSchedule:
    def __init__(self, asset, interval):
        self.asset = asset
        self.interval = interval

pm_223 = PMSchedule("INV3B","Quarterly")
print(type(pm_223))

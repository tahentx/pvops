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

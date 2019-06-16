class PM:
  def __init__(self, asset, interval,entitlement):
    self.asset = asset
    self.interval = interval
    self.entitlement = entitlement

tidewater_solar = PM("inverter",3,"Availability Guarantee")
print(tidewater_solar.entitlement)

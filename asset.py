class Asset:
  def __init__(self, type, nameplate, project):
    self.type = type
    self.nameplate = nameplate
    self.project = project

B02 = Asset("Tracker","none", "Saltwood Solar")
print(B02.project)

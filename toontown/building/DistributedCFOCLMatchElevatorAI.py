from .ElevatorConstants import *
from . import DistributedBossElevatorAI

class DistributedCFOCLMatchElevatorAI(DistributedBossElevatorAI.DistributedBossElevatorAI):

    def __init__(self, air, bldg, zone, antiShuffle = 0, minLaff = 0):
        DistributedBossElevatorAI.DistributedBossElevatorAI.__init__(self, air, bldg, zone, antiShuffle=antiShuffle, minLaff=minLaff)
        self.type = ELEVATOR_CFO_CL
        self.countdownTime = ElevatorData[self.type]['countdown']

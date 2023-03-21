
from UIKit import UIDevice
device = UIDevice.currentDevice
device.setBatteryMonitoringEnabled(True)
print(f"Battery Level = {int(device.batteryLevel * 100)}%\n")
device.setBatteryMonitoringEnabled(False)
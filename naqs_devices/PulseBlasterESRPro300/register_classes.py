#####################################################################
#                                                                   #
# /naqs_devices/PulseBlasterESRPro300/register_classes.py           #
#                                                                   #
#                                                                   #
#####################################################################
import labscript_devices

labscript_devices.register_classes(
    'PulseBlasterESRPro300',
    BLACS_tab='naqs_devices.PulseBlasterESRPro300.blacs_tabs.PulseBlasterESRPro300Tab',
    runviewer_parser='naqs_devices.PulseBlasterESRPro300.runviewer_parsers.PulseBlasterESRProParser',
)

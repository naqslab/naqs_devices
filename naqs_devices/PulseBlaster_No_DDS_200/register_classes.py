#####################################################################
#                                                                   #
# /naqs_devices/PulseBlaster_No_DDS_200/register_classes.py         #
#                                                                   #
#                                                                   #
#####################################################################
import labscript_devices

labscript_devices.register_classes(
    'PulseBlaster_No_DDS_200',
    BLACS_tab='naqs_devices.PulseBlaster_No_DDS_200.blacs_tabs.PulseBlaster_No_DDS_200_Tab',
    runviewer_parser='naqs_devices.PulseBlaster_No_DDS_200.runviewer_parsers.PulseBlaster_No_DDS_200_Parser',
)

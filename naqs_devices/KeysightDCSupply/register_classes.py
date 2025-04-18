#####################################################################
#                                                                   #
# /naqs_devices/KeysightDCSupply/register_classes.py                #
#                                                                   #
# Copyright 2020, David Meyer                                       #
#                                                                   #
# This file is part of naqs_devices,                                #
# and is licensed under the                                         #
# Simplified BSD License. See the license.txt file in the root of   #
# the project for the full license.                                 #
#                                                                   #
#####################################################################
import labscript_devices

labscript_devices.register_classes(
    'KeysightDCSupply',
    BLACS_tab='naqs_devices.KeysightDCSupply.blacs_tab.KeysightDCSupplyTab',
    runviewer_parser='')
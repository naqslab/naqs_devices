#####################################################################
#                                                                   #
# /naqs_devices/TektronixTDS/register_classes.py                    #
#                                                                   #
# Copyright 2018, David Meyer                                       #
#                                                                   #
# This file is part of naqs_devices,                                #
# and is licensed under the                                         #
# Simplified BSD License. See the license.txt file in the root of   #
# the project for the full license.                                 #
#                                                                   #
#####################################################################
import labscript_devices

labscript_devices.register_classes(
    'TDS_Scope',
    BLACS_tab='naqs_devices.TektronixTDS.blacs_tabs.TDS_ScopeTab',
    runviewer_parser='')

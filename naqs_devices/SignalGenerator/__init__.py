#####################################################################
#                                                                   #
# /naqs_devices/SignalGenerator/__init__.py                         #
#                                                                   #
# Copyright 2018, David Meyer                                       #
#                                                                   #
# This file is part of naqs_devices,                                #
# and is licensed under the                                         #
# Simplified BSD License. See the license.txt file in the root of   #
# the project for the full license.                                 #
#                                                                   #
#####################################################################
from labscript_devices import deprecated_import_alias

# For backwards compatibility with old experiment scripts:
RS_SMF100A = deprecated_import_alias("naqs_devices.SignalGenerator.Models.RS_SMF100A")

RS_SMHU = deprecated_import_alias("naqs_devices.SignalGenerator.Models.RS_SMHU")

HP8643A = deprecated_import_alias("naqs_devices.SignalGenerator.Models.HP8643A")

HP8642A = deprecated_import_alias("naqs_devices.SignalGenerator.Models.HP8642A")

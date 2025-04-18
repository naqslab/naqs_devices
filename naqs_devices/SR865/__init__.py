#####################################################################
#                                                                   #
# /naqs_devices/SR865/__init__.py                                   #
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
SR865 = deprecated_import_alias("naqs_devices.SR865.labscript_device.SR865")

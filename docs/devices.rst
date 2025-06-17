Devices
=======

Directory of all device classes that can be installed within this namespace.

.. The labscript primitive subclasses are derivatives of the labscript-provided 
.. children classes used by devices in this repository. 

.. There are two parent classes that are not directly used, but rather provide 
.. templates for creating new devices. First is the :doc:`VISA` class that 
.. templates communication with devices through the VISA communication protocol.

.. This uses the :std:doc:`PyVISA python wrapper <pyvisa:index>`. The second is 
.. the :doc:`SignalGenerator` class that uses the :doc:`VISA` class to template 
.. CW frequency generators.

.. There are two thin subclasses of the labscript_devices.PulseBlaster_No_DDS 
.. class: :doc:`PulseBlasterESRPro300` and :doc:`PulseBlaster_No_DDS_200`. They 
.. exist simply to enforce the correct core clock frequency and clock limits 
.. without any other change in functionality from the parent.

.. Other device classes control particular series of devices and implement 
.. functional control of their hardware to varying degrees. In general, the 
.. design philosophy is that if the device class does not set an option, it will 
.. not be interfered with when using the device class to control the instrument. 
.. This means that custom settings and configurations of each device can be used 
.. by setting them manually at the device front panel without the device class 
.. interfering.


Templates
---------

These components are not meant to be used directly,
but provide templates for creating new devices.
Some are designed to be inherited to provide basic functionality.

* `TemplateDevice <https://naqs-devices.readthedocs.io/projects/template_device/en/latest/>`_
* `VISA <https://naqs-devices.readthedocs.io/projects/VISA/en/latest/>`_

Frequency Synthesis
-------------------

* `NovaTechDDS <https://naqs-devices.readthedocs.io/projects/NovaTechDDS/en/latest/>`_
* `SignalGenerator <https://naqs-devices.readthedocs.io/projects/SignalGenerator/en/latest/>`_

Oscilloscopes
-------------

* `KeysightXSeries <https://naqs-devices.readthedocs.io/projects/KeysightXSeries/en/latest/>`_
* `TektronixTDS <https://naqs-devices.readthedocs.io/projects/TektronixTDS/en/latest/>`_

Thin Subclasses
---------------

These are thin subclasses of standard labscript devices
that enforce specific device limitations for particular submodels.

* `PulseBlaster_No_DDS_200 <https://naqs-devices.readthedocs.io/projects/PulseBlaster_No_DDS_200/en/latest/>`_
* `PulseBlasterESRPro300 <https://naqs-devices.readthedocs.io/projects/PulseBlasterESRPro300/en/latest/>`_

DC Power Supplies
-----------------

* `KeysightDCSupply <https://naqs-devices.readthedocs.io/projects/KeysightDCSupply/en/latest/>`_

Lock-in Amplifiers
------------------

* `SR865 <https://naqs-devices.readthedocs.io/projects/SR865/en/latest/>`_



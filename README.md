# naqs_devices (previously naqslab_devices) #

This repository contains various 3rd-party device implementations for use with
the python-based [labscript suite](https://labscriptsuite.org/en/latest/)
experiment control system.

Devices include:

* Novatech 409B, 409B-AC, & 440A DDS
* Stanford Research 865 Lockin Amplifier
* Tektronix TDS series oscilloscopes
* Keysight MSO/DSO X series oscilloscopes
* Various CW RF Signal Generators
  * Rohde & Schwarz SMF 100A
  * Rohde & Schwarz SMA 100B
  * Rohde & Schwarz SMHU
  * HP 8642A
  * HP 8643A
  * HP 8648A/B/C/D
  * Keysight E8257N
  * Keysight/Agilent DC Power Supplies
    * E364x series tested

The above code is designed to be modular allowing for easy addition of other
models, particularly oscilloscopes and CW Signal Generators.

## How do I get set up? ##

Clone this repository into your workspace. It does not necessarily need to be in the labscript suite directory.

### Valid since labscript\_devices version 2.6.0 ###

Add the following line to the labconfig.ini file under the `[DEFAULT]` section.

```text
user_devices = naqs_devices
```

Note that previously it was required to place this repository in the `userlib` directory in your labscript install, but now this repository can be anywhere.

### Installation ###

After adding the above, navigate to where you have placed this directory and:

* Ensure you are in your labscript environment

```bash
conda activate labscript
```

* Install `naqs_devices` as a namespace package:

```bash
pip install -e .
```

#### Usage ####

Invoke in labscript scripts like other labscript\_devices

```python
from naqs_devices import ScopeChannel
from naqs_devices.KeysightXSeries.labscript_device import KeysightXScope
```

Usage of individual devices varies somewhat.
Here is an example connectiontable showing some of their instantiation with
labscript_devices > 2.2.0.

```python
from labscript import *
from naqs_devices.PulseBlasterESRPro300.labscript_device import PulseBlasterESRPro300
from naqs_devices.NovaTechDDS.labscript_device import NovaTech409B, NovaTech409B_AC, NovaTech440A
from labscript_devices.NI_DAQmx import NI_DAQmx
from naqs_devices.SignalGenerator.Models import RS_SMF100A, RS_SMHU
from naqs_devices.SR865.labscript_device import SR865
from naqs_devices import ScopeChannel, StaticFreqAmp
from naqs_devices.KeysightXSeries.labscript_device import KeysightXScope

PulseBlasterESRPro300(name='pulseblaster_0', board_number=0, programming_scheme='pb_start/BRANCH')
ClockLine(name='pulseblaster_0_clockline_fast', pseudoclock=pulseblaster_0.pseudoclock, connection='flag 0')
ClockLine(name='pulseblaster_0_clockline_slow', pseudoclock=pulseblaster_0.pseudoclock, connection='flag 1')

NI_DAQmx(name='ni_6343', parent_device=pulseblaster_0_clockline_fast, clock_terminal='/ni_usb_6343/PFI0',
        MAX_name='ni_usb_6343',
        num_AO = 4,
        sample_rate_AO = 700e3,
        num_DO = 32,
        sample_rate_DO = 1e6,
        num_AI = 32,
        clock_terminal_AI = '/ni_usb_6343/PFI0',
        mode_AI = 'labscript',
        sample_rate_AI = 250e3, # 500 kS/s max aggregate
        num_PFI=16,
        DAQmx_waits_counter_bug_workaround=False)

NovaTech409B(name='novatech_static', com_port="com4", baud_rate = 115200, phase_mode='aligned')
NovaTech409B_AC(name='novatech', parent_device=pulseblaster_0_clockline_slow, com_port="com3", update_mode='asynchronous', phase_mode='aligned', baud_rate = 115200)
NovaTech440A(name='HFnovatech', com_port='com6', baud_rate = 19200)
StaticDDS('HFDDS', HFnovatech, 'channel 0')

# using NI-MAX alias instead of full VISA name
RS_SMHU(name='SMHU',VISA_name='SMHU58')
RS_SMF100A(name='SMF100A', VISA_name='SMF100A')

# add Lock-In Amplifier
SR865(name='LockIn', VISA_name='SR865')

# call the scope, use NI-MAX alias instead of full name
KeysightXScope(name='Scope',VISA_name='DSOX3024T',
    trigger_device=pulseblaster_0.direct_outputs,trigger_connection='flag 3',
    num_AI=4,DI=False)
ScopeChannel('Heterodyne',Scope,'Channel 1')
#ScopeChannel('Absorption',Scope,'Channel 2')
#ScopeChannel('Modulation',Scope,'Channel 4')

# Define the Wait Monitor for the AC-Line Triggering
# note that connections used here cannot be used elsewhere
# 'connection' needs to be physically connected to 'acquisition_connection'
# for M-Series DAQs, ctr0 gate is on PFI9
WaitMonitor(name='wait_monitor', parent_device=ni_6343, connection='port0/line0', acquisition_device=ni_6343, acquisition_connection='ctr0', timeout_device=ni_6343, timeout_connection='PFI1')

DigitalOut( 'AC_trigger_arm', pulseblaster_0.direct_outputs, 'flag 2')

# define the PB digital outputs
DigitalOut( 'probe_AOM', pulseblaster_0.direct_outputs, 'flag 4')
DigitalOut( 'blue_AOM', pulseblaster_0.direct_outputs, 'flag 5')
#DigitalOut( 'PB_6', pulseblaster_0.direct_outputs, 'flag 6')
#DigitalOut( 'PB_7', pulseblaster_0.direct_outputs, 'flag 7')
#DigitalOut( 'PB_8', pulseblaster_0.direct_outputs, 'flag 8')
DigitalOut( 'PB_9', pulseblaster_0.direct_outputs, 'flag 9')
DigitalOut( 'PB_10', pulseblaster_0.direct_outputs, 'flag 10')
DigitalOut( 'PB_11', pulseblaster_0.direct_outputs, 'flag 11')
DigitalOut( 'PB_12', pulseblaster_0.direct_outputs, 'flag 12')
DigitalOut( 'PB_13', pulseblaster_0.direct_outputs, 'flag 13')
DigitalOut( 'PB_14', pulseblaster_0.direct_outputs, 'flag 14')
DigitalOut( 'PB_15', pulseblaster_0.direct_outputs, 'flag 15')
DigitalOut( 'PB_16', pulseblaster_0.direct_outputs, 'flag 16')
DigitalOut( 'PB_17', pulseblaster_0.direct_outputs, 'flag 17')
DigitalOut( 'PB_18', pulseblaster_0.direct_outputs, 'flag 18')
DigitalOut( 'PB_19', pulseblaster_0.direct_outputs, 'flag 19')
DigitalOut( 'PB_20', pulseblaster_0.direct_outputs, 'flag 20')

# short pulse control channels
DigitalOut(  'bit21', pulseblaster_0.direct_outputs, 'flag 21')
DigitalOut(  'bit22', pulseblaster_0.direct_outputs, 'flag 22')
DigitalOut(  'bit23', pulseblaster_0.direct_outputs, 'flag 23')

AnalogOut( 'ProbeAmpLock', ni_6343, 'ao0')
AnalogOut( 'PSK', ni_6343, 'ao1')
AnalogOut( 'BlueAmpLock', ni_6343, 'ao2')
AnalogOut( 'ni_6343_ao3', ni_6343, 'ao3')

AnalogIn( 'LockIn_X', ni_6343, 'ai0')
AnalogIn( 'LockIn_Y', ni_6343, 'ai1')
AnalogIn( 'PSK_Phase', ni_6343, 'ai2')
AnalogIn( 'AI3', ni_6343, 'ai3')

# this dummy line necessary to balance the digital out for the wait monitor
DigitalOut( 'P0_1', ni_6343, 'port0/line1')

StaticDDS( 'blueAOM', novatech_static, 'channel 0')
StaticDDS( 'ProbeBeatNote', novatech_static, 'channel 1')
StaticDDS( 'ProbeAOM', novatech_static, 'channel 2')
StaticDDS( 'LO', novatech_static, 'channel 3')

DDS( 'dds0', novatech, 'channel 0')
DDS( 'dds1', novatech, 'channel 1')
StaticDDS( 'dds2', novatech, 'channel 2')
StaticDDS( 'dds3', novatech, 'channel 3')

StaticFreqAmp( 'blueEOM', SMHU, 'channel 0', freq_limits=(0.1,4320), amp_limits=(-140,13))
StaticFreqAmp( 'uWaves', SMF100A, 'channel 0', freq_limits=(100e-6,22), amp_limits=(-26,18))

start()

stop(1)
```

### Contribution guidelines ###

* Submitted code should follow labscript\_suite style and guidelines
* Submitted code should also be backwards compatible where possible

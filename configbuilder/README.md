# Cloud Vision Portal State Data

There are several useful python imports in CVP's ConfigBuilder interpreter
to gather state information about the device we're trying to configure, or
CVP itself.

## os.environ 

Environment variables containing information about the instance of CVP. 
This has greatly expanded in version 2021.0. Interesting variables as 
follows:

- `CURRENT_NODE_IP`-- IP Address of the current CVP node.
- `CVP_VERSION`-- Version of CVP running.
- `CVP_MODE`-- singlenode, multinode, cluster
- `PRIMARY_DEVICE_INTF_IP`-- Interface IP of the Primary CVP Node
- `PRIMARY_HOSTNAME`-- Hostname of the Primary CVP Node.
- `PRIMARY_HOST_IP`-- Host IP of the Primary CVP Node.
- `SECONDARY_*`-- ...
- `TERTIARY_*`-- ...

## cvplibrary.CVPGlobalVariables

CVPGlobalVariables contains state information specific to this Config
Builder's session and the device it's configuring. This first set all
return single values.

`CURRENT_DEVICE_IP` `CURRENT_DEVICE_MAC` `CURRENT_DEVICE_SERIAL`
`CVP_IP` `CVP_MAC` `CVP_PASSWORD` `CVP_SERIAL` `CVP_SESSION_ID` 
`CVP_USERNAME` `SCRIPT_ARGS` `ZTP_PASSWORD` `ZTP_STATE` `ZTP_USERNAME`

The following set of Global Variables contain the values of labels
(or tags) associated with devices inside of CVP, giving one the ability
to leverage location in the hierarchy, or specific attributes to
supplement configuration. 

**`NOTE`**-- the returned value is simply a string representation of
a list of colon separated key-value pairs. See  
[CVPLabelExpansion.py](CVPLAbelExpansion.py) for a simple way to
expand these into a dictionary.

- `CVP_SYSTEM_LABELS`-- Builtin labels assigned by CVP.
- `CVP_CUSTOM_LABELS`-- User specified labels.
- `CVP_ALL_LABELS`-- Inclusive set of `CVP_SYSTEM_LABELS` and `VP_CUSTOM_LABELS`

### Builtin labels

`Container:str`  `bgp:disabled|enabled`  `eos:str(version)`   `eostrain:str(maj_version)`    `hostname:str`
`model:str`      `mpls:bool`             `serialnumber:str`   `systype:fixed|modular`        `tapagg:str`
`terminattr:str` `topology_pod:path`     `topology_rack:path` `topology_type:leaf|spine|...` `ztp:bool`



# Examples and Timesaving Snippets

1. **[CVPLabelExpansion.py](CVPLabelExpansion.py)** [[raw](CVPLabelExpansion.py?raw=true)] -- Get useful dictionaries from CVPGlobalVariables and GlobalVariableNames
2. **[L2EVPNBuilderExample.py](L2EVPNBuilderExample.py)** [[raw](L2EVPNBuilderExample.py?raw=true)] -- Example of using python to generate EVPN Configuration.

import os
import cvp
from cvplibrary import Form                as CVPForm, \
                       CVPGlobalVariables  as CVPGV, \
                       GlobalVariableNames as CVPVarNames

# Mutate CVPGlobalsVariables into Mapping => CVPGlobals
# Create Mapping from CVPGlobals['CVP_SYSTEM_LABELS'] => CVPLabels
# Update CVPLabels to include CVPGlobals['CVP_CUSTOM_LABELS'] if it isn't empty.
# ** NOTE: if a custom label could happen to be the same as a system label, 
#          the value in the mapping is overwritten. Not sure this is an issue. Untested. **
CVPGlobals = { varname: CVPGV.getValue(varname) for varname in dir(CVPVarNames) if '__' not in varname }
CVPLabels  = {}
if CVPGlobals['CVP_SYSTEM_LABELS'] is not None:
   CVPLabels = { k: v for (k,v) in [ kv.split(':') for kv in CVPGlobals['CVP_SYSTEM_LABELS'] ] }
   if CVPGlobals['CVP_CUSTOM_LABELS'] is not None:
      CVPLabels.update( { k: v for (k,v) in [ kv.split(':') for kv in CVPGlobals['CVP_CUSTOM_LABELS'] ] } )
 
 
if __name__ == "__main__":
  print("\nOS Environment:\n")
  for (k, v) in os.environ.items():
    print("os.environ['%s']: %s" % (k,v))
  #
  print("\nSample CVP Globals:\n")
  for (k, v) in CVPGlobals.items():
    print("CVPGlobals['%s']: %s" % (k,v))
  #
  print("\nSample CVP Labels:\n")  
  for (k, v) in CVPLabels.items():
    print("CVPLabels['%s']: %s" % (k,v))


"""
#### OUTPUT: #####

NOTE: Some content has been stripped, redacted, or shortened for better viewing
      and to minimize data leakage.
 
OS Environment:

os.environ['AERIS_INGEST_KEY']: <randomkey>
os.environ['CVP_MODE']: singlenode
os.environ['CVP_VERSION']: 2020.2.3
os.environ['HOME']: /
os.environ['HOSTNAME']: <cvphostname.fqdn.example>
os.environ['KUBERNETES_PORT']: tcp://192.0.2.1:443
os.environ['KUBERNETES_PORT_443_TCP']: tcp://192.0.2.1:443
os.environ['KUBERNETES_PORT_443_TCP_ADDR']: 192.0.2.1
os.environ['KUBERNETES_PORT_443_TCP_PORT']: 443
os.environ['KUBERNETES_PORT_443_TCP_PROTO']: tcp
os.environ['KUBERNETES_SERVICE_HOST']: 192.0.2.1
os.environ['KUBERNETES_SERVICE_PORT']: 443
os.environ['KUBERNETES_SERVICE_PORT_HTTPS']: 443
os.environ['PATH']: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
os.environ['PRIMARY_DEVICE_INTF_IP']: 192.168.0.3
os.environ['PRIMARY_HOSTNAME']: <cvphostname.fqdn.example>
os.environ['PRIMARY_HOST_IP']: 192.168.0.3
os.environ['PWD']: /
os.environ['SECONDARY_DEVICE_INTF_IP']: 
os.environ['SECONDARY_HOSTNAME']: 
os.environ['SECONDARY_HOST_IP']: 
os.environ['SHLVL']: 1
os.environ['TERTIARY_DEVICE_INTF_IP']: 
os.environ['TERTIARY_HOSTNAME']: 
os.environ['TERTIARY_HOST_IP']: 
os.environ['_']: /usr/bin/python

Sample CVP Globals:

CVPGlobals['CURRENT_DEVICE_IP']: None
CVPGlobals['CURRENT_DEVICE_MAC']: None
CVPGlobals['CURRENT_DEVICE_SERIAL']: None
CVPGlobals['CVP_ALL_LABELS']: None
CVPGlobals['CVP_CUSTOM_LABELS']: []
CVPGlobals['CVP_IP']: 192.168.0.22
CVPGlobals['CVP_MAC']: XX:XX:XX:XX:XX:XX
CVPGlobals['CVP_PASSWORD']: <cvppassword>
CVPGlobals['CVP_SERIAL']: leaf2-DC1
CVPGlobals['CVP_SESSION_ID']: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...[removedForBrevity]...zz7HPNDr00POCV7Wc
CVPGlobals['CVP_SYSTEM_LABELS']: ['ztp:false', 'terminattr:v1.12.1', 'tapagg:none', 'topology_rack:leaf1-DC1-leaf2-DC1', 'topology_type:leaf', 'bgp:disabled', 'eostrain:4.25', 'systype:fixed', 'eos:4.25.1F', 'topology_pod:OOB-DC1-spine1-DC1-spine2-DC1-spine3-DC1', 'model:cEOSLab', 'hostname:leaf2-DC1', 'Container:DC1', 'Container:Tenant', 'Container:Leaf-DC1', 'Container:Right-DC1', 'mpls:false', 'serialnumber:leaf2-DC1']
CVPGlobals['CVP_USERNAME']: <username>
CVPGlobals['SCRIPT_ARGS']: None
CVPGlobals['ZTP_PASSWORD']: None
CVPGlobals['ZTP_STATE']: false
CVPGlobals['ZTP_USERNAME']: <ztpuser>

Sample CVP Labels:

CVPLabels['Container']: Right-DC1
CVPLabels['bgp']: disabled
CVPLabels['eos']: 4.25.1F
CVPLabels['eostrain']: 4.25
CVPLabels['hostname']: leaf2-DC1
CVPLabels['model']: cEOSLab
CVPLabels['mpls']: false
CVPLabels['serialnumber']: leaf2-DC1
CVPLabels['systype']: fixed
CVPLabels['tapagg']: none
CVPLabels['terminattr']: v1.12.1
CVPLabels['topology_pod']: OOB-DC1-spine1-DC1-spine2-DC1-spine3-DC1
CVPLabels['topology_rack']: leaf1-DC1-leaf2-DC1
CVPLabels['topology_type']: leaf
CVPLabels['ztp']: false

"""

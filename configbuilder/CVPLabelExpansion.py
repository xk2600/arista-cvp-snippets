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
CVPLabels = { k: v for (k,v) in [ kv.split(':') for kv in CVPGlobals['CVP_SYSTEM_LABELS'] ] }
if CVPGlobals['CVP_CUSTOM_LABELS'] is not None:
   CVPLabels.update( { k: v for (k,v) in [ kv.split(':') for kv in CVPGlobals['CVP_CUSTOM_LABELS'] ] } )
 
 
if __name__ == "__main__":
  print("\nSample CVP Globals:\n")
  for (k, v) in CVPGlobals.items():
    print("CVPGlobals['%s']: %s" % (k,v))
  #
  print("\nSample CVP Labels:\n")  
  for (k, v) in CVPLabels.items():
    print("CVPLabels['%s']: %s" % (k,v))

"""
OUTPUT:
 
Sample CVP Globals:
 
CVPGlobals['ZTP_USERNAME']: cvptemp
CVPGlobals['CURRENT_DEVICE_MAC']: None
CVPGlobals['CVP_MAC']: 00:1c:73:c2:c6:01
CVPGlobals['CVP_ALL_LABELS']: None
CVPGlobals['ZTP_STATE']: false
CVPGlobals['CVP_USERNAME']: arista
CVPGlobals['CVP_SESSION_ID']: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWQiOjQ5LCJkc24iOiJhcmlzdGEiLCJkc3QiOiJ1c2VyIiwic2lkIjoiZTZkNmNiZDEyMjljZmQ4YTNjN2JmOWY2Y2QxZjg5ZGY2ZmVjYmQ4MmE4OGI5NGU0N2Y4NzE1MTM3M2ZkNDU0NC1MeXV5X2JfVDlZYmhMeENmY0FxNmNQMi04UFRPY2psb0x0Q25KMDhSIn0.sLu3OHDWGdcXf3au6ix8DAitKX43tWXvEASaIlY8wiGD3Hben3ZdP5ggNdxs9gyNnftXtj-MsQJXt37XivbW1Ejvm_voiQ2VREQ40qR4v7E1IIUDmfJzWaYGg6nprBCuSaCm6dQGWGRN451CeGVizz3aMIsmgr_r-AmW9BhteH0YBFuKZ0EZo_y00pALcV_-mbojUyXawL3hX_lp8e5QSTzMl7HxYIotFlnN9be-SpPUn51_uYB7jMgd0VewhDltekRW0tT8t2EDqBxCayUltjjn2evvZYaWJY0_ibPORuaQZgLiEtc3AzVMmgGn9iHqdmEweceL2FCet8Rb2XUGsNFgA2JRb6HbBR2Lm9UZauXMeb1hkdJbqBVOC_89uCevZdoL1_Np5Q2VWq4a1885xnsar1Nz-7bTtH1-OPHOO6xz5QyDi6H6kjT38iFq5ORSfBpze4a4FzahyVwrjq9aitLr7jeLhRlRv4ckeUKZ2Mj0KVDYPG7lt6PsGwi1FmlwODW5AGV-PBLaS3p7wyNYfgjkuKY01OlmBOK8M61SN783n03SrWpLWEtH7MoIZl_b3kAiwsX1BO-AKlvB8nTt99SMGfM6AjWojm7XYU94wpQiGtxbTfJ-n-2J3GNG5EZW7tLkNM_D0ArbICH7VHtLgrjk3-zz7HPNDr00POCV7Wc
CVPGlobals['CURRENT_DEVICE_SERIAL']: None
CVPGlobals['CVP_CUSTOM_LABELS']: []
CVPGlobals['ZTP_PASSWORD']: None
CVPGlobals['CVP_IP']: 192.168.0.22
CVPGlobals['CVP_PASSWORD']: aristaXXXX
CVPGlobals['SCRIPT_ARGS']: None
CVPGlobals['CVP_SYSTEM_LABELS']: ['bgp:disabled', 'tapagg:none', 'eostrain:4.25', 'topology_rack:leaf1-DC1-leaf2-DC1', 'topology_type:leaf', 'mpls:false', 'systype:fixed', 'topology_pod:OOB-DC1-spine1-DC1-spine2-DC1-spine3-DC1', 'Container:DC1', 'Container:Tenant', 'Container:Leaf-DC1', 'Container:Right-DC1', 'hostname:leaf2-DC1', 'model:cEOSLab', 'eos:4.25.1F', 'ztp:false', 'serialnumber:leaf2-DC1', 'terminattr:v1.12.1']
CVPGlobals['CURRENT_DEVICE_IP']: None
CVPGlobals['CVP_SERIAL']: leaf2-DC1
 
Sample CVP Labels:
 
CVPLabels['tapagg']: none
CVPLabels['hostname']: leaf2-DC1
CVPLabels['Container']: Right-DC1
CVPLabels['eos']: 4.25.1F
CVPLabels['topology_pod']: OOB-DC1-spine1-DC1-spine2-DC1-spine3-DC1
CVPLabels['mpls']: false
CVPLabels['serialnumber']: leaf2-DC1
CVPLabels['bgp']: disabled
CVPLabels['topology_rack']: leaf1-DC1-leaf2-DC1
CVPLabels['topology_type']: leaf
CVPLabels['terminattr']: v1.12.1
CVPLabels['model']: cEOSLab
CVPLabels['systype']: fixed
CVPLabels['ztp']: false
CVPLabels['eostrain']: 4.25

"""

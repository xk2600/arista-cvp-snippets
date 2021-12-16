from cvplibrary import CVPGlobalVariables, GlobalVariableNames, Form

# setup some global variables
serial = CVPGlobalVariables.getValue( GlobalVariableNames.CVP_SERIAL )

def create_macvrf(originrd, vlanid):
  """ create a MAC VRF to extend a VLAN across an EVPN Fabric. """
  rd = "%s:%s" % (originrd, vlanid)
  rt = "%s:10%s" % (vlanid, vlanid)
  config = """
      vlan %s
        rd %s
        route-target both %s
        redistribute learned
  """.rstrip()
  print(config % (vlanid, rd, rt))


def create_bundle(name, originrd, bundleid, *vlans):
  vlans = ','.join(tuple(map(str,vlans)))
  rd = "%s:%s" % (originrd, bundleid)
  rt = "%s:%s" % (bundleid, bundleid)
  config = """
      vlan-aware-bundle %s
        rd %s
        route-target both %s
        vlan %s
        redistribute learned
  """.rstrip()
  print(config % (name, rd, rt, vlans))


def config_evpn(bgpas, originrd):
  config = """
    router bgp %s
      neighbor 10.21.21.21 peer group EVPN-OVERLAY
      neighbor 10.22.22.22 peer group EVPN-OVERLAY
      neighbor 10.23.23.23 peer group EVPN-OVERLAY
      neighbor EVPN-OVERLAY send-community
      neighbor EVPN-OVERLAY ebgp-multihop
      neighbor EVPN-OVERLAY remote-as 65100
      neighbor EVPN-OVERLAY update-source loopback 0
      neighbor EVPN-OVERLAY maximum-routes 0
      
      address-family ipv4
        no neighbor EVPN-OVERLAY activate
      
      address-family evpn
        neighbor EVPN-OVERLAY activate
        bgp next-hop-unchanged
  """.rstrip()
  print(config % bgpas)
  # create per VLAN MAC VRFs by uncommenting the following two lines.
  #create_macvrf(originrd, 101)
  #create_macvrf(originrd, 201)
  # create a single MAC VRF with multiple vlans.
  create_bundle('leafvlans', originrd, 1, 101, 201)



if serial == '7F1667B95972F1249854FF8B2FDB976B':
 hostname = 'leaf1'
 config_evpn(65001, '10.11.11.11')
elif serial == '1039AC16817F5F0F37DBE49446726B9A':
 hostname = 'leaf2'
 config_evpn(65002, '10.12.12.12')
elif serial == '1543A1F849F99C9BCA2C1B2BBD0E518C':
 hostname = 'leaf3'
 config_evpn(65003, '10.13.13.13')
elif serial == '24D4FA4BE0302370AE38F66CAE0EDF1C':
 hostname = 'leaf4'
 config_evpn(65004, '10.14.14.14')
elif serial == '12A9CA08642AED44098E9D3A5E0DDDDA':
 hostname = 'spine1'
elif serial == 'C6C4EE7B77B915B86B937A8931FEF756':
 hostname = 'spine2'
elif serial == '85A471905320E1D1B8FDA0CC7264F7A6':
 hostname = 'spine3'
elif serial == '7094BACB7F8ACFE709B7460887419955':
 hostname = 'borderleaf1'
elif serial == 'A0CEAF2B20525BC40F26552C65B165C9':
 hostname = 'borderleaf2'
elif serial == 'DEA8705692D5C2889ACDDBAB66C42E88':
 hostname = 'host1'
elif serial == 'C3A2A37812CAEE651CAFA5B1CE15C8B9':
 hostname = 'host2'



from cvplibrary import CVPGlobalVariables, GlobalVariableNames, Form
import jinja2 as j2

""" FILESYSTEM TEMPLATE STORAGE EXAMPLE...
template_loader = j2.FileSystemLoader('./templates')
env = j2.Environment(loader=template_loader, undefined=jinja2.DebugUndefined) """

########## NOTE IMCOMPLETE ###################



# Customize (wrapped) Dictionary permitting dot traversal.
class Model:
  def __init__(self, *args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and isinstance(args, dict):
      kwargs = args[0]
    if isinstance(args, dict):
      self.__do_init__self, *args, **kwargs)
  def __do_init__(self, *args, **kwargs):
    for attr, value in kwargs.items():
      if isinstance(value, dict):
        value = Model(value)
      elif value is (list, tuple):
        vlist = value
        value = []
        for item in vlist:
          if isinstance(item, dict):
            item = Model(item)
          value.append(item)
      if not isinstance(attr, str):
        attr = str(attr)
      setattr(self, attr, value)
  def items(self):
    r = {}
    for attr, value in self.__dict__.items():
      if isinstance(value, Model):
        value = value.items()
      elif isinstance(value, (list, tuple)):
        vlist = value
        value = []
        for item in vlist:
          if isinstance(item, Model):
            item = item.items()
          value.append(item)
      r.update({attr: value})
    return r
  def keys(self):
    return self.__dict__.keys()
  def __getitem__(self, attr):
    if isinstance(attr, int):
      # autocast integers to strings
      attr = str(attr)
    return self.__dict__[attr]
  def __str__(self):
    return "Model(%s)" % str(self.items())
  
class Template(Model):
  def render(template, **data):
    template = j2.Environment(loader=BaseLoader()).from_string(template)
    template.render(data)

device = Model({
  '7F1667B95972F1249854FF8B2FDB976B': {
    'hostname': 'leaf1',
    'bgpas': '65001',
    'macvrf': {},
    'v4vrf': {
      'default': {
        'ip': {
          'loopback0': '10.11.11.11/32'
        }
      }
    }
  },
  '1039AC16817F5F0F37DBE49446726B9A': {
    'hostname': 'leaf2',
    'bgpas': '65002',
    'macvrf': {},
    'v4vrf': {
      'default': {
        'ip': {
          'loopback0': '10.12.12.12/32'
        }
      },
      'tenant-202': {
        'vni': 2222, 
        'ip': {
          'ethernet6': '192.168.201.254/24'
        }
      }
    }
  },
  '1543A1F849F99C9BCA2C1B2BBD0E518C': {
    'hostname': 'leaf3',
    'bgpas': '65003',
    'macvrf': {},
    'v4vrf': {
      'default': {
        'ip': {
          'loopback0': '10.13.13.13/32'
        }
      }
    }
  },
  '24D4FA4BE0302370AE38F66CAE0EDF1C': {
    'hostname': 'leaf4',
    'bgpas': '65004',
    'macvrf': {},
    'v4vrf': {
      'default': {
        'ip': {
          'loopback0': '10.14.14.14/32'
      },
      'tenant-202': {
        'vni': 2222, 
        'ip': {
          'ethernet6': '192.168.202.254/24'
        }
      }
    }
  },
  '12A9CA08642AED44098E9D3A5E0DDDDA': {
    'hostname': 'spine1'
  },
  'C6C4EE7B77B915B86B937A8931FEF756': {
    'hostname': 'spine2'
  },
  '85A471905320E1D1B8FDA0CC7264F7A6': {
    'hostname': 'spine3'
  },
  '7094BACB7F8ACFE709B7460887419955': {
    'hostname': 'borderleaf1'
  },
  'A0CEAF2B20525BC40F26552C65B165C9': {
    'hostname': 'borderleaf2'
  },
  'DEA8705692D5C2889ACDDBAB66C42E88': {
    'hostname': 'host1'
  },
  'C3A2A37812CAEE651CAFA5B1CE15C8B9': {
    'hostname': 'host2'
  }
})


Template({
  "l3evpn": """
  
    router bgp {{ bgpas }}
      {% for spine in spines %}
      neighbor {{ spine.v4vrf.default.loopback0.ip }} peer group EVPN-OVERLAY
      {% endfor %}
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
        
      {% for name, items in macvrf.items %}
        vrf {{ name }}
          rd {{ rd }}
          route-target import evpn {{ rt }}
          route-target export evpn {{ rt }}
          redistribute connected
          redistribute static
      {% endfor %}
  """})


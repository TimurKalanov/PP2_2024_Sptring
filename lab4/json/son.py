import json
file = open('sample-data.json')
sonn = json.load(file)
print(f'\nInterface status\n{"="*80}\nDN{" "* 49}Description{" " * 11}Speed    MTU  ')
for data in sonn['imdata']:
    size_of_dn = len(data["l1PhysIf"]["attributes"]["dn"])
    size_of_descr = len(data['l1PhysIf']['attributes']['descr'])
    
    print(data['l1PhysIf']['attributes']['dn'], " " * (49 - size_of_dn), 
          data['l1PhysIf']['attributes']['descr'], " " * (20 - size_of_descr),
          data['l1PhysIf']['attributes']['fecMode'], "",
          data['l1PhysIf']['attributes']['mtu']
          )
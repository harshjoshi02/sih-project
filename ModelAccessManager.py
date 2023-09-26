import os,uuid,json
import datetime
import config
KeyFolder,InventoryFile=('Keys','KeyData.txt')


def CountActiveKeys(InventoryFile):
    key_data=read_key_data(InventoryFile)
    return len(key_data.keys())

def returnvalidkey(InventoryFile):
    if InventoryFile==None:
      InventoryFile=config.InventoryFile
    data=read_key_data(InventoryFile)
    keyids,keyfilenames,keyusage=list(data.keys()),[],[]
    for val in data.values():
      keyfilenames.append(val[0]),keyusage.append(val[1])
    indx=keyusage.index(min(keyusage))
    update_usage(InventoryFile,keyids[indx])
    KeyFileAddress=KeyFolder+'/'+str(keyfilenames[indx])
    return readsecurekey(KeyFileAddress)


def readsecurekey(KeyFileAddress):
    with open(KeyFileAddress, "r") as f:
      value=f.readline()
      return value


def update_key_data(folder, InventoryFile):
  recorded_files=[val[0] for val in read_key_data(InventoryFile).values()]
  key_files,key_data = ([InventoryFile for InventoryFile in os.listdir(folder)],read_key_data(InventoryFile))
  
  for file in key_files:
    if file in recorded_files:
      pass
    else:
      k_id,usecount= len(key_data.keys())+1,0
      key_data[k_id] = (str(file),usecount)
      print("New Key file added: Updated Inventory - ADDED:",k_id,file,usecount)
  
  for key,val in list(key_data.items()):
    file,usecount=val[0],val[1]
    if file in key_files:
      pass
    else:
      print("Key file removed from storage: Updated Inventory - REMOVED:",key_data[key])
      del key_data[key]
  write_key_data(InventoryFile, key_data)

def update_usage(InventoryFile,KeyId):
    key_data=read_key_data(InventoryFile)
    name,usage=(key_data[KeyId][0],key_data[KeyId][1])
    print('Model Access recorded at',datetime.datetime.now())
    key_data[KeyId]=(name,usage+1)
    write_key_data(InventoryFile,key_data)
    
def read_key_data(InventoryFile):
  with open(InventoryFile, "r") as f:
    try:
      key_data = json.load(f)
    except json.JSONDecodeError:
      print("The file is empty or invalid:", InventoryFile)
      key_data = {}
  return key_data

def write_key_data(InventoryFile, key_data):
  with open(InventoryFile, "w") as f:
    json.dump(key_data, f)


update_key_data(KeyFolder,InventoryFile)
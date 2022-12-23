import pymem,time
while (True):
  try:
    pm = pymem.Pymem("voicemeeter8.exe")
    pm.write_int(pm.process_base.lpBaseOfDll + 0x11FBE8,0)
    time.sleep(5)
  except: pass

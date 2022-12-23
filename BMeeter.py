import pymem,time
while (True):
  time.sleep(5)
  try:
    pm = pymem.Pymem("voicemeeter8.exe")
    pm.write_int(pm.process_base.lpBaseOfDll + 0x11FBE8,0)
  except: pass

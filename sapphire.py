from pymem import Pymem
from pymem.process import module_from_name
from requests import get

dwEntityList = (0x4D533AC) #81081260
dwForceAttack = (0x3184930) #51923248
dwLocalPlayer = (0xD3ED14) #13888788
m_iCrosshairId = (0xB3E4) #46052
m_iTeamNum = (0xF4) #244

pm = Pymem("csgo.exe")
client = module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

print("Sapphire has launched.")

abierto=True
while abierto:
    player = pm.read_int(client + dwLocalPlayer)
    entity_id = pm.read_int(player + m_iCrosshairId)
    entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

    entity_team = pm.read_int(entity + m_iTeamNum)
    player_team = pm.read_int(player + m_iTeamNum)

    if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
        pm.write_int(client + dwForceAttack, 6)



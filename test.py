from nanonisTCP import nanonisTCP
from nanonisTCP.Scan import Scan

IP = '127.0.0.1'
PORT = 6501

NTCP = nanonisTCP(IP,PORT)

scan_module = Scan(NTCP)
print(scan_module.PropsGet())
scan_module.PropsSet(series_name="%y%m%d_SPM_")

NTCP.close_connection()
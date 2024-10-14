import os
while True:
    try:
        print("run script")
        os.system('D:\\Frp\\frp_0.53.2_windows_amd64\\frpc.exe -c D:\\Frp\\frp_0.53.2_windows_amd64\\frpc.toml')
    except Exception as e:
        print(f'error {e}')
        import time
        time.sleep(1000)
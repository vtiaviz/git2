
import requests
import speedtest

def verificar_conexao():
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def medir_velocidade():
    st = speedtest.Speedtest()
    st.get_best_server()
    download = st.download() / 1_000_000  # em Mbps
    upload = st.upload() / 1_000_000      # em Mbps
    ping = st.results.ping
    return download, upload, ping

if verificar_conexao():
    print("Conectado à internet!")
    download, upload, ping = medir_velocidade()
    print(f"Velocidade de download: {download:.2f} Mbps")
    print(f"Velocidade de upload: {upload:.2f} Mbps")
    print(f"Ping: {ping} ms")
else:
    print("Sem conexão com a internet.")
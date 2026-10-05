import requests

# Defina apenas a URL base do seu projeto (sem /rest/v1/ no final)
SUPABASE_URL = "https://your-project.supabase.co"  # Substitua pelo URL do seu projeto
SUPABASE_KEY = "your-supabase-key"  # Substitua pela sua chave de API do Supabase
TABELA = "your_table_name"  # Substitua pelo nome da tabela que deseja consultar

url = f"{SUPABASE_URL}/rest/v1/{TABELA}?select=id&limit=1"

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Supabase mantido ativo com sucesso!")
    else:
        print(f"Erro ao conectar: {response.status_code} - {response.text}")
except Exception as e:
    print(f"Falha na requisição: {e}")
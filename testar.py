# testar_api.py atualizado
import requests
import sys

print("🔍 Testando API Flask...\n")

# Teste 1: Rota raiz
try:
    response = requests.get('http://localhost:5000/')
    print(f"✓ Rota raiz (/): {response.status_code}")
    print(f"  Resposta: {response.text}\n")
except Exception as e:
    print(f"✗ Erro na rota raiz: {e}\n")

# Teste 2: Rota /api/feliz
try:
    response = requests.get('http://localhost:5000/api/feliz')
    print(f"✓ Rota /api/feliz: {response.status_code}")
    print(f"  Resposta: {response.json()}\n")
except Exception as e:
    print(f"✗ Erro na rota /api/feliz: {e}\n")

# Teste 3: Rota /api/triste
try:
    response = requests.get('http://localhost:5000/api/triste')
    print(f"✓ Rota /api/triste: {response.status_code}")
    print(f"  Resposta: {response.json()}\n")
except Exception as e:
    print(f"✗ Erro na rota /api/triste: {e}\n")

print("✅ Teste concluído!")
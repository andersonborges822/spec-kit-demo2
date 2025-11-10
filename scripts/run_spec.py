import yaml, subprocess, os

print("🚀 Executando Spec Kit (simulado no GitHub Actions)...")

# Lê o arquivo spec.yml
with open("spec.yml", "r", encoding="utf-8") as f:
    spec = yaml.safe_load(f)

# Cria estrutura básica de diretórios
os.makedirs("scripts", exist_ok=True)
os.makedirs("tests", exist_ok=True)
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)
os.makedirs("models", exist_ok=True)

# Cria os arquivos indicados em 'generate'
for item in spec.get("generate", []):
    for path, prompt in item.items():
        # Garante que o diretório do arquivo exista
        os.makedirs(os.path.dirname(path), exist_ok=True)
        # Gera o conteúdo simulado
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# Gerado automaticamente pelo Spec Kit\n")
            f.write(f"# Instrução original:\n# {prompt}\n\n")
            f.write("print('Arquivo gerado automaticamente!')\n")

# Executa as etapas listadas em 'steps'
for step in spec.get("steps", []):
    print(f"\n➡️ Etapa: {step['id']}")
    cmd = step["run"]
    print(f"Executando: {cmd}")
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"✅ Etapa {step['id']} concluída!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro na etapa {step['id']}: {e}")
        break

print("\n🏁 Processo do Spec Kit finalizado com sucesso!")

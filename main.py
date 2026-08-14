print("========================================")
print("  SISTEMA DE TRIAGEM - HELP DESK TI & OPS")
print("========================================\n")

# 1. Entrada de dados (Simulando o usuário abrindo um chamado)
nome_usuario = input("Digite o seu nome: ")
descricao_problema = input("Descreva brevemente o problema ou chamado: ").lower()

print("\n--- Processando Chamado... ---")

# 2. Lógica de Triagem (Análise de dados simples por palavras-chave)
if "senha" in descricao_problema or "computador" in descricao_problema or "sistema" in descricao_problema:
    setor_destino = "SUPORTE TÉCNICO DE TI (HELP DESK)"
    prioridade = "ALTA"
    
elif "devolução" in descricao_problema or "retorno" in descricao_problema or "avariado" in descricao_problema:
    setor_destino = "LOGÍSTICA REVERSA / QUALIDADE"
    prioridade = "MÉDIA"
    
elif "nota" in descricao_problema or "fiscal" in descricao_problema or "faturamento" in descricao_problema:
    setor_destino = "DEPARTAMENTO DE FATURAMENTO / PORTARIA"
    prioridade = "MÉDIA"
    
else:
    setor_destino = "ATENDIMENTO GERAL / TRIAGEM MANUAL"
    prioridade = "BAIXA"

# 3. Exibição do Resultado (Simulando a saída do sistema)
print(f"Chamado aberto com sucesso por: {nome_usuario}")
print(f"Encaminhado para o setor: {setor_destino}")
print(f"Nível de Prioridade: {prioridade}")
print("========================================")

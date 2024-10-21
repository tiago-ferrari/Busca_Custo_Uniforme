import heapq

def busca_custo_uniforme(grafo, inicio, objetivo):
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, inicio))  # (custo total, nodo atual)

    custos_acumulados = {inicio: 0}
    caminhos = {inicio: []}
    visitados = set()

    while fila_prioridade:
        custo_total, nodo_atual = heapq.heappop(fila_prioridade)

        if nodo_atual in visitados:
            continue

        visitados.add(nodo_atual)

        if nodo_atual == objetivo:
            return custos_acumulados[nodo_atual], caminhos[nodo_atual] + [nodo_atual]

        for vizinho, distancia in grafo[nodo_atual].items():
            if vizinho in visitados:
                continue

            novo_custo = custos_acumulados[nodo_atual] + distancia
            if vizinho not in custos_acumulados or novo_custo < custos_acumulados[vizinho]:
                custos_acumulados[vizinho] = novo_custo
                heapq.heappush(fila_prioridade, (novo_custo, vizinho))
                caminhos[vizinho] = caminhos[nodo_atual] + [nodo_atual]

    return float("inf"), []  # Se não encontrar o objetivo

# Definição do grafo
grafo = {
    'entrada_ifc_alt': {'canto_galpao_maq': 168, 'entrada_salas_2': 113, 'estacionamento': 52},
    'canto_galpao_maq': {'entrada_ifc_alt': 168, 'laboratorios': 102, 'circulo': 93, 'entrada_salas_2': 78},
    'laboratorios': {'canto_galpao_maq': 102, 'auditorio': 83, 'circulo': 58},
    'auditorio': {'laboratorios': 83, 'mini_auditorio': 55},
    'mini_auditorio': {'auditorio': 55, 'biblioteca': 53, 'entrada_salas_1': 75, 'pedagogico': 99},
    'biblioteca': {'mini_auditorio': 53, 'pedagogico': 92, 'cantina': 70},
    'cantina': {'biblioteca': 70, 'pedagogico': 60, 'entrada_salas_1': 90, 'refeitorio': 187, 'bancos_lago': 155},
    'refeitorio': {'cantina': 187, 'ginasio': 120},
    'ginasio': {'refeitorio': 120, 'bancos_lago': 150},
    'bancos_lago': {'cantina': 155, 'ginasio': 150, 'guarita': 65},
    'guarita': {'bancos_lago': 65, 'entrada_salas_1': 120, 'pedagogico': 130, 'administrativo': 51, 'estacionamento': 36},
    'estacionamento': {'guarita': 36, 'administrativo': 35, 'entrada_ifc_alt': 52},
    'administrativo': {'estacionamento': 35, 'guarita': 51, 'entrada_salas_1': 52},
    'entrada_salas_1': {'guarita': 120, 'entrada_salas_2': 85, 'circulo': 58, 'pedagogico': 42, 'administrativo': 52, 'cantina': 90, 'mini_auditorio': 75},
    'entrada_salas_2': {'entrada_ifc_alt': 113, 'canto_galpao_maq': 78, 'entrada_salas_1': 85, 'circulo': 70},
    'circulo': {'laboratorios': 58, 'canto_galpao_maq': 93, 'entrada_salas_2': 70, 'entrada_salas_1': 58},
    'pedagogico': {'mini_auditorio': 99, 'biblioteca': 92, 'cantina': 60, 'guarita': 130, 'entrada_salas_1': 42}
}

custo, caminho = busca_custo_uniforme(grafo, 'administrativo', 'refeitorio')
print("Custo total:", custo)
print("Caminho:", caminho)

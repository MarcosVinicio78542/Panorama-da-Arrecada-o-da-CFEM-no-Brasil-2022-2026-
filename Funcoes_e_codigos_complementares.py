import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# Dicionário de padronização por categoria de bem mineral
unidades_padrao = {
    # MINERAIS METÁLICOS (toneladas)
    'MINÉRIO DE FERRO': 't',
    'FERRO': 't',
    'MINÉRIO DE MANGANÊS': 't',
    'MANGANÊS': 't',
    'MINÉRIO DE OURO': 't',
    'OURO': 'kg',  # Para ouro, kg é mais comum que toneladas
    'OURO NATIVO': 'kg',
    'MINÉRIO DE COBRE': 't',
    'COBRE': 't',
    'MINÉRIO DE ZINCO': 't',
    'ZINCO': 't',
    'MINÉRIO DE ESTANHO': 't',
    'ESTANHO': 't',
    'MINÉRIO DE TUNGSTÊNIO': 't',
    'TUNGSTÊNIO': 't',
    'MINÉRIO DE NÍQUEL': 't',
    'NÍQUEL': 't',
    'MINÉRIO DE CHUMBO': 't',
    'CHUMBO': 't',
    'MINÉRIO DE ALUMÍNIO': 't',
    'ALUMÍNIO': 't',
    'MINÉRIO DE TÂNTALO': 't',
    'TÂNTALO': 'kg',  # Geralmente em kg para minérios preciosos
    'MINÉRIO DE NIÓBIO': 't',
    'NIÓBIO': 't',
    'MINÉRIO DE PRATA': 't',
    'PRATA': 'kg',
    'MINÉRIO DE TITÂNIO': 't',
    'TITÂNIO': 't',
    'MINÉRIO DE ZIRCÔNIO': 't',
    'ZIRCÔNIO': 't',
    'MINÉRIO DE BERÍLIO': 't',
    'MINÉRIO DE VANÁDIO': 't',
    'MINÉRIO DE LÍTIO': 't',
    'MINÉRIO DE SILÍCIO': 't',
    
    # MINERAIS NÃO-METÁLICOS/INDUSTRIAIS (toneladas)
    'CAULIM': 't',
    'TALCO': 't',
    'FELDSPATO': 't',
    'GIPSITA': 't',
    'GIPSO': 't',
    'MAGNESITA': 't',
    'DIATOMITO': 't',
    'FOSFATO': 't',
    'FLUORITA': 't',
    'BARITA': 't',
    'PIROFILITA': 't',
    'BENTONITA': 't',
    'VERMICULITA': 't',
    'APATITA': 't',
    'GRAFITA': 't',
    'ILMENITA': 't',
    'MAGNETITA': 't',
    'HEMATITA': 't',
    'PIRITA': 't',
    'CROMITA': 't',
    'MONAZITA': 't',
    'ZIRCONITA': 't',
    'MOLIBDENITA': 't',
    'SCHEELITA': 't',
    'CASSITERITA': 't',
    'COLUMBITA': 't',
    'TANTALITA': 't',
    'TANTALITA-COLUMBITA': 't',
    'PIROCLORO': 't',
    'ESPODUMÊNIO': 't',
    'BERILO': 't',
    
    # ROCHAS ORNAMENTAIS E DE REVESTIMENTO (m³ ou m²)
    'GRANITO': 'm³',
    'MÁRMORE': 'm³',
    'ARDÓSIA': 'm²',  # Ardósia geralmente vendida por m²
    'BASALTO': 'm³',
    'XISTO': 'm³',
    'QUARTZITO': 'm³',
    'SIENITO': 'm³',
    'GNAISSE': 'm³',
    'DIABÁSIO': 'm³',
    'GRANITO ORNAMENTAL': 'm³',
    'GRANITO P/ REVESTIMENTO': 'm³',
    'MÁRMORE P/ REVESTIMENTO': 'm³',
    'BASALTO P/ REVESTIMENTO': 'm³',
    
    # ROCHAS PARA BRITA (m³)
    'GRANITO P/ BRITA': 'm³',
    'BASALTO P/ BRITA': 'm³',
    'DIABÁSIO P/ BRITA': 'm³',
    'BRITA DE GRANITO': 'm³',
    'GNAISSE P/ BRITA': 'm³',
    
    # ROCHAS DIVERSAS (m³)
    'ARENITO': 'm³',
    'CALCÁRIO': 'm³',
    'DOLOMITO': 'm³',
    'FILITO': 'm³',
    'MIGMATITO': 'm³',
    'RIÓLITO': 'm³',
    'DIORITO': 'm³',
    'GABRO': 'm³',
    'TONALITO': 'm³',
    'GRANODIORITO': 'm³',
    'DACITO': 'm³',
    'TRAQUITO': 'm³',
    'ANDESITO': 'm³',
    'FONÓLITO': 'm³',
    'CONGLOMERADO': 'm³',
    'SILTITO': 'm³',
    'ARGILITO': 'm³',
    'FOLHELHO': 'm³',
    'FOLHELHO ARGILOSO': 'm³',
    'XISTO ARGILOSO': 'm³',
    'MARGA': 'm³',
    'ARCÓSIO': 'm³',
    'ANFIBOLITO': 'm³',
    'MICAXISTO': 'm³',
    'SERPENTINITO': 'm³',
    'PIROXENITO': 'm³',
    'CHARNOQUITO': 'm³',
    'PEGMATITO': 'm³',
    'CARBONATITO': 'm³',
    'TINGUAÍTO': 'm³',
    'SIENO GRANITO': 'm³',
    'GRANULITO': 'm³',
    'LEUCOFILITO': 'm³',
    
    # AGREGADOS PARA CONSTRUÇÃO CIVIL (m³)
    'AREIA': 'm³',
    'AREIA INDUSTRIAL': 'm³',
    'AREIA DE FUNDIÇÃO': 'm³',
    'AREIA P/ VIDRO': 'm³',
    'AREIA QUARTZOSA': 'm³',
    'AREIA ALUVIONAR': 'm³',
    'AREIA DE BARRANCO': 'm³',
    'AREIA FLUVIAL': 'm³',
    'AREIA LAVADA': 'm³',
    'AREIA COMUM': 'm³',
    'SAIBRO': 'm³',
    'CASCALHO': 'm³',
    'SEIXOS': 'm³',
    'SEIXOS ROLADOS': 'm³',
    
    # MATERIAIS CERÂMICOS (toneladas)
    'ARGILA': 't',
    'ARGILA REFRATÁRIA': 't',
    'ARGILA VERMELHA': 't',
    'ARGILA P/CER. VERMELH': 't',
    'ARGILA BENTONÍTICA': 't',
    'ARGILA COMUM': 't',
    'ARGILA BRANCA': 't',
    'ARGILA FERRUGINOSA': 't',
    'ARGILA CAULÍNICA': 't',
    'LATERITA': 't',
    
    # GEMA E PEDRAS PRECIOSAS (gramas ou quilates)
    'DIAMANTE': 'ct',  # quilates
    'DIAMANTE INDUSTRIAL': 'ct',
    'ESMERALDA': 'g',
    'RUBI': 'g',
    'SAFIRA': 'g',
    'AMETISTA': 'kg',  # Ametista em kg é comum no Brasil
    'ÁGATA': 'kg',
    'TOPÁZIO': 'g',
    'ÁGUA MARINHA': 'g',
    'TURMALINA': 'g',
    'OPALA': 'g',
    'CITRINO': 'g',
    'GRANADA': 'g',
    'ALEXANDRITA': 'g',
    'KUNZITA': 'g',
    'MORGANITA': 'g',
    'CALCEDÔNIA': 'kg',
    'QUARTZO': 't',  # Quartzo industrial em toneladas
    'QUARTZO RÓSEO': 'kg',
    'GEMA': 'g',
    
    # COMBUSTÍVEIS FÓSSEIS (toneladas)
    'CARVÃO MINERAL': 't',
    'CARVÃO': 't',
    'TURFA': 't',
    
    # SALES MINERAIS (toneladas)
    'SALGEMA': 't',
    'SILVINITA': 't',
    
    # ÁGUAS MINERAIS (litros ou m³)
    'ÁGUA MINERAL': 'm³',
    'ÁGUA POTÁVEL DE MESA': 'm³',
    'ÁGUAS TERMAIS': 'm³',
    'ÁGUA MINERAL RAD. FON': 'm³',
    'ÁGUA MINERAL CARBOGAS': 'm³',
    
    # OUTROS
    'URÂNIO': 't',
    'TERRAS RARAS': 't',
    'CONCHAS CALCÁRIAS': 'm³',
    'CALCITA': 't',
    'HIDRARGILITA': 't',
    'OCRE': 't',
    'ATAPULGITA': 't',
    'SAPONITO': 't',
    'SODALITA': 't',
    'CIANITA': 't',
    'LEUCITA': 't',
    'QUARTZITO INDUSTRIAL': 't',
    'QUARTZITO DUMORTIERITA': 't',
    'CALCÁRIO DOLOMÍTICO': 'm³',
    'CALCÁRIO CALCÍTICO': 'm³',
    'CALCÁRIO INDUSTRIAL': 't',
    'BAUXITA': 't',
    'BAUXITA FOSFOROSA': 't',
    'ROCHA POTÁSSICA': 't',
    'ALUVIÃO ESTANÍFERO': 'm³',
    'ESTEATITO': 't',
    'AMIANTO': 't',
    'ANFIBÓLIO': 't',
    'AGALMATOLITO': 't',
    'MOSCOVITA': 't',
    'MICA': 't',
    'PEDRA CORADA': 't',
    'SÍLEX': 't'
}

def padronizar_unidades(dados):
    """
    Padroniza unidades de medida em um DataFrame de bens minerais
    """
    # Criar cópia do DataFrame
    dados_padronizado = dados.copy()
    
    # Aplicar padronização
    dados_padronizado['UnidadePadronizada'] = dados_padronizado['Bens_minerais'].map(
        lambda x: unidades_padrao.get(x, 't')  # Padrão: toneladas
    )
    
    # Se houver coluna de quantidade, podemos criar uma coluna convertida
    if 'Quantidade' in dados.columns:
        # Função auxiliar para conversão
        def converter_quantidade(row):
            unidade_orig = row['UnidadeDeMedida'].strip().lower()
            unidade_dest = row['UnidadePadronizada']
            quantidade = row['Quantidade']
            
            # Se já está na unidade padrão, mantém
            if unidade_orig == unidade_dest:
                return quantidade
            
            # Fatores de conversão básicos
            conversoes = {
                ('kg', 't'): lambda x: x / 1000,
                ('g', 't'): lambda x: x / 1000000,
                ('g', 'kg'): lambda x: x / 1000,
                ('t', 'kg'): lambda x: x * 1000,
                ('kg', 'g'): lambda x: x * 1000,
                ('ct', 'g'): lambda x: x * 0.2,  # 1 quilate = 0.2g
                ('g', 'ct'): lambda x: x / 0.2,
            }
            
            chave = (unidade_orig, unidade_dest)
            if chave in conversoes:
                return conversoes[chave](quantidade)
            
            # Para conversões m³ ↔ t, precisaria de densidade específica
            # Aqui mantemos o valor se não houver conversão direta
            return quantidade
        
        dados_padronizado['QuantidadePadronizada'] = dados_padronizado.apply(
            converter_quantidade, axis=1
        )
    
    return dados_padronizado


def criar_grafico_barras_horizontais(dados, x_col, y_col, titulo='', xlabel='', ylabel='',
                                     cor='steelblue', figsize=(12, 8), max_categorias=None):
    """
    Cria um gráfico de barras HORIZONTAIS com valores formatados nas barras.

    Parâmetros:
    -----------
    dados : DataFrame
        Conjunto de dados
    x_col : str
        Nome da coluna para o eixo y (categorias) - fica na esquerda
    y_col : str
        Nome da coluna para o eixo x (valores) - fica na base
    titulo : str, opcional
        Título do gráfico
    xlabel : str, opcional
        Label do eixo x (valores)
    ylabel : str, opcional
        Label do eixo y (categorias)
    cor : str, opcional
        Cor das barras (padrão: 'steelblue')
    figsize : tuple, opcional
        Tamanho da figura (padrão: (12, 8))
    max_categorias : int, opcional
        Número máximo de categorias a mostrar (útil para muitos dados)

    Retorna:
    --------
    fig, ax : objetos de figura e eixo do matplotlib
    dados_agrupados : Series com os dados agrupados
    """

    # Criar a figura
    fig, ax = plt.subplots(figsize=figsize)

    # Agrupar e ordenar os dados
    dados_agrupados = (
        dados.groupby(x_col)[y_col]
        .sum()
        .sort_values(ascending=True)  # Ordenar ascendente para barras horizontais
    )

    # Limitar número de categorias se especificado
    if max_categorias and len(dados_agrupados) > max_categorias:
        dados_agrupados = dados_agrupados.tail(max_categorias)

    # Criar o gráfico de barras HORIZONTAIS
    posicoes = range(len(dados_agrupados))
    barras = ax.barh(
        posicoes,
        dados_agrupados.values,
        color=cor,
        edgecolor='black',
        linewidth=0.5,
        height=0.7  # Altura das barras
    )

    # Função para formatar os valores
    def formatar_valor(valor):
        """Formata valores para exibir com 'M' para milhões."""
        if abs(valor) >= 1_000_000_000:
            return f'R$ {valor/1_000_000_000:.1f}B'
        elif abs(valor) >= 1_000_000:
            return f'R$ {valor/1_000_000:.0f}M'
        elif abs(valor) >= 1_000:
            return f'R$ {valor/1_000:.0f}K'
        else:
            return f'R$ {valor:.0f}'

    # Adicionar valores no final de cada barra
    for i, (barra, valor) in enumerate(zip(barras, dados_agrupados.values)):
        valor_formatado = formatar_valor(valor)

        # Calcular posição do texto
        x_pos = barra.get_width()

        # Posicionar o texto dentro ou fora da barra dependendo do espaço
        if x_pos < max(dados_agrupados.values) * 0.4:
            # Se a barra for curta, colocar texto fora
            text_x = x_pos + (max(dados_agrupados.values) * 0.01)
            ha = 'left'
            color = 'black'
        else:
            # Se a barra for longa, colocar texto dentro
            text_x = x_pos * 0.95
            ha = 'right'
            color = 'white'

        ax.text(
            text_x,
            barra.get_y() + barra.get_height() / 2,
            valor_formatado,
            ha=ha,
            va='center',
            fontsize=10,
            fontweight='bold',
            color=color
        )

    # Configurar labels do eixo y (categorias)
    ax.set_yticks(posicoes)
    ax.set_yticklabels(
        dados_agrupados.index,
        fontsize=11,
        fontweight='medium'
    )

    # Configurar título e labels
    ax.set_title(titulo, fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel(xlabel, fontsize=12, labelpad=10)
    ax.set_ylabel(ylabel, fontsize=12, labelpad=10)

    # Formatar eixo x para mostrar valores em milhões
    if dados_agrupados.values.max() >= 1_000_000:
        # Criar formatação personalizada para o eixo x
        ax.xaxis.set_major_formatter(
            ticker.FuncFormatter(lambda x, p: f'R$ {x/1_000_000:.0f}M')
        )
    elif dados_agrupados.values.max() >= 1_000:
        ax.xaxis.set_major_formatter(
            ticker.FuncFormatter(lambda x, p: f'R$ {x/1_000:.0f}K')
        )
    else:
        ax.xaxis.set_major_formatter(
            ticker.FuncFormatter(lambda x, p: f'R$ {x:,.0f}')
        )

    # Remover bordas desnecessárias
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Adicionar grid no eixo x para melhor leitura
    ax.grid(axis='x', alpha=0.3, linestyle='--')

    # Adicionar linha vertical no zero
    ax.axvline(x=0, color='gray', linewidth=0.5, alpha=0.5)

    # Ajustar layout para garantir que labels não sejam cortados
    plt.tight_layout()

    return fig, ax, dados_agrupados


# Versão simplificada para uso rápido
def grafico_barras_h_simples(dados, x_col, y_col, titulo='', cor='skyblue', figsize=(10, 6)):
    """
    Versão simplificada para gráficos de barras horizontais.
    """
    dados_agrupados = (
        dados.groupby(x_col)[y_col]
        .sum()
        .sort_values(ascending=True)
    )

    fig, ax = plt.subplots(figsize=figsize)

    # Criar barras horizontais
    barras = ax.barh(
        range(len(dados_agrupados)),
        dados_agrupados.values,
        color=cor,
        height=0.6
    )

    # Adicionar valores formatados
    for barra in barras:
        valor = barra.get_width()

        # Formatar valor
        if valor >= 1_000_000:
            texto = f'R$ {valor/1_000_000:.0f}M'
        elif valor >= 1_000:
            texto = f'R$ {valor/1_000:.0f}K'
        else:
            texto = f'R$ {valor:.0f}'

        # Posicionar texto
        ax.text(
            barra.get_width() * 1.01,
            barra.get_y() + barra.get_height()/2,
            texto,
            ha='left',
            va='center',
            fontsize=9
        )

    # Configurar eixos
    ax.set_yticks(range(len(dados_agrupados)))
    ax.set_yticklabels(dados_agrupados.index)

    # Configurar título
    if titulo:
        ax.set_title(titulo, fontsize=14, pad=15)

    # Grid sutil
    ax.grid(axis='x', alpha=0.2)

    plt.tight_layout()
    return ax

###############################################################################################


def analisar_bens_minerais(df, 
                          col_bens='Bens_minerais',
                          col_quantidade='QuantidadeComercializada', 
                          col_valor='ValorRecolhido',
                          col_municipio='Município',
                          col_unidade='UnidadeDeMedida',
                          titulo_principal='BENS MINERAIS',
                          ano='2025',
                          cor_quantidade='viridis',
                          cor_valor='plasma',
                          cor_rentabilidade='cool',
                          n_top=15,
                          exportar_csv=True,
                          nome_arquivo='analise_bens_minerais.csv'):
    """
    Analisa e visualiza dados de bens minerais.
    
    Parâmetros:
    -----------
    df : pandas.DataFrame
        DataFrame com os dados brutos
    col_bens : str
        Nome da coluna com os bens minerais
    col_quantidade : str
        Nome da coluna com a quantidade comercializada
    col_valor : str
        Nome da coluna com o valor recolhido
    col_municipio : str
        Nome da coluna com o município
    col_unidade : str
        Nome da coluna com a unidade de medida
    titulo_principal : str
        Título principal para os gráficos
    ano : str
        Ano para exibição nos títulos
    cor_quantidade : str
        Colormap para gráfico de quantidade
    cor_valor : str
        Colormap para gráfico de valor
    cor_rentabilidade : str
        Colormap para gráfico de rentabilidade
    n_top : int
        Número de itens para os top N
    exportar_csv : bool
        Se True, exporta os dados para CSV
    nome_arquivo : str
        Nome do arquivo para exportação
        
    Retorna:
    --------
    dict: Dicionário com os DataFrames de análise
    """
    
    # ============================================================================
    # 1. PRÉ-PROCESSAMENTO DOS DADOS
    # ============================================================================
    dados = df.copy()
    
    # Converter colunas numéricas
    def converter_numerico(coluna):
        if coluna in dados.columns:
            dados[coluna] = (dados[coluna]
                             .astype(str)
                             .str.replace('.', '', regex=False)
                             .str.replace(',', '.', regex=False)
                             .astype(float))
    
    converter_numerico(col_quantidade)
    converter_numerico(col_valor)
    
    # ============================================================================
    # 2. AGRUPAMENTO DOS DADOS
    # ============================================================================
    bens_agrupado = dados.groupby(col_bens).agg({
        col_quantidade: 'sum',
        col_valor: 'sum',
        col_municipio: 'nunique',  # Número de municípios distintos
        col_unidade: lambda x: x.mode()[0] if len(x.mode()) > 0 else 'N/A'
    }).reset_index()
    
    # Renomear colunas
    bens_agrupado.columns = ['Bens_Minerais', 'Quantidade_Total', 'Valor_Total', 
                             'Num_Municipios', 'Unidade_Comum']
    
    # Calcular valor médio por unidade (rentabilidade)
    bens_agrupado['Valor_por_Unidade'] = bens_agrupado['Valor_Total'] / bens_agrupado['Quantidade_Total']
    bens_agrupado['Valor_por_Unidade'] = bens_agrupado['Valor_por_Unidade'].replace([np.inf, -np.inf], np.nan)
    
    # ============================================================================
    # 3. FUNÇÕES DE FORMATAÇÃO
    # ============================================================================
    def formatar_valor(valor):
        """Formata valores monetários grandes"""
        if pd.isna(valor):
            return 'R$ 0.00'
        
        valor_abs = abs(valor)
        if valor_abs >= 1e12:
            return f'R$ {valor/1e12:.2f}T'
        elif valor_abs >= 1e9:
            return f'R$ {valor/1e9:.2f}B'
        elif valor_abs >= 1e6:
            return f'R$ {valor/1e6:.2f}M'
        elif valor_abs >= 1e3:
            return f'R$ {valor/1e3:.2f}K'
        else:
            return f'R$ {valor:.2f}'
    
    def formatar_quantidade(valor, unidade=''):
        """Formata quantidades grandes"""
        if pd.isna(valor):
            return '0.00'
        
        valor_abs = abs(valor)
        if valor_abs >= 1e12:
            texto = f'{valor/1e12:.2f}T'
        elif valor_abs >= 1e9:
            texto = f'{valor/1e9:.2f}B'
        elif valor_abs >= 1e6:
            texto = f'{valor/1e6:.2f}M'
        elif valor_abs >= 1e3:
            texto = f'{valor/1e3:.2f}K'
        else:
            texto = f'{valor:.2f}'
        
        if unidade and unidade != 'N/A':
            return f'{texto} {unidade}'
        return texto
    
    # ============================================================================
    # 4. CRIAÇÃO DOS TOP N
    # ============================================================================
    top_quantidade = bens_agrupado.nlargest(n_top, 'Quantidade_Total')
    top_valor = bens_agrupado.nlargest(n_top, 'Valor_Total')
    top_rentabilidade = (bens_agrupado[bens_agrupado['Quantidade_Total'] > 0]
                         .nlargest(n_top, 'Valor_por_Unidade'))
    
    # ============================================================================
    # 5. GRÁFICO 1: TOP POR QUANTIDADE
    # ============================================================================
    print("\n" + "="*100)
    print(f"TOP {n_top} {titulo_principal} POR QUANTIDADE COMERCIALIZADA")
    print("="*100)
    
    plt.figure(figsize=(14, 10))
    bars1 = plt.barh(top_quantidade['Bens_Minerais'], top_quantidade['Quantidade_Total'],
                     color=getattr(plt.cm, cor_quantidade)(np.linspace(0.3, 0.9, n_top)), 
                     height=0.7)
    
    plt.xlabel('Quantidade Comercializada', fontsize=12, fontweight='bold')
    plt.title(f'TOP {n_top} {titulo_principal} POR QUANTIDADE COMERCIALIZADA - {ano}',
              fontsize=16, fontweight='bold', pad=20)
    plt.gca().invert_yaxis()
    plt.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Adicionar valores nas barras
    for bar, valor, unidade in zip(bars1, top_quantidade['Quantidade_Total'], top_quantidade['Unidade_Comum']):
        texto = formatar_quantidade(valor, unidade)
        plt.text(bar.get_width() * 1.01, bar.get_y() + bar.get_height()/2,
                 texto, ha='left', va='center', fontsize=9, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.show()
    
    # Tabela com dados
    print(f"\n{'='*80}")
    print(f"{titulo_principal:<50} {'QUANTIDADE':>20} {'UNIDADE':>10}")
    print('='*80)
    for idx, row in top_quantidade.iterrows():
        print(f"{row['Bens_Minerais']:<50} {formatar_quantidade(row['Quantidade_Total'], row['Unidade_Comum']):>30}")
    
    # ============================================================================
    # 6. GRÁFICO 2: TOP POR VALOR
    # ============================================================================
    print("\n" + "="*100)
    print(f"TOP {n_top} {titulo_principal} POR VALOR RECOLHIDO")
    print("="*100)
    
    plt.figure(figsize=(14, 10))
    bars2 = plt.barh(top_valor['Bens_Minerais'], top_valor['Valor_Total'],
                     color=getattr(plt.cm, cor_valor)(np.linspace(0.3, 0.9, n_top)), 
                     height=0.7)
    
    plt.xlabel('Valor Recolhido (R$)', fontsize=12, fontweight='bold')
    plt.title(f'TOP {n_top} {titulo_principal} POR VALOR RECOLHIDO - {ano}',
              fontsize=16, fontweight='bold', pad=20)
    plt.gca().invert_yaxis()
    plt.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Adicionar valores nas barras
    for bar, valor in zip(bars2, top_valor['Valor_Total']):
        texto = formatar_valor(valor)
        plt.text(bar.get_width() * 1.01, bar.get_y() + bar.get_height()/2,
                 texto, ha='left', va='center', fontsize=9, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.show()
    
    # Tabela com dados
    print(f"\n{'='*80}")
    print(f"{titulo_principal:<50} {'VALOR RECOLHIDO':>25} {'MUNICÍPIOS':>10}")
    print('='*80)
    for idx, row in top_valor.iterrows():
        print(f"{row['Bens_Minerais']:<50} {formatar_valor(row['Valor_Total']):>25} {row['Num_Municipios']:>10}")
    
    # ============================================================================
    # 7. GRÁFICO 3: TOP POR RENTABILIDADE
    # ============================================================================
    print("\n" + "="*100)
    print(f"TOP {n_top} {titulo_principal} POR RENTABILIDADE")
    print("="*100)
    
    plt.figure(figsize=(14, 10))
    bars3 = plt.barh(top_rentabilidade['Bens_Minerais'], top_rentabilidade['Valor_por_Unidade'],
                     color=getattr(plt.cm, cor_rentabilidade)(np.linspace(0.3, 0.9, n_top)), 
                     height=0.7)
    
    plt.xlabel('Valor por Unidade (R$)', fontsize=12, fontweight='bold')
    plt.title(f'TOP {n_top} {titulo_principal} POR RENTABILIDADE - {ano}',
              fontsize=16, fontweight='bold', pad=20)
    plt.gca().invert_yaxis()
    plt.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Adicionar valores nas barras
    for bar, valor, unidade in zip(bars3, top_rentabilidade['Valor_por_Unidade'], top_rentabilidade['Unidade_Comum']):
        texto = f'R$ {valor:,.2f}/{unidade}'
        plt.text(bar.get_width() * 1.01, bar.get_y() + bar.get_height()/2,
                 texto, ha='left', va='center', fontsize=9, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.show()
    
    # Tabela com dados
    print(f"\n{'='*80}")
    print(f"{titulo_principal:<50} {'R$/UNIDADE':>20} {'UNIDADE':>10}")
    print('='*80)
    for idx, row in top_rentabilidade.iterrows():
        print(f"{row['Bens_Minerais']:<50} R$ {row['Valor_por_Unidade']:>15,.2f}/{row['Unidade_Comum']:>10}")
    
    # ============================================================================
    # 8. ANÁLISE COMPARATIVA
    # ============================================================================
    print("\n" + "="*100)
    print(f"ANÁLISE COMPARATIVA: {titulo_principal} DESTAQUES")
    print("="*100)
    
    bens_top_quantidade = set(top_quantidade['Bens_Minerais'])
    bens_top_valor = set(top_valor['Bens_Minerais'])
    bens_top_rentabilidade = set(top_rentabilidade['Bens_Minerais'])
    
    bens_todas_listas = bens_top_quantidade & bens_top_valor & bens_top_rentabilidade
    bens_duas_listas = ((bens_top_quantidade & bens_top_valor) | 
                        (bens_top_quantidade & bens_top_rentabilidade) | 
                        (bens_top_valor & bens_top_rentabilidade))
    
    print(f"\n{titulo_principal} que estão nas 3 listas TOP {n_top}:")
    print("-" * 60)
    for bem in sorted(bens_todas_listas):
        print(f"  • {bem}")
    
    print(f"\n{titulo_principal} que estão em 2 listas TOP {n_top}:")
    print("-" * 60)
    for bem in sorted(bens_duas_listas - bens_todas_listas):
        print(f"  • {bem}")
    
    # ============================================================================
    # 9. GRÁFICO DE DISPERSÃO
    # ============================================================================
    print("\n" + "="*100)
    print(f"GRÁFICO DE DISPERSÃO: QUANTIDADE VS VALOR")
    print("="*100)
    
    plt.figure(figsize=(14, 10))
    top30_combinado = bens_agrupado.nlargest(30, 'Valor_Total')
    
    scatter = plt.scatter(top30_combinado['Quantidade_Total'],
                          top30_combinado['Valor_Total'],
                          s=top30_combinado['Num_Municipios']*50,
                          c=top30_combinado['Valor_por_Unidade'],
                          cmap='viridis',
                          alpha=0.7,
                          edgecolors='black',
                          linewidth=0.5)
    
    plt.xlabel('Quantidade Comercializada (escala log)', fontsize=12, fontweight='bold')
    plt.ylabel('Valor Recolhido (R$) - escala log', fontsize=12, fontweight='bold')
    plt.title(f'RELACIONAMENTO: QUANTIDADE VS VALOR - {ano}',
              fontsize=16, fontweight='bold', pad=20)
    
    plt.xscale('log')
    plt.yscale('log')
    
    cbar = plt.colorbar(scatter)
    cbar.set_label('Valor por Unidade (R$)', fontsize=12, fontweight='bold')
    
    for idx, row in top30_combinado.nlargest(10, 'Valor_Total').iterrows():
        nome = row['Bens_Minerais'][:20] + '...' if len(row['Bens_Minerais']) > 20 else row['Bens_Minerais']
        plt.annotate(nome, (row['Quantidade_Total'], row['Valor_Total']),
                     fontsize=8, alpha=0.8,
                     bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.7))
    
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.show()
    
    # ============================================================================
    # 10. RESUMO ESTATÍSTICO
    # ============================================================================
    print("\n" + "="*100)
    print(f"RESUMO ESTATÍSTICO - {ano}")
    print("="*100)
    
    print(f"\nTotal de tipos diferentes: {len(bens_agrupado)}")
    print(f"Com dados comerciais: {len(bens_agrupado[bens_agrupado['Quantidade_Total'] > 0])}")
    
    print(f"\nESTATÍSTICAS GERAIS:")
    print("-" * 60)
    print(f"Quantidade total: {formatar_quantidade(bens_agrupado['Quantidade_Total'].sum())}")
    print(f"Valor total: {formatar_valor(bens_agrupado['Valor_Total'].sum())}")
    print(f"Valor médio por unidade: R$ {bens_agrupado['Valor_por_Unidade'].mean():,.2f}")
    print(f"Média de municípios: {bens_agrupado['Num_Municipios'].mean():.1f}")
    
    # ============================================================================
    # 11. EXPORTAÇÃO DOS DADOS
    # ============================================================================
    if exportar_csv:
        bens_agrupado.to_csv(nome_arquivo, index=False, encoding='utf-8-sig')
        print(f"\nDados exportados para: {nome_arquivo}")
    
    print("="*100)
    
    # ============================================================================
    # 12. RETORNO DOS DADOS
    # ============================================================================
    return {
        'dados_agrupados': bens_agrupado,
        'top_quantidade': top_quantidade,
        'top_valor': top_valor,
        'top_rentabilidade': top_rentabilidade,
        'analise_comparativa': {
            'tres_listas': list(bens_todas_listas),
            'duas_listas': list(bens_duas_listas - bens_todas_listas)
        }
    }


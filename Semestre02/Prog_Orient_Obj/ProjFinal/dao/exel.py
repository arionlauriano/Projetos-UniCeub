import pandas as pd
import io
from datetime import datetime
import sys
from pathlib import Path

# Adicionar o diretório pai ao path para importar dao
sys.path.insert(0, str(Path(__file__).parent))

from dao.comp_dao import CompraDao

# Criar pasta para relatórios se não existir
PASTA_RELATORIOS = Path(__file__).parent / 'relatorios'
PASTA_RELATORIOS.mkdir(exist_ok=True)

def gerar_relatorio():
    """Gera relatório Excel a partir das compras no banco de dados"""

    # 1. Buscar os dados usando o DAO
    comp_dao = CompraDao()
    lista_compras = comp_dao.select_comp_az()
    rt = ""

    if not lista_compras:
        rt = "❌ Nenhuma compra encontrada no banco de dados!"
        print(rt)
        return (rt, "")

    print(f"✓ {len(lista_compras)} compras encontradas")

    # 2. Preparar a lista de dicionários para o relatório
    dados_excel = []

    for comp in lista_compras:
        try:
            item = {
                'Data': comp.data_comp,
                'Nota Fiscal': comp.cod_nf_comp,
                'Total (R$)': float(comp.total_comp) if comp.total_comp else 0.0,
                'Cliente': comp.cli.nome_cli,
                'UF': comp.cli.uf.sgl_uf,
                'Montadora': comp.vers.mod.mont.nome_mont,
                'Modelo': comp.vers.mod.nome_mod,
                'Versão': comp.vers.nome_vers,
            }
            dados_excel.append(item)
            
        except AttributeError as e:
            print(f"⚠ Aviso: Objeto incompleto na compra {comp.id_comp}. Erro: {e}")
            item = {
                'Data': comp.data_comp,
                'Nota Fiscal': comp.cod_nf_comp,
                'Total (R$)': float(comp.total_comp) if comp.total_comp else 0.0,
                'Cliente': f"ID {comp.cod_cli} (Erro ao carregar)",
                'UF': 'N/A',
                'Montadora': 'N/A',
                'Modelo': 'N/A',
                'Versão': f"ID {comp.cod_vers} (Erro ao carregar)",
            }
            dados_excel.append(item)

    # 3. Criar DataFrame
    df = pd.DataFrame(dados_excel)

    # Formatar datas
    if 'Data' in df and not df['Data'].isnull().all():
        df['Data'] = pd.to_datetime(df['Data']).dt.strftime('%d/%m/%Y')

    # 4. Gerar arquivo Excel
    filename = f"relatorio_vendas_{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.xlsx"
    filepath = PASTA_RELATORIOS / filename

    try:
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Relatorio_Vendas_Auto')
            
            # Ajustar largura das colunas
            worksheet = writer.sheets['Relatorio_Vendas_Auto']
            for i, col in enumerate(df.columns):
                max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
                worksheet.column_dimensions[chr(65 + i)].width = max_len
        

        print(f"✓ Relatório criado com sucesso!")
        print(f"✓ Arquivo salvo em: {filepath}")
        return (rt, filepath)
        
    except Exception as e:
        rt = f"❌ Erro ao salvar arquivo: {e}"
        print(rt)
        return (rt, "")

if __name__ == '__main__':
    print("Gerando relatório de compras...")
    gerar_relatorio()


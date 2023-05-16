import beautifultable
import locale
locale.setlocale(locale.LC_MONETARY, '')
table = beautifultable.BeautifulTable()
table.set_style(beautifultable.BeautifulTable().STYLE_GRID)

class Barbearia():
    
    def __init__(self, nome: str) -> None:
        self._carteira = 1000
        self._informados = []
        self.nome_barbeiro = nome.title()
        
        self.valor_corte_promossional = 20
        self.valor_corte = 25
        
        self.produtos = ProdutoParaVenda(self)
        
              
    @property    
    def carteira(self) -> float:
        return self._carteira
    
    
    @carteira.setter
    def carteira(self, valor: int):
        self._carteira = valor
        print(f'Carteira: {Barbearia._formatar_moeda(self._carteira)}')
    
        
    @property
    def informados(self) -> list:
        return self._informados
    
    
    @informados.setter
    def informados(self, nome: str):
        if nome in self._informados:
            pass
        else:
            self._informados.append(nome)
            
        print(f'Clientes Avisados: {" - ".join(self._informados)}')
    
        
    @staticmethod
    def _formatar_moeda(valor) -> str:
        return locale.currency(valor, grouping=True)
    
        
    def _continuar_ou_interromper(self):
        pergunta_interrupcao = input('Você deseja encerrar os cortes? (s/n)')
        if pergunta_interrupcao.lower() in ['sim','s']:
            pass
        
        else:
            self.corte()
        
        
    def corte(self):
        nome_cliente = input(f'{self.nome_barbeiro}, qual o nome do cliente?').title()
        
        if nome_cliente in self.informados:
            self.carteira += self.valor_corte
            self.informados = nome_cliente          
            
        else:
            self.carteira += self.valor_corte_promossional
            self.informados = nome_cliente
            
        self._continuar_ou_interromper()
            


class ProdutoParaVenda(Barbearia):
    
    def __init__(self, objeto) -> None:
        self.barbearia_objeto = objeto
        self.produtos_itens = ...
    
    @staticmethod
    def __encontrar_chave_por_valor(dicionario, valor) -> str:
        for chave, valor_atual in dicionario.items():
            if valor_atual == valor:
                return chave
            
        return None    
    
    def apresentar_produtos_venda(self):
        table.clear()
        self.produtos_itens = {
            'Gel' : 7,
            'Creme de Barbear' : 12,
            'Camisa' : 90,
            'Bermuda' : 50,
            'Navalhete' : 20
        }
        
        table.columns.header = ['Nome','Preço']
        for produto, valor in self.produtos_itens.items():
            table.rows.append([produto, valor])
            
        print(table)

        
    def compra(self):
        table.clear()
        nomes_produtos = [nome for nome in self.produtos_itens.keys()]
        
        for i, each in enumerate(nomes_produtos):
            print(f'{i + 1} - {each}')    
            
        l = int(input('Qual produto deseja comprar? Escolha pelo NÚMERO! '))

        
        valor_compra = self.produtos_itens[nomes_produtos[l - 1]]
        nome_compra = ProdutoParaVenda.__encontrar_chave_por_valor(self.produtos_itens, valor_compra)

        
        table.columns.header = ['Produto','Preço']
        table.rows.append([nome_compra, Barbearia._formatar_moeda(valor_compra)])
        print(table)

        
        self.barbearia_objeto.carteira += valor_compra
        
    
    
    
if __name__ == '__main__':
    barbeiro = Barbearia('kevin')
    barbeiro.corte()
    barbeiro.produtos.apresentar_produtos_venda()
    barbeiro.produtos.compra()
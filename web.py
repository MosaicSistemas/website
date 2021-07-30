from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def init():
    html ='''
    <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
    
    <title>Pagina Inicial - ArcBridge</title>
</head>
<body>
    <header>
        
        <h1>
            ArcBridge
        </h1>
        
    </header>
    
    <section>
        <h2>
            O que é?
        </h2>

        <div class='conteudo' id='1'>
        
            <div class='imagem'>
                <picture>
                    <source media="(max-width: 500px)" srcset="img/main-p.jpeg">
                    <source media="(max-width: 700px)" srcset="img/main-m.jpeg">
                    <img src="img/main-g.jpeg" alt="imagen media">
                </picture>
            </div>

            <div class='texto'></div>
                <p>
                    ArcBridge é um aplicativo de sistema de caixa para pequenos negócios que possibilita aos usuários mais organização, com anotações das vendas e a produção de um pequeno relatório com informações importantes, tais como: ranking das categorias, produtos mais vendidos, número de produtos vendidos e faturamento total. Ter essas informações de forma facilitada auxilia o usuário a tomar decisões como investimentos e estoque.
                    <br>
                    O aplicativo também pode ser usado em vários tipos de negócios devido sua capacidade de cadastro não só de produtos como também por categorias e formas de pagamento. Desta forma, o ArcBridge pode ser aplicado em diversos negócios de lanchonetes até mesmo em pequenas lojas. <br>
                    O aplicativo é compatível até mesmo com sistemas mais antigos sem a necessidade de equipamentos mais modernos. Tem versão disponível somente para Windows. As versões para Linux e Mac ainda serão lançadas. 
                </p>
            </div>
        </div>

        <div class='conteudo'>

            <div class='imagem' id='2'>
                <picture>
                    <source media="(max-width: 500px)" srcset="img/extra-p.jpeg">
                    <source media="(max-width: 700px)" srcset="img/extra-m.jpeg">
                    <img src="img/extra-g.jpeg" alt="janela pgto/categoria ArcBridge">
                </picture>
            </div>

            <div class='texto'></div>
                <p>
                    
                </p>
            </div>
        </div>
        
        <div class='link'> 
           <ul>
                <li><a href="download.html">Area de Downloads</a></li>

           </ul>
        </div>
         
    </section>

    <footer>
        
        <h3>
        Criado por: Igor Crissaff
        </h3>
    
    </footer>
    
</body>
</html>
    '''

app.run()

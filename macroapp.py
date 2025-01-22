import streamlit as st


def mostrar_pergunta(pergunta, resposta_correta, justificativa):
    st.markdown(f"**Pergunta:** {pergunta}")
    resposta_usuario = st.radio(
        "Resposta:",
        options=["V", "F"],
        key=pergunta,
        index=None,  # Nenhuma opção selecionada por padrão
    )
    if resposta_usuario is not None:
        if resposta_usuario == resposta_correta:
            st.success("Correto! ✅")
        else:
            st.error(f"Incorreto! ❌ A resposta correta é: {resposta_correta}")
        st.write(f"**Justificativa:** {justificativa}")
    st.write("---")  # Linha divisória entre as perguntas


def main():
    # Configuração da página
    st.set_page_config(page_title="Quiz de Macro III - por Bernardo Louzada", page_icon="📚", layout="centered")

    # Barra lateral para instruções
    with st.sidebar:
        st.title("Instruções")
        st.write("""
        Bem-vindo ao Quiz de revisão pra P1 de Macro III!

        - Responda às perguntas marcando **Verdadeiro (V)** ou **Falso (F)**.
        - Após responder, você verá se acertou e a justificativa da resposta.
        - As perguntas estão organizadas por tópicos.
        - Boa sorte! 🤓
        """)

    # Título principal
    st.title("Quiz de revisão pra P1 de Macro III")
    st.write("Programei isso pra brincar e ajudar geral a revisar. Tmj galera. 🤍📖 - @Bernardo Louzada")

    # Perguntas organizadas por tópicos
    st.header("1. Princípio da Demanda Efetiva")
    perguntas_demanda_efetiva = [
        {
            "pergunta": "No ponto de demanda efetiva, o lucro real é maximizado.",
            "resposta_correta": "F",
            "justificativa": "Keynes argumenta que o ponto de demanda efetiva é onde as expectativas de lucro são maximizadas, mas isso não significa que o lucro real seja maximizado, pois as expectativas podem não se materializar devido à incerteza."
        },
        {
            "pergunta": "As expectativas de longo prazo estão embutidas na função de demanda agregada.",
            "resposta_correta": "V",
            "justificativa": "A demanda agregada keynesiana incorpora expectativas de longo prazo dos empresários, que influenciam decisões de investimento."
        },
        {
            "pergunta": "O ponto de demanda efetiva se modifica quando as expectativas de longo prazo se modificam.",
            "resposta_correta": "V",
            "justificativa": "Mudanças nas expectativas de longo prazo alteram o investimento e, consequentemente, o ponto de demanda efetiva."
        }
    ]
    for q in perguntas_demanda_efetiva:
        mostrar_pergunta(q["pergunta"], q["resposta_correta"], q["justificativa"])

    st.header("2. Determinação da Taxa de Juros")
    perguntas_taxa_juros = [
        {
            "pergunta": "A taxa de juros de equilíbrio é determinada pela demanda e pela oferta de fundos.",
            "resposta_correta": "F",
            "justificativa": "Essa é a visão neoclássica. Keynes afirma que a taxa de juros é determinada pela preferência pela liquidez (demanda por moeda) e oferta monetária."
        },
        {
            "pergunta": "Quando os agentes esperam um aumento da taxa de juros, a Preferência pela Liquidez diminui.",
            "resposta_correta": "F",
            "justificativa": "Se os agentes esperam aumento da taxa de juros, a demanda por moeda aumenta (eles retêm moeda para comprar títulos no futuro, quando os preços estiverem mais baixos)."
        },
        {
            "pergunta": "Na Teoria Geral, a demanda por moeda é determinada pela taxa de juros.",
            "resposta_correta": "V",
            "justificativa": "Keynes divide a demanda por moeda em três motivos: transação, precaução e especulação. A demanda por especulação é inversamente relacionada à taxa de juros."
        }
    ]
    for q in perguntas_taxa_juros:
        mostrar_pergunta(q["pergunta"], q["resposta_correta"], q["justificativa"])

    st.header("3. Função de Investimento (I)")
    perguntas_investimento_I = [
        {
            "pergunta": "O investimento é realizado quando o preço de oferta é maior que o preço de demanda.",
            "resposta_correta": "F",
            "justificativa": "O investimento ocorre quando o preço de demanda (valor presente dos retornos esperados) é maior que o preço de oferta (custo do capital)."
        },
        {
            "pergunta": "O preço de oferta de um determinado bem de capital corresponde ao preço pelo qual esse bem foi comprado.",
            "resposta_correta": "F",
            "justificativa": "O preço de oferta é o custo de reposição do bem no momento do investimento, não o preço histórico."
        },
        {
            "pergunta": "Na Teoria Geral, o investimento depende diretamente de uma poupança prévia.",
            "resposta_correta": "F",
            "justificativa": "Keynes rejeita essa ideia neoclássica. O investimento gera renda, que por sua vez gera poupança."
        }
    ]
    for q in perguntas_investimento_I:
        mostrar_pergunta(q["pergunta"], q["resposta_correta"], q["justificativa"])

    st.header("4. Função de Investimento (II)")
    perguntas_investimento_II = [
        {
            "pergunta": "No curto prazo, a eficiência do capital diminui porque o preço de oferta do capital sobe.",
            "resposta_correta": "V",
            "justificativa": "No curto prazo, o aumento da demanda por bens de capital eleva seu preço de oferta, reduzindo a EMC."
        },
        {
            "pergunta": "O investimento global depende da diferença entre a eficiência do capital, em geral, e a taxa de juros.",
            "resposta_correta": "V",
            "justificativa": "Investimento = f(EMC – taxa de juros). Quanto maior a diferença, maior o investimento."
        },
        {
            "pergunta": "A eficiência marginal do capital de uma determinada qualidade é constante no tempo.",
            "resposta_correta": "F",
            "justificativa": "A EMC varia com as expectativas de retorno e as condições de mercado."
        }
    ]
    for q in perguntas_investimento_II:
        mostrar_pergunta(q["pergunta"], q["resposta_correta"], q["justificativa"])

    st.header("5. Multiplicador de Investimento")
    perguntas_multiplicador = [
        {
            "pergunta": "Quanto maior a propensão média a poupar, maior a variação do produto e do emprego.",
            "resposta_correta": "F",
            "justificativa": "O multiplicador é 1/s. Quanto maior a propensão a poupar (s), menor o multiplicador."
        },
        {
            "pergunta": "À medida que uma coletividade se torna mais 'rica', é cada vez mais difícil alcançar novos aumentos do emprego.",
            "resposta_correta": "V",
            "justificativa": "Sociedades ricas têm maior propensão a poupar, reduzindo o multiplicador (Paradoxo da Abundância)."
        },
        {
            "pergunta": "Uma sociedade 'pobre' é sujeita a flutuações mais importantes que uma sociedade 'rica'.",
            "resposta_correta": "V",
            "justificativa": "Em sociedades pobres, a propensão a consumir é maior, amplificando os efeitos do investimento (multiplicador maior)."
        }
    ]
    for q in perguntas_multiplicador:
        mostrar_pergunta(q["pergunta"], q["resposta_correta"], q["justificativa"])

    st.header("6. Ajustamento Macroeconômico Neoclássico")
    perguntas_ajustamento_neoclassico = [
        {
            "pergunta": "A macroeconomia neoclássica se caracteriza pela determinação exógena da taxa de juros.",
            "resposta_correta": "F",
            "justificativa": "Na visão neoclássica, a taxa de juros é determinada endogenamente pelo mercado de fundos de empréstimos."
        },
        {
            "pergunta": "Na macroeconomia neoclássica, oferta e demanda de trabalho são determinadas independentemente.",
            "resposta_correta": "V",
            "justificativa": "Oferta de trabalho é função do salário real, e demanda é função da produtividade marginal."
        },
        {
            "pergunta": "O ajustamento rumo ao equilíbrio é realizado ex-post, a partir de uma variação da renda.",
            "resposta_correta": "F",
            "justificativa": "Neoclássicos ajustam via variação da taxa de juros (ex-ante), não da renda."
        }
    ]
    for q in perguntas_ajustamento_neoclassico:
        mostrar_pergunta(q["pergunta"], q["resposta_correta"], q["justificativa"])

    st.header("7. Macroeconomia Keynesiana")
    perguntas_keynesiana = [
        {
            "pergunta": "No modelo keynesiano, o equilíbrio é realizado primeiramente no mercado do trabalho.",
            "resposta_correta": "F",
            "justificativa": "Keynes rejeita a hierarquia neoclássica. O equilíbrio é determinado pela demanda efetiva, não pelo mercado de trabalho."
        },
        {
            "pergunta": "Keynes adota o postulado clássico sobre a oferta de trabalho.",
            "resposta_correta": "F",
            "justificativa": "Keynes critica o segundo postulado clássico, argumentando que salários são negociados em termos nominais, não reais."
        },
        {
            "pergunta": "Para Keynes, demanda global = oferta global apenas para um valor específico do produto.",
            "resposta_correta": "V",
            "justificativa": "Diferente dos neoclássicos, que afirmam igualdade para qualquer nível de produto (Lei de Say)."
        }
    ]
    for q in perguntas_keynesiana:
        mostrar_pergunta(q["pergunta"], q["resposta_correta"], q["justificativa"])

    # Mensagem final
    st.markdown("---")
    st.success("🎉 Fim do jogo! Obrigado por participar!")


if __name__ == "__main__":
    main()
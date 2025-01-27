import streamlit as st


# ====== FUNÇÕES AUXILIARES ======
def mostrar_pergunta(pergunta, resposta_correta, justificativa):
    with st.container(border=True):
        st.markdown(f"**Pergunta:** {pergunta}")
        resposta_usuario = st.radio(
            "Resposta:",
            options=["V", "F"],
            key=pergunta,
            index=None,
        )
        if resposta_usuario is not None:
            # Atualizar contagem de respostas
            if resposta_usuario == resposta_correta:
                st.session_state.acertos += 1
                st.success("Correto! ✅")
            else:
                st.session_state.erros += 1
                st.error(f"Incorreto! ❌ Resposta correta: **{resposta_correta}**")
            st.markdown(f"*Justificativa:* {justificativa}")
        st.write("---")


def calcular_progresso():
    total_perguntas = sum(len(topico) for topico in st.session_state.perguntas.values())
    return st.session_state.acertos + st.session_state.erros, total_perguntas


# ====== CONFIGURAÇÃO INICIAL ======
def main():
    # Inicializar estados da sessão
    if "acertos" not in st.session_state:
        st.session_state.acertos = 0
    if "erros" not in st.session_state:
        st.session_state.erros = 0
    if "modo_escuro" not in st.session_state:
        st.session_state.modo_escuro = False

    # ====== CONFIGURAÇÃO DA PÁGINA ======
    st.set_page_config(
        page_title="Quiz de Macro III - por Bernardo Louzada",
        page_icon="📚",
        layout="centered"
    )

    # CSS para modo escuro/claro
    st.markdown(f"""
        <style>
            .main {{
                background-color: {'#1E1E1E' if st.session_state.modo_escuro else 'white'};
                color: {'white' if st.session_state.modo_escuro else 'black'};
            }}
        </style>
    """, unsafe_allow_html=True)

    # ====== BARRA LATERAL ======
    with st.sidebar:
        st.title("⚙️ Configurações")

        # Tema
        st.session_state.modo_escuro = st.toggle("Modo Escuro 🌙")

        # Seletor de Tópicos
        st.subheader("📚 Tópicos")
        tópicos = {
            "Demanda Efetiva": "1",
            "Taxa de Juros": "2",
            "Investimento I": "3",
            "Investimento II": "4",
            "Multiplicador": "5",
            "Neoclássicos": "6",
            "Keynesiana": "7",
            "Equilíbrio": "8",
            "Keynes vs Neo": "9",
            "Demanda TG": "10",
            "Investimento TG": "11",
            "Multiplicador Keynes": "12"
        }
        tópicos_selecionados = [k for k, v in tópicos.items() if st.checkbox(k, key=v, value=True)]

        # Botão de Reinício
        if st.button("🔄 Reiniciar Quiz"):
            st.session_state.acertos = 0
            st.session_state.erros = 0
            st.rerun()

    # ====== CONTEÚDO PRINCIPAL ======
    st.title("Quiz de revisão pra P1 de Macro III 📖")
    st.caption("Programei isso pra brincar e ajudar geral a revisar. Tmj galera. 🤍 - @Bernardo Louzada")

    # Barra de Progresso
    respondidas, total = calcular_progresso()
    st.progress(respondidas / total if total > 0 else 0)
    st.subheader(f"🎯 Acertos: {st.session_state.acertos} | ❌ Erros: {st.session_state.erros}")

    # ====== PERGUNTAS (ESTRUTURA SIMPLIFICADA) ======
    # [As listas de perguntas originais devem ser mantidas aqui...]
    # Adicione todas as perguntas conforme o código anterior, organizando em dicionários por tópico.
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


    st.header("8. Equilíbrio Macroeconômico")
    perguntas_equilibrio = [
        {
            "pergunta": "A resolução proposta por Keynes, no que diz respeito ao sistema de equações simultâneas que representa as condições do equilíbrio macroeconômico, consiste em tornar exógena a renda.",
            "resposta_correta": "F",
            "justificativa": "Keynes torna exógenas as expectativas de longo prazo e a demanda efetiva, não a renda. A renda é determinada endogenamente pelo modelo."
        },
        {
            "pergunta": "A partir da resolução proposta por Keynes, a determinação do produto de equilíbrio depende, em parte, da moeda.",
            "resposta_correta": "V",
            "justificativa": "A taxa de juros (influenciada pela oferta monetária) afeta o investimento, que é componente da demanda efetiva."
        },
        {
            "pergunta": "Para a economia neoclássica, o equilíbrio macroeconômico (demanda agregada igual à oferta agregada) é realizado para qualquer nível do produto.",
            "resposta_correta": "V",
            "justificativa": "Neoclássicos seguem a Lei de Say: a oferta cria sua própria demanda, válida para qualquer nível de produção."
        }
    ]
    for q in perguntas_equilibrio:
        mostrar_pergunta(q["pergunta"], q["resposta_correta"], q["justificativa"])

    st.header("9. Keynes vs Neoclássicos")
    perguntas_keynes_neoclassicos = [
        {
            "pergunta": "A análise de Keynes, na Teoria Geral, é totalmente compatível com a verificação da teoria dos fundos de empréstimos (TFE).",
            "resposta_correta": "F",
            "justificativa": "Keynes rejeita a TFE, pois sua teoria da taxa de juros baseia-se na preferência pela liquidez, não na poupança prévia."
        },
        {
            "pergunta": "Segundo Keynes, a TFE é compatível com a existência do multiplicador de investimento.",
            "resposta_correta": "F",
            "justificativa": "A TFE supõe poupança como pré-condição do investimento, enquanto o multiplicador keynesiano mostra que o investimento gera poupança."
        },
        {
            "pergunta": "Keynes adota o segundo postulado da economia (neo)clássica, postulado segundo o qual 'A utilidade do salário, quando se emprega determinado volume de trabalho, é igual à desutilidade marginal desse mesmo volume de emprego'.",
            "resposta_correta": "F",
            "justificativa": "Keynes rejeita esse postulado, argumentando que salários são rígidos em termos nominais e não se ajustam automaticamente."
        }
    ]
    for q in perguntas_keynes_neoclassicos:
        mostrar_pergunta(q["pergunta"], q["resposta_correta"], q["justificativa"])

    st.header("10. Demanda Efetiva na Teoria Geral")
    perguntas_demanda_teoria_geral = [
        {
            "pergunta": "O ponto de demanda efetiva corresponde à maximização dos lucros efetivamente auferidos pelos capitalistas.",
            "resposta_correta": "F",
            "justificativa": "Corresponde à maximização das expectativas de lucro, não necessariamente dos lucros realizados (há incerteza)."
        },
        {
            "pergunta": "As expectativas de longo prazo estão embutidas na função de oferta agregada, o que explica sua inclinação.",
            "resposta_correta": "V",
            "justificativa": "A oferta agregada reflete custos e expectativas de retorno de longo prazo dos empresários."
        },
        {
            "pergunta": "Uma modificação das expectativas de longo prazo se traduz obrigatoriamente por uma modificação do ponto de demanda efetiva.",
            "resposta_correta": "V",
            "justificativa": "Expectativas alteram o investimento e a demanda efetiva, deslocando o equilíbrio."
        }
    ]
    for q in perguntas_demanda_teoria_geral:
        mostrar_pergunta(q["pergunta"], q["resposta_correta"], q["justificativa"])

    st.header("11. Função de Investimento na TG")
    perguntas_investimento_tg = [
        {
            "pergunta": "O preço de oferta de um bem de capital representa o valor pelo qual este bem foi comprado pelo capitalista.",
            "resposta_correta": "F",
            "justificativa": "Preço de oferta é o custo de reposição atual, não o preço histórico."
        },
        {
            "pergunta": "O investimento será efetivamente realizado quando o preço de oferta for superior ao preço de demanda.",
            "resposta_correta": "F",
            "justificativa": "O investimento ocorre quando o preço de demanda (retorno esperado) supera o preço de oferta (custo)."
        },
        {
            "pergunta": "No curto prazo, quando o investimento aumenta, a eficiência marginal do capital diminui pelo fato do preço de oferta aumentar.",
            "resposta_correta": "V",
            "justificativa": "Maior demanda por bens de capital eleva seus custos (preço de oferta), reduzindo a EMC."
        }
    ]
    for q in perguntas_investimento_tg:
        mostrar_pergunta(q["pergunta"], q["resposta_correta"], q["justificativa"])

    st.header("12. Multiplicador Keynesiano")
    perguntas_multiplicador_keynes = [
        {
            "pergunta": "O paradoxo da abundância ressalta o fato que quanto mais rica uma sociedade, menor tem que ser o aumento do investimento produtivo para alcançar uma situação de pleno emprego.",
            "resposta_correta": "F",
            "justificativa": "O paradoxo afirma que sociedades ricas têm menor multiplicador, exigindo aumentos maiores no investimento para gerar emprego."
        },
        {
            "pergunta": "O multiplicador keynesiano implica que uma política de redistribuição da renda para camadas mais pobres aumenta o valor deste multiplicador.",
            "resposta_correta": "V",
            "justificativa": "Populações mais pobres têm maior propensão a consumir, elevando o multiplicador (k = 1/s)."
        },
        {
            "pergunta": "Um aumento da propensão marginal e média a poupar vem diminuir o valor do multiplicador.",
            "resposta_correta": "V",
            "justificativa": "Multiplicador é inversamente proporcional à propensão a poupar (k = 1/s). Quanto maior 's', menor 'k'."
        }
    ]
    for q in perguntas_multiplicador_keynes:
        mostrar_pergunta(q["pergunta"], q["resposta_correta"], q["justificativa"])

        # Filtrar perguntas pelos tópicos selecionados
        for tópico in tópicos_selecionados:
            st.header(f"{list(tópicos.keys()).index(tópico) + 1}. {tópico}")
            for q in st.session_state.perguntas.get(tópico, []):
                mostrar_pergunta(q["pergunta"], q["resposta_correta"], q["justificativa"])

        # ====== SEÇÃO FINAL ======
        st.markdown("---")
        if respondidas == total and total > 0:
            st.balloons()
            acuracia = (st.session_state.acertos / total) * 100
            st.success(f"🏆 **Quiz Concluído!** Acurácia: **{acuracia:.1f}%**")
            st.metric("Resumo", f"{st.session_state.acertos}/{total} corretas")

    if __name__ == "__main__":
        main()

# ED01 — Tema 4: Alucinações em LLMs (pesquisa com fontes reais)

**Status:** rascunho de pesquisa · **sem dados inventados** · aguardando decisões do aluno  
**PDF do enunciado:** `material/exercicios/ED01.pdf`  
**Questão norteadora (ED):** *Em que medida é apropriado utilizar modelos de linguagem em decisões que exigem alto grau de precisão factual?*

---

## Conceito técnico (obrigatório)

**Alucinação (hallucination)** em LLM: afirmação gerada pelo modelo que **não está alinhada** com o conhecimento estabelecido do mundo **ou** com o contexto/entrada fornecida (definição operacional usada em Ravichander et al., ACL 2025 — HALoGEN).

Tipos úteis (HALoGEN):
- **Tipo A** — possível má recuperação do dado de treino  
- **Tipo B** — conhecimento incorreto no treino / má contextualização  
- **Tipo C** — fabricação (sem base)

No direito, a literatura distingue ainda **fabricações** (casos/citações inexistentes) e **inexatidões** (autoridade real, mas com sentido distorcido) — ver Magesh et al. (2025), citado na ordem disciplinar do 9º Circuito (jun/2026).

---

## Caso concreto recente (últimos 12 meses) — recomendado

### *Malkeet LNU* — sanções no 9º Circuito dos EUA (3 jun 2026)

| Item | Fonte verificável |
|------|-------------------|
| O quê | Advogados Mike Singh Sethi e William Rounds apresentaram memoriais com **casos inexistentes**, citações mal atribuídas e distorção de precedentes; negaram uso de IA; depois admitiram uso não autorizado por redatores e falha de verificação |
| Sanção | **US$ 2.500** cada + **suspensão de 6 meses** de atuar no 9º Circuito + obrigação de IA em petições por **2 anos** |
| Ponto jurídico | A corte **não** sancionou o uso de IA em si; sancionou **assinar e protocolar** conteúdo falso e a falta de candura |
| Opinião oficial | https://cdn.ca9.uscourts.gov/datastore/opinions/2026/06/03/24-4790.pdf |
| Cobertura ABA Journal | https://www.abajournal.com/news/article/attorneys-lack-of-candor-over-ai-errors-leads-to-stricter-sanctions |
| FindLaw | https://caselaw.findlaw.com/court/us-9th-circuit/88589.html |

**Caso de apoio (contexto histórico, 2023 — citar como antecedente, não como “últimos 12 meses”):** *Mata v. Avianca* (S.D.N.Y., 22 jun 2023) — ChatGPT gerou precedentes fictícios; multa conjunta de US$ 5.000. Ordem: https://www.nhd.uscourts.gov/sites/default/files/pdf/Mata-v-Avianca-sanctions-order.PDF

**Caso adicional recente (opcional):** Califórnia (set/2025) — advogado multado em US$ 10.000 por citações fabricadas por IA (The Recorder / Law.com, 15/09/2025).

---

## Dados quantitativos (com ressalva de escopo)

> **Importante:** não existe “a taxa oficial de alucinação da IA”. Cada número vale **para um protocolo, tarefa e conjunto de modelos**. No texto, sempre dizer *em que benchmark*.

| Fonte | O que mede | Número a citar com cuidado |
|-------|------------|----------------------------|
| **Magesh et al., J. Empirical Legal Studies (2025)** | Ferramentas jurídicas com RAG (Lexis+ AI, Westlaw AI, Ask Practical Law AI) | Ainda alucinam **entre ~17% e ~33%** das consultas no estudo pré-registrado; claims de “hallucination-free” são exageradas · https://doi.org/10.1111/jels.12413 · PDF Stanford: https://dho.stanford.edu/wp-content/uploads/Legal_RAG_Hallucinations.pdf |
| **HALoGEN** (ACL 2025) | ~150 mil gerações, 14 modelos, 9 domínios | Mesmo os melhores modelos alucinam; **até ~86%** dos *fatos atômicos* gerados **em certos domínios** (não é média global) · https://aclanthology.org/2025.acl-long.71/ |
| **Vectara Hallucination Leaderboard** (atualizado 2026; sumarização grounded) | Taxa de alucinação ao resumir documentos | Ex.: modelos no topo ~**1,8%–~11%+** conforme modelo; GPT-4.1 (~abr/2025) aparece com **5,6%** na tabela pública · https://github.com/vectara/hallucination-leaderboard |
| **FaithBench** (NAACL 2025) | Sumarização “difícil” | GPT-4o com **40%** de alucinação “unwanted” no recorte do paper · https://aclanthology.org/2025.naacl-short.38.pdf |
| **EMNLP 2025** (multilíngue, long-form QA) | Estimativa entre línguas | Taxas agregadas tipicamente na faixa **~7%–12%** no estudo · PDF: https://aclanthology.org/2025.emnlp-main.1481.pdf |

**Posição “favorável” (uso com salvaguardas):** ABA Formal Opinion **512** (29 jul 2024) — advogados **podem** usar IA generativa, mas com competência, revisão/verificação proporcional à tarefa, confidencialidade e candura ao tribunal.  
https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf

**Posição crítica / regulatória (transparência, não “banir LLM”):** EU AI Act, Art. 50 — obrigações de transparência (marcar interação com IA / conteúdo sintético), aplicáveis a partir de **2 ago 2026**. Não é uma proibição de alucinação; é informar o usuário.  
https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act

---

## Tese candidata (para você confirmar)

**Opção A (restritiva — alinhada ao caso jurídico):**  
*Defende-se que modelos de linguagem **não são apropriados como fonte autônoma** em decisões que exigem alta precisão factual (ex.: citação jurídica, diagnóstico, nota fiscal/contrato crítico); são apropriados apenas como **assistentes**, desde que haja verificação humana independente e rastreável.*

**Opção B (contextual):**  
*Defende-se que a apropriação depende do **risco do domínio**: em tarefas de baixa criticidade e com RAG/verificação, o uso é adequado; em decisões de alto risco factual sem verificação, é inadequado — independentemente do modelo.*

**Opção C (sua frase):** preencher depois das respostas abaixo.

---

## Mapa das 5 seções (quando escrever)

1. Contextualização — alucinação + tipos + por que “parece certo”  
2. Tese — uma das opções acima  
3. Argumentos (≥2) — (i) evidência empírica HALoGEN/Vectara; (ii) dano institucional no 9º Circuito  
4. Contra-argumento — “modelos melhoraram / Opinion 512 autoriza uso” → resposta: autorização ≠ autonomia factual; sanção foi por falta de verificação  
5. Síntese — implicações (protocolos de verificação, disclosure, RAG, limites de uso em alto risco)

---

## Checklist de fontes (mínimo do ED)

- [x] Caso ≤12 meses — 9º Circuito, jun/2026  
- [x] Posição favorável — ABA Opinion 512  
- [x] Posição crítica/restritiva — jurisprudência sancionadora + benchmarks HALoGEN/FaithBench  
- [x] Dado quantitativo — HALoGEN e/ou Vectara (sempre com escopo)  
- [x] Conceito técnico — alucinação (+ fabricação vs inexatidão)

---

## Perguntas em aberto (responder para eu redigir o texto)

1. Trabalho **solo** ou em **dupla**? Se dupla, nome do colega.  
2. Qual **tese** prefere: A, B ou outra (escreva em 1 frase)?  
3. Foco principal: **só direito**, ou também **saúde/educação** como analogia?  
4. Entrega em **português** (assumido) — o professor pediu algum tamanho mínimo além dos 2 parágrafos/seção?  
5. Quer o rascunho já em estrutura do `.docx` (Markdown → você cola no Word) ou prefere primeiro um **outline** curto?

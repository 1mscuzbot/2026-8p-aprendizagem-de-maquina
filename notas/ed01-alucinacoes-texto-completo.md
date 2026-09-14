# Estudo Dirigido 01 — Análise argumentativa

**Disciplina:** Aprendizagem de Máquina  
**Tema 4:** Alucinações em modelos de linguagem e confiabilidade  
**Autores:** Lucas Müller Scuzziato · Davi Emannoel Lopes de Souza  
**Formato de entrega pedido pelo professor:** arquivo `.docx` (um integrante posta; incluir os dois nomes)  
**Versão de trabalho:** Markdown (colar no Word / Google Docs e exportar `.docx`)

> **Sobre LaTeX:** o TCC usa ABNT/UTP porque a entrega final é monografia em PDF. Este ED pede **`.docx` no diretório do professor**. Montar o pipeline LaTeX do TCC aqui seria mais trabalho sem ganho de nota. Use este texto no Word.

---

## 1. Contextualização

Modelos de linguagem de grande porte (*large language models*, LLMs) geram texto fluente e persuasivo, o que os torna atrativos para tarefas jurídicas como pesquisa de precedentes, redação de petições e sumarização de documentos. Essa fluência, contudo, não equivale a garantia factual. Na literatura de processamento de linguagem natural, denomina-se **alucinação** a produção de enunciados desalinhados do conhecimento estabelecido sobre o mundo ou do contexto fornecido na entrada do modelo (Ravichander et al., 2025). Em outras palavras, o sistema pode afirmar com tom de certeza algo inexistente, incorreto ou não sustentado pelas fontes consultáveis. O perigo prático está exatamente nessa combinação: aparência de autoridade + conteúdo não verificado.

No domínio jurídico, a tipificação prática costuma distinguir pelo menos duas formas de erro relevantes para o advogado: **fabricações** (citações, ementas ou decisões que simplesmente não existem) e **inexatidões** (autoridades reais cujo conteúdo ou *holding* é distorcido). Essa distinção aparece na discussão acadêmica sobre ferramentas de pesquisa jurídica com IA e foi retomada em decisões disciplinares recentes de tribunais norte-americanos (Magesh et al., 2025; *Malkeet LNU*, 9º Cir., 2026). O risco específico do direito é institucional: uma citação inventada não é apenas um equívoco textual — ela induz o juízo, onera a parte adversa e compromete a confiança no processo. Diferentemente de um erro ortográfico, a alucinação jurídica ataca o próprio material de prova argumentativa do processo.

O problema não é novo. Em *Mata v. Avianca* (S.D.N.Y., 2023), advogados protocolaram precedentes gerados pelo ChatGPT que não existiam; a corte impôs sanção e deixou claro que o uso de ferramenta tecnológica não dispensa o papel de *gatekeeping* do advogado. O que mudou desde então é a escala de adoção e a expectativa de que ferramentas especializadas — inclusive com *retrieval-augmented generation* (RAG) — teriam “eliminado” o fenômeno. Avaliações empíricas posteriores mostram que essa expectativa é exagerada: mesmo produtos comerciais de pesquisa jurídica com RAG ainda alucinam em fração relevante das consultas (Magesh et al., 2025). Assim, a pergunta correta para o uso profissional não é se o modelo “parece bom”, e sim **em que medida** ele pode participar de decisões que exigem alta precisão factual.

## 2. Tese do grupo

Defende-se que **modelos de linguagem não são apropriados como fonte autônoma** em decisões jurídicas que exigem alto grau de precisão factual — em especial a identificação, citação e interpretação de precedentes e dispositivos normativos. Nesses contextos, LLMs são adequados apenas como **assistentes de produtividade**, desde que haja **verificação humana independente e rastreável** de cada afirmação factual relevante antes de qualquer uso perante o juízo, o cliente ou terceiros.

Os motivos principais são três. Primeiro, a alucinação permanece mensurável mesmo em *benchmarks* acadêmicos e em produtos especializados de pesquisa jurídica. Segundo, o dano processual de uma citação falsa é assimétrico: barato de gerar automaticamente e caro de desfazer perante o juízo. Terceiro, as próprias orientações éticas da advocacia norte-americana (ABA Formal Opinion 512, 2024) e a jurisprudência sancionadora recente autorizam o uso da ferramenta, mas **não** a substituição do dever de checagem. Em uma frase: a tecnologia pode entrar no fluxo de trabalho; a responsabilidade factual permanece humana.

## 3. Argumentação principal

### 3.1 Evidência empírica: a alucinação não desaparece com “IA jurídica”

O primeiro argumento é factual-técnico. O *benchmark* HALoGEN (ACL 2025) avaliou cerca de 150 mil gerações de 14 modelos em múltiplos domínios e concluiu que mesmo os melhores sistemas ainda produzem alucinações em escala relevante — em certos domínios, chegando a proporções muito elevadas dos *fatos atômicos* gerados (Ravichander et al., 2025). Não se trata, portanto, de um defeito residual de modelos antigos: o fenômeno é estrutural o bastante para merecer medição sistemática. HALoGEN ainda classifica erros segundo origem plausível (má recuperação do treino, conhecimento incorreto no treino ou fabricação), o que reforça que “alucinar” não é um rótulo único, e sim uma família de falhas com consequências práticas distintas.

Mais próximo do direito, Magesh et al. (2025), em estudo pré-registrado publicado no *Journal of Empirical Legal Studies*, avaliaram ferramentas comerciais de pesquisa jurídica com RAG (incluindo produtos da LexisNexis e da Thomson Reuters) e verificaram que essas ferramentas ainda alucinam **entre aproximadamente 17% e 33%** das consultas analisadas. O resultado é especialmente importante porque contradiz *marketing* de soluções “sem alucinação” ou com citações “garantidas”: o RAG reduz o problema em relação a *chatbots* genéricos, mas **não o elimina**. Se mesmo sistemas desenhados para o direito erram nessa faixa, utilizá-los como fonte autônoma de precedentes é incompatível com o padrão de precisão exigido em peça processual.

Leaderboards de consistência factual em sumarização, como o mantido pela Vectara (atualizações públicas em 2025–2026), mostram que taxas de alucinação variam conforme modelo e protocolo — frequentemente na casa de poucos pontos percentuais em tarefas de resumo *grounded*, e mais altas em modelos ou configurações menos favoráveis. Esses números **não** devem ser lidos como “taxa universal da IA”; devem ser lidos como evidência de que a falha factual é mensurável, variável e **não nula**. Em direito, uma taxa “baixa” ainda é inaceitável se o erro for uma jurisprudência inventada protocolada sem verificação. A lição metodológica é a mesma em todos esses estudos: falar de confiabilidade exige falar de **tarefa**, **protocolo** e **domínio** — e o domínio jurídico é particularmente intolerante a fabricação de autoridade.

### 3.2 Evidência institucional: o 9º Circuito (2026) e o dever de verificação

O segundo argumento é institucional e recente. Em 3 de junho de 2026, o *United States Court of Appeals for the Ninth Circuit* sancionou os advogados Mike Singh Sethi e William Rounds por apresentarem memoriais com múltiplos casos inexistentes, citações mal atribuídas e distorções graves de precedentes reais, bem como por falta de candura ao tratar da origem dos erros (*Malkeet LNU*, ordem disciplinar de 3 jun. 2026). As sanções incluíram multa de **US$ 2.500** para cada advogado, **suspensão de seis meses** para atuar perante aquele tribunal e obrigação de divulgar o uso de IA em petições por **dois anos**. A corte enfatizou que **não** estava punindo o mero uso de inteligência artificial generativa: as regras processuais e éticas são violadas no momento em que o advogado **assina e protocola** conteúdo falso, independentemente de a fabricação ter saído de um modelo ou de erro humano.

Esse caso cumpre o requisito de exemplo concreto dos últimos doze meses e ilustra a assimetria de risco da tese. A geração automática barateia a produção de texto “com cara de jurisprudência”; a correção consome tempo do juízo e da parte adversária e pode gerar sanção disciplinar. A cobertura da ABA Journal sobre a decisão destaca, ainda, que a falta de transparência — negar a origem dos erros e só depois admitir uso não autorizado de IA por redatores — agravou o desfecho. Em outras palavras, o problema não termina no clique que gera o texto; continua no silêncio que impede a correção rápida.

O precedente histórico *Mata v. Avianca* (2023) já tinha sinalizado o mesmo dever de *gatekeeping*, com multa conjunta de US$ 5.000 naquele episódio inaugural amplamente reportado. A decisão de 2026 mostra que o problema persiste três anos depois e que os tribunais estão dispostos a endurecer a resposta quando há reincidência de falta de candura. Em conjunto com Magesh et al. (2025), o quadro é coerente: a ferramenta pode errar; o profissional que não verifica transforma erro técnico em ilícito processual.

## 4. Contra-argumentação

A posição contrária mais consistente afirma que **é apropriado** empregar LLMs também em tarefas de alta precisão factual, desde que se usem modelos atualizados, ferramentas jurídicas especializadas e boas práticas profissionais. Em favor dessa visão, a American Bar Association, na Formal Opinion 512 (29 jul. 2024), reconhece que a IA generativa pode auxiliar o exercício da advocacia e **não proíbe** seu uso. A opinião exige, contudo, competência tecnológica, proteção da confidencialidade, comunicação adequada e — de modo central — **grau apropriado de verificação ou revisão independente** do resultado, proporcional à ferramenta e à tarefa. Em suma: a posição favorável não é “confie no modelo”; é “use o modelo, mas continue sendo advogado”.

Há, ainda, um segundo fio nessa posição contrária: a ideia de que a evolução técnica (modelos maiores, RAG, *leaderboards* de factualidade) tornaria o risco residual aceitável. De fato, rankings como o da Vectara documentam diferenças reais entre sistemas em tarefas de sumarização *grounded*, o que sugere que escolher ferramenta importa. Esse ponto deve ser reconhecido: não é indiferente usar um modelo qualquer ou uma ferramenta jurídica com recuperação de documentos.

Responde-se a esse contra-argumento reconhecendo seu núcleo correto e delimitando sua extensão. Concorda-se que o uso assistido é legítimo e, em muitos fluxos, desejável (organização de rascunhos, exploração preliminar de temas, sumarização *com* checagem posterior). Concorda-se também que melhores modelos e RAG reduzem — em alguns protocolos — a frequência do erro. Discorda-se da inferência de que autorização ética ou melhora de *benchmarks* tornem o modelo **fonte autônoma** de fatos jurídicos. A Opinion 512, lida com rigor, reforça a tese deste trabalho: o padrão profissional continua sendo a verificação humana. O estudo de Magesh et al. (2025) mostra que nem o RAG comercial remove o risco a níveis desprezíveis no próprio domínio do direito. E o 9º Circuito (2026) deixa explícito que o ponto crítico é o protocolo de assinatura e candura — não a existência da tecnologia. Assim, a limitação real da tese restritiva é prática, não conceitual: a verificação consome tempo e pode reduzir parte do ganho de produtividade. Essa limitação deve ser aceita quando o custo do erro factual for processualmente alto.

## 5. Síntese crítica

A questão norteadora pergunta em que medida é apropriado usar modelos de linguagem em decisões que exigem alta precisão factual. No recorte jurídico adotado neste estudo dirigido, a resposta é: **apropriado como assistência; inadequado como autoridade factual autônoma**. A adequação não decorre do marketing do produto nem da fluência do texto, e sim da existência de um circuito de verificação humana capaz de confirmar cada citação e cada afirmação normativa antes do uso externo. Essa conclusão articula o dado empírico (HALoGEN; Magesh et al.; Vectara), a orientação profissional (Opinion 512) e a sanção institucional recente (9º Circuito, 2026).

As implicações práticas são diretas. Escritórios e estudantes de direito que adotarem LLMs deveriam tratar citações geradas como **hipóteses a checar** em bases oficiais (tribunais, repositórios, legislação consolidada), nunca como resultado final. Um protocolo mínimo inclui: (i) abrir a fonte citada; (ii) confirmar se o trecho sustenta a tese; (iii) registrar quem verificou. Ferramentas com RAG podem entrar no fluxo, mas sem a ilusão de “zero alucinação”. Orientação ética do tipo da Opinion 512 e decisões como a do 9º Circuito apontam na mesma direção: transparência, revisão e responsabilidade profissional.

Olhando adiante, o campo tende a combinar melhores detectores e *leaderboards* de factualidade com regras processuais mais explícitas de *disclosure* de uso de IA. Nenhuma dessas camadas, porém, substitui o dever de ler o que se cita. Em síntese crítica, o avanço útil não é banir o modelo, nem sacralizá-lo. É redesenhar o fluxo de trabalho jurídico para que a velocidade da geração automática conviva com o padrão clássico de precisão do direito — um padrão que a alucinação, por definição, ameaça sempre que a verificação humana for omitida.

---

## Referências (citadas no texto)

AMERICAN BAR ASSOCIATION. Standing Committee on Ethics and Professional Responsibility. **Formal Opinion 512**: Generative Artificial Intelligence Tools. 29 jul. 2024. Disponível em: https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf. Acesso em: 14 set. 2026.

ABA JOURNAL. Attorneys’ lack of candor over AI errors leads to stricter sanctions. 2026. Disponível em: https://www.abajournal.com/news/article/attorneys-lack-of-candor-over-ai-errors-leads-to-stricter-sanctions. Acesso em: 14 set. 2026.

MAGESH, Varun et al. Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools. **Journal of Empirical Legal Studies**, 2025. DOI: https://doi.org/10.1111/jels.12413. PDF: https://dho.stanford.edu/wp-content/uploads/Legal_RAG_Hallucinations.pdf.

RAVICHANDER, Abhilasha et al. HALoGEN: Fantastic LLM Hallucinations and Where to Find Them. In: **Proceedings of the 63rd ACL**, 2025, p. 1402–1425. DOI: 10.18653/v1/2025.acl-long.71. Disponível em: https://aclanthology.org/2025.acl-long.71/.

UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT. **Malkeet LNU**; ordem disciplinar envolvendo Mike Singh Sethi e William Rounds. 3 jun. 2026. Disponível em: https://cdn.ca9.uscourts.gov/datastore/opinions/2026/06/03/24-4790.pdf. Acesso em: 14 set. 2026.

UNITED STATES DISTRICT COURT, S.D.N.Y. **Mata v. Avianca, Inc.**, Opinion and Order on Sanctions, 22 jun. 2023. Disponível em: https://www.nhd.uscourts.gov/sites/default/files/pdf/Mata-v-Avianca-sanctions-order.PDF.

VECTARA. **Hallucination Leaderboard** (repositório público, atualizações 2025–2026). Disponível em: https://github.com/vectara/hallucination-leaderboard. Acesso em: 14 set. 2026.

---

## Checklist do enunciado

- [x] Caso ≤ 12 meses (9º Cir., jun/2026)  
- [x] Posição favorável (ABA Opinion 512)  
- [x] Posição crítica (Magesh + sanções judiciais)  
- [x] Dado quantitativo (17%–33% Magesh; HALoGEN/Vectara com escopo)  
- [x] Conceito técnico (alucinação; fabricação × inexatidão)  
- [x] 5 seções com ≥ 2 parágrafos cada (versão um pouco mais longa, sem inventar dados)  
- [x] Tese explícita (tipo A)  
- [ ] Passar para `.docx` e postar no diretório do professor (ação de vocês)

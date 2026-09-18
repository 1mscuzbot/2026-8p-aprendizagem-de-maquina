# Revisão 1º bimestre — gabarito comentado

**Fonte:** `material/revisao-1b.pdf`  
**Disciplina:** Aprendizagem de Máquina  

Gabarito impresso no final do PDF: questões **1–20 = C**; V/F **A–J = V**, **K–T = F**. Q21 também **C**.

---

## Objetivas 1–21

| Q | Resp. | Motivo curto |
|---|:-----:|--------------|
| 1 | **C** | Chatbot = IA simbólica/regras; reconhecedor = ML a partir de dados |
| 2 | **C** | I–III corretas; IV falsa (consciência ≠ ML supervisionado) |
| 3 | **C** | Turing testa indistinguibilidade na conversa, não consciência/IA forte |
| 4 | **C** | X supervisionado; Y não supervisionado; Z reforço |
| 5 | **C** | Problema → dados → pré-processar → split → treinar → métricas |
| 6 | **C** | min-max: (35−20)/(60−20)=15/40=**0,375** |
| 7 | **C** | recall = VP/(VP+FN)=40/45≈**0,89** |
| 8 | **C** | I, II, IV; III falsa (complexidade não reduz viés e variância juntos) |
| 9 | **C** | Erro treino ↓ e teste ↑ → **overfitting** |
| 10 | **C** | Imputar ausentes + tratar outliers (idade 300) |
| 11 | **C** | Cor (nominal) → one-hot; satisfação (ordinal) → label/ordinal |
| 12 | **C** | preço=50+8×10=**130** |
| 13 | **C** | σ(1,5)=1/(1+0,223)≈**0,82** |
| 14 | **C** | H=−0,6·(−0,737)−0,4·(−1,322)=**0,971** |
| 15 | **C** | 3 vizinhos de P(4,5): C(1), E(0), B(0) → maioria **classe 0** |
| 16 | **C** | I e III; II falsa (suportes são os **mais próximos** da margem) |
| 17 | **C** | P1,P2→C1; novo C1 = ((1+2)/2,(2+1)/2)=**(1,5; 1,5)** |
| 18 | **C** | PCA = componentes = combinações lineares por variância |
| 19 | **C** | Normalizar numéricos + one-hot nominal + F1/recall (desbalanceado) |
| 20 | **C** | I–III; IV falsa (k importa em KNN e K-means) |
| 21 | **C** | I, III, IV; II falsa (erro desejado−gerado é do **supervisionado**) |

---

## Verdadeiro / Falso (A–T)

| | | |
|-|-|-|
| **A V** | Regras × ML | **K F** | KNN **usa distância**; escala importa |
| **B V** | Dado → info → conhecimento | **L F** | Vetores de suporte = **mais próximos** da margem |
| **C V** | Superv. × não superv. | **M F** | K-means depende da init; não garante ótimo global |
| **D V** | Overfitting + regularização | **N F** | PCA é **não supervisionado** (não usa rótulo) |
| **E V** | Acurácia engaña se desbalanceado | **O F** | ↑ complexidade não reduz viés e variância juntos |
| **F V** | Tratar outliers antes | **P F** | Regressão linear **não** aceita texto cru |
| **G V** | Normalizar antes do KNN | **Q F** | Doença rara → acurácia **não** basta |
| **H V** | Ordinal × one-hot | **R F** | Vetores perpendiculares → produto escalar 0 → **não** similares |
| **I V** | Sigmoide ∈ (0,1) | **S F** | Reforço **não** exige rótulo “correto” como no superv. |
| **J V** | Nó puro → entropia 0 | **T F** | Label encoding em nominal **≠** one-hot p/ modelos lineares |

---

## Fórmulas úteis

- min-max: `(x − min)/(max − min)`
- recall: `VP / (VP + FN)`
- sigmoide: `1 / (1 + e^(−z))`
- entropia binária: `−p log₂ p − (1−p) log₂(1−p)`

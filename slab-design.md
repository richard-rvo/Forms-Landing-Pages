---
name: slab-design
description: >
  Identidade visual oficial do S-LAB (Laboratório de Desenvolvimento Profissional em Saúde).
  Use esta skill sempre que precisar criar, adaptar ou avaliar qualquer material visual para o S-LAB —
  incluindo interfaces, apresentações, documentos, peças digitais, mockups, ícones ou qualquer
  artefato que precise seguir a identidade da marca. Garante consistência de cores, tipografia,
  símbolo e tom em todos os pontos de contato.
---

# S-LAB — Design System & Identidade Visual

## Sobre a Marca

**Nome completo:** S-LAB — Laboratório de Desenvolvimento Profissional em Saúde  
**Sigla de aplicação:** S-LAB  
**Segmento:** Educação / Saúde  
**Posicionamento:** Profissional, moderno, acessível, orientado à prática.

---

## Símbolo (Ícone)

O símbolo é composto pelas letras **S** e **L** integradas graficamente:

- O **S** ocupa a parte superior-esquerda, com traço arredondado e peso médio-bold.
- O **L** (invertido/espelhado) ancora a base do ícone, criando equilíbrio visual e leitura bidirecional.
- Um **traço horizontal curto** (dash) entre as letras reforça o ritmo do nome "S-LAB".
- O conjunto é inscrito em um **quadrado com cantos arredondados** (border-radius generoso, estilo app icon).

### Versões do Símbolo

| Versão | Fundo | Uso recomendado |
|---|---|---|
| **Primária** | Gradiente laranja (#F8A23B → #F08113) | Padrão digital, app, apresentações |
| **Monocromática** | Fundo preto (#1A1614), ícone branco | Fundo escuro, contraste alto |
| **Negativa** | Fundo branco/claro, ícone preto | Impressão, documentos formais |

### Regras do Símbolo

- Nunca distorcer proporções — o ícone é quadrado com cantos arredondados.
- Manter área de respiro mínima de **25% da largura do ícone** em todos os lados.
- Não aplicar sombras ou efeitos extras além do gradiente nativo.
- Em tamanhos menores que 24px, usar apenas a versão monocromática.

---

## Logotipo (Símbolo + Wordmark)

### Wordmark

- **"S-"** em peso leve/light, cor preta (#1A1614).
- **"LAB"** em peso leve/light, cor preta (#1A1614).
- O **traço "-"** entre S e LAB é renderizado em laranja (#F08113) — elemento de destaque da marca.
- Tipografia do wordmark: **geométrica sans-serif, peso light**, sem serifa. Referência visual próxima a: Futura Light, Nunito Light, ou similar de alta legibilidade.

### Tagline / Descritivo

```
LABORATÓRIO DE
DESENVOLVIMENTO PROFISSIONAL
EM SAÚDE
```

- Caixa alta, espaçamento entre letras generoso (letter-spacing: 0.1–0.15em).
- Peso: regular/light.
- Separada do logotipo por uma linha vertical laranja (#F08113) à esquerda.
- Tamanho: aproximadamente 30–35% do tamanho do wordmark principal.

---

## Paleta de Cores

### Cores Primárias (Laranja — identidade central)

| Nome | HEX | Uso |
|---|---|---|
| **Laranja Principal** | `#F8A23B` | Gradiente claro, botões secundários |
| **Laranja Forte** | `#F08113` | Gradiente escuro, CTA, destaques, traço do "-" |
| **Laranja Queimado** | `#E94D1D` | Alertas, hover states, urgência |

### Cores Neutras

| Nome | HEX | Uso |
|---|---|---|
| **Preto Suave** | `#1A1614` | Textos principais, ícone monocromático |
| **Cinza Médio** | `#87807A` | Textos secundários, legendas |
| **Branco Quente** | `#F2EEE7` | Fundos principais, áreas de respiro |
| **Off-White** | `#FAF7F2` | Fundo alternativo, cards |

### Cores de Apoio (Tons de Creme)

| Nome | HEX | Uso |
|---|---|---|
| **Creme Claro** | `#FFF4E8` | Background geral, telas principais |
| **Creme Médio** | `#FDE3C7` | Cards, seções destacadas |

### Gradiente Oficial do Símbolo

```css
background: linear-gradient(135deg, #F8A23B 0%, #F08113 60%, #E94D1D 100%);
```

---

## Tipografia

### Família Recomendada

O wordmark usa tipografia **geométrica sans-serif light**. Para consistência nos materiais, recomenda-se:

**Principal:** `Nunito` (Google Fonts — gratuita)  
**Alternativa:** `Poppins`, `Futura`, `Raleway`

### Escala Tipográfica

| Nível | Estilo | Peso | Uso |
|---|---|---|---|
| H1 | 48–64px | Light (300) | Títulos de destaque |
| H2 | 32–40px | Light (300) | Seções principais |
| H3 | 24–28px | Regular (400) | Subtítulos |
| Body | 16–18px | Regular (400) | Texto corrido |
| Caption | 11–13px | Regular (400) | Legendas, labels |
| Tag/Label | 10–12px | SemiBold (600), UPPERCASE | Categorias, badges |

### Regras Tipográficas

- Taglines e labels em **CAIXA ALTA** com letter-spacing de 0.1em ou mais.
- Nunca usar peso Bold no wordmark principal.
- Contraste mínimo texto/fundo: **4.5:1** (WCAG AA).

---

## Tom Visual & Estilo

- **Limpo e profissional** — espaço em branco generoso, hierarquia clara.
- **Quente, não clínico** — a paleta creme/laranja afasta o visual frio hospitalar típico do setor de saúde.
- **Moderno sem ser hype** — sem trends passageiros; foco em longevidade da identidade.
- **Ícones e ilustrações:** linha fina (stroke), sem fill sólido agressivo. Preferir estilo outline com 1.5–2px de espessura.

---

## Aplicações Digitais

### App Icon (Mobile)

- Quadrado com `border-radius: 22–25%` da largura (padrão iOS/Android).
- Gradiente oficial no fundo.
- Símbolo S-L em branco, centralizado.
- Nunca adicionar texto dentro do ícone no tamanho de app icon.

### Interface Web/App

```css
/* CSS Variables base */
--color-primary: #F08113;
--color-primary-light: #F8A23B;
--color-primary-dark: #E94D1D;
--color-text: #1A1614;
--color-text-secondary: #87807A;
--color-bg: #FFF4E8;
--color-bg-card: #FDE3C7;
--color-surface: #F2EEE7;
--color-white: #FAF7F2;

--gradient-brand: linear-gradient(135deg, #F8A23B 0%, #F08113 60%, #E94D1D 100%);
--border-radius-icon: 22%;
--border-radius-card: 12px;
--border-radius-button: 8px;
```

### Botões

- **CTA Primário:** fundo `#F08113`, texto branco, `border-radius: 8px`.
- **Secundário:** borda `#F08113`, texto `#F08113`, fundo transparente.
- **Ghost/Neutro:** fundo `#F2EEE7`, texto `#1A1614`.

---

## O Que Nunca Fazer

- ❌ Usar o laranja sobre fundo vermelho ou vice-versa (baixo contraste).
- ❌ Distorcer o símbolo ou alterar proporção S/L.
- ❌ Aplicar cores frias (azul, verde, roxo) como cor de destaque — fogem da identidade.
- ❌ Usar tipografia com serifa no wordmark ou em títulos principais.
- ❌ Reduzir o símbolo abaixo de 16px sem usar versão simplificada/monocromática.
- ❌ Usar gradiente em texto corrido — apenas em ícone e elementos de destaque.

---

## Checklist de Consistência

Antes de entregar qualquer peça visual S-LAB, verificar:

- [ ] Cores dentro da paleta oficial?
- [ ] Tipografia geométrica sans-serif light?
- [ ] Traço "-" em laranja (#F08113) no wordmark?
- [ ] Gradiente oficial no símbolo (quando colorido)?
- [ ] Área de respiro respeitada ao redor do logo?
- [ ] Contraste de acessibilidade adequado (4.5:1 mínimo)?
- [ ] Tom visual limpo, quente, profissional?
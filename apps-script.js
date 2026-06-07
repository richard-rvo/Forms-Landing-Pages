// ============================================================
// Google Apps Script — S-LAB · Criação de Landing Pages
//
// Como usar:
//   1. Abra a planilha Google Sheets que vai receber as respostas
//   2. No menu: Extensões > Apps Script
//   3. Cole TODO este código no editor (substitua o conteúdo existente)
//   4. Clique em "Implantar" > "Nova implantação"
//      - Tipo: Aplicativo da Web
//      - Executar como: Eu (sua conta)
//      - Quem tem acesso: Qualquer pessoa
//   5. Copie a URL gerada e cole em index.html na variável SCRIPT_URL
// ============================================================

// ── ⚙️  CONFIGURAÇÃO — ajuste aqui se necessário ──────────────
const SHEET_NAME = 'Inscrições'; // nome da aba no Sheets
// ─────────────────────────────────────────────────────────────

function doPost(e) {
  try {
    const sheet = getOrCreateSheet();
    const data  = e.parameter;

    sheet.appendRow([
      data.timestamp,
      data.nome,
      data.whatsapp,
      data.email,
      data.idade,
      data.sexo,
      data.profissao,
      data.tem_site,
      data.nivel_tec,
      data.objetivo,
      data.ferramentas,
      data.obstaculo,
      data.expectativa,
    ]);

    return response({ success: true });
  } catch (err) {
    return response({ success: false, error: err.message });
  }
}

function doGet() {
  return response({ status: 'Apps Script ativo ✓', projeto: 'S-LAB — Criação de Landing Pages' });
}

// ── Helpers ───────────────────────────────────────────────────

function getOrCreateSheet() {
  const ss    = SpreadsheetApp.getActiveSpreadsheet();
  let   sheet = ss.getSheetByName(SHEET_NAME);

  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);

    const headers = [
      'Data/Hora',
      'Nome completo',
      'WhatsApp',
      'E-mail',
      'Idade',
      'Sexo',
      'Profissão / Área de atuação',
      'Possui site hoje',
      'Nível de tecnologia',
      'Objetivo com Landing Page',
      'Ferramentas que já usou',
      'Maior obstáculo atual',
      'Expectativa com a aula',
    ];

    sheet.appendRow(headers);

    // Formata cabeçalho com identidade S-LAB
    const numCols = headers.length;
    const header  = sheet.getRange(1, 1, 1, numCols);
    header.setBackground('#F08113');
    header.setFontColor('#FFFFFF');
    header.setFontWeight('bold');
    sheet.setFrozenRows(1);

    // Larguras das colunas
    const widths = [150, 200, 130, 220, 100, 100, 220, 200, 200, 260, 260, 340, 340];
    widths.forEach((w, i) => sheet.setColumnWidth(i + 1, w));
  }

  return sheet;
}

function response(data) {
  return ContentService
    .createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}

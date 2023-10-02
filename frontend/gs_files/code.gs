
function createCSVMenu() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('CSV Functionality1')
    .addItem('Upload CSV', 'basicFunction')
    .addToUi();

  var ui = SpreadsheetApp.getUi();
  ui.createMenu('CSV Functionality2')
    .addItem('Upload CSV Server', 'UploadCSVDialog')
    .addToUi();
}



function UploadCSVDialog() {
  // Create a FilePicker dialog
  var htmlOutput = HtmlService.createHtmlOutputFromFile('filePicker')
    .setWidth(400)
    .setHeight(300);
  SpreadsheetApp.getUi().showModalDialog(htmlOutput, 'Upload CSV File');
}


function basicFunction(){
  var html = HtmlService.createHtmlOutputFromFile('UploadCSV')
      .setWidth(400)
      .setHeight(300);
  SpreadsheetApp.getUi().showModalDialog(html, 'Upload CSV File');

}


function uploadCSVFile(contents) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var newSheet = ss.insertSheet('NewSheet');
  var rows = contents.split("\n").map(function(row) {
    return Utilities.parseCsv(row);
  });
  newSheet.getRange(1, 1, rows.length, rows[0].length).setValues(rows);
}


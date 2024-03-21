function getApiData() {
    var url = 'https://api.torn.com/user/?selections=basic&key=YOUR_SECRET_API_KEY';  // Change YOUR_SECRET_API_KEY to your actual API key
    var response = UrlFetchApp.fetch(url);
    var json = response.getContentText();
    var data = JSON.parse(json);

    writeToSheet(data);
}

function writeToSheet(data) {
    // Open the Spreadsheet by its ID or name: adjust as necessary
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Sheet1');  // Change Sheet1 if you change the name of your sheet

    // Clear existing sheet content
    sheet.clear()

    // Starting row and column indices
    var row = 1;
    var col = 1;

    // Iterate over the key-value pairs in the data object
    for (var key in data) {
        if (data.hasOwnProperty(key)) {
            // Write the key in the first column and its value in the next column
            sheet.getRange(row, col).setValue(key)
            sheet.getRange(row, col + 1).setValue(data[key])
            // Move to the next row for the next key-value pair
            row++;
        }
    }
}
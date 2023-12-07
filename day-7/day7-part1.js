const fs = require('fs');

fs.readFile('day7-input.txt', 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  const lines = data.split(/\r?\n/); // Splits the text into lines
  console.log(lines);
});

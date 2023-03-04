const fs = require('fs');
const data = fs.readFileSync('books.tsv', 'utf16');

const arry = []

for(let i = 0; i < data.length; i++){
    arry.push(data)
}
console.log(arry)
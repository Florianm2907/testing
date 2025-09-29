// const fs = require('fs')
// console.log("test")

// // var fs = require('fs')
// var text = fs.readFileSync('./test.txt');

// var einzeln = text.split(" ")
// console.log(einzeln)


// async function fetchText() {
//     let response = await fetch('../test.txt');

//     console.log(response.status); // 200
//     console.log(response.statusText); // OK

//     if (response.status === 200) {
//         let data = await response.text();
//         console.log(data);
//         // handle data
//     }
// }

// fetchText();

var fs = require('fs');

fs.readFile('test1/script.txt', 'utf8', function(err, data) {
    if (err) throw err;
    // console.log(data);
    var einzeln = data.split(" ")
    for(i = 0; i< data.length; i++)
    
    
fs.appendFile('getrennt.txt', (einzeln[i] + '\n'), function (err) {
    if (err) {
    // append failed
    } else {
        
    }
})


});


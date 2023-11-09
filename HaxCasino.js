let seed = Math.floor(new Date().getTime() / 1000);
console.log("Seed is " + seed);

function generateNumber(varObj) {
    varObj.a = (1103515245 * varObj.a + 12345) % (2**31);
    return (varObj.a % 10) + 1;
}

var obj = {
a:  seed}
let xes = 0
let arr = new Array(); 
while (true){
    if (xes <= 35){
    arr[xes] = generateNumber(obj);
    xes = xes + 1
    }
    else{
    break
    }
}
console.log("Numbers gonna be " + arr);
const prompt = require('prompt-sync')();

const url_adress = prompt('Enter url: ');
const token = prompt('Enter token: ');


const { url } = require('inspector');
// request -> curl -X POST -H "Authorization: dd7aff1427e0f7c639dac0eabbc56452" -H "Content-Type: application/json" http://3.127.64.31:63417/play -d '{"bet": 100, "guess": 7}'

bet = 100
const request = require('request');
for (pos = 0; pos < 35; pos++){
    request.post({
        headers: {'Authorization': token, 'Content-Type': 'application/json'},
        url: url_adress,
        body: JSON.stringify({bet: bet, guess: arr[pos]})
    }, function(error, response, body){
        console.log(body);
    });
    bet = bet * 2
}


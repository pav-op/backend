var express = require('express');
var app = express();


let sleep = ms => {
return new Promise(resolve => setTimeout(resolve, ms));
};


app.use(express.json());

app.get('/', (req, res) => {
    res.send("You are gay")
});

let obj;

app.post('/', function(request, response){
    obj = request.body;      // your JSONresponse
    response.send("Works");    // echo the result back
});

app.get('/gay', (req, res) => {
    sleep(2000).then(() => {
        console.log("oolalalala");
        res.send(obj);
    })
});

app.listen(3000);

const express = require("express");
const fs = require('fs');
const app = express()
const path = require("path")
const {spawn} = require('child_process');


//Settings
app.set('port',3000)
app.set('public', path.join(__dirname, 'public'))


const codeFolder = path.join(__dirname, 'code')

app.use(express.urlencoded({extended:true}))

page=path.join(app.get('public'),'/index.html')

app.get("/", (req,res) =>{
    res.sendFile(page)
})

app.post('/', (req,res) => {
    console.log(req.body);
    var filepath = path.join(codeFolder, 'test.txt')
    var fileContent = req.body.code
    fs.writeFile(filepath, fileContent, (err) => {
        if (err) throw err;
        console.log("The file was succesfully saved!");
        console.log(fileContent);
    }); 

    res.sendFile(page);
    
    // spawn new child process to call the python script
    //const python = spawn('python', ['main.py']);
    // collect data from script
   // python.stdout.on('data', (d) => {
    //    data = d
    //});
        // in close event we are sure that stream from child process is closed
 //      python.on('close', (code) => {
  //     console.log(`child process close all stdio with code ${code}`);
 //       res.send("post data received "+ data)
 //   });


})

app.use(express.static('public'));

app.listen(app.get('port'), () =>{
    console.log(`Server on port ${app.get('port')}`);

})



   /*
    

    */
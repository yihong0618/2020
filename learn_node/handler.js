let exec = require("child_process").exec;

exports.start = (response) => {
    exec("ls -lah", function(error, stdout, stderr) {
        response.writeHead(200, {"Content-Type": "html/plain"})
        response.write(stdout)
        response.end()
    })
}


exports.upload = (response) => {
    let body = '<html>'+
    '<head>'+
    '<meta http-equiv="Content-Type" content="text/html; '+
    'charset=UTF-8" />'+
    '</head>'+
    '<body>'+
    '<form action="/upload" method="post">'+
    '<textarea name="text" rows="20" cols="60"></textarea>'+
    '<input type="submit" value="Submit text" />'+
    '</form>'+
    '</body>'+
    '</html>';

    response.writeHead(200, {"Content-Type": "text/html"});
    response.write(body);
    response.end();
}


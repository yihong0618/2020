let exec = require("child_process").exec;

exports.start = (response) => {
    console.log("fafa");
    exec("ls -lah", function(error, stdout, stderr) {
        response.writeHead(200, {"Content-Type": "html/plain"})
        response.write(stdout)
        response.end()
    })
}


let http = require("http")
let url = require("url")


function start(route, handle) {
    function onRequest(request, response) {
        let pathName = url.parse(request.url).pathname
        // console.log(`Request ${pathName} route received`)
        route(pathName, handle)
        response.writeHead(200, {"Content-Type": "text/html"});
        response.write("<h1>Hello World</h1>");
        response.end();
    }
    http.createServer(onRequest).listen(8888);
    console.log("Server has started");
}


exports.start = start

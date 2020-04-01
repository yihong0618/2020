let server = require("./server")
let route = require("./route")
let start = require("./handler")

handle = {
    "/test": () => {console.log(3333333333);return "hello test"},
    "/name": () => {return "hello name"},
    "/start": start.start
}


server.start(route.route, handle)

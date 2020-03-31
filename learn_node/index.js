let server = require("./server")
let route = require("./route")

handle = {
    "/test": () => {console.log(3333333333);return "hello test"},
    name: () => {return "hello name"}
}


server.start(route.route, handle)

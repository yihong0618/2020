

function test(message) {
    console.log("Test" + message)
}

function upload(message) {
    console.log("Upload" + message)
}

function route(pathname, handle) {
  console.log("About to route a request for " + pathname);
  if (typeof handle[pathname] === 'function') {
    console.log(22222222222222222);
    handle[pathname]();
  } else {
    console.log("No request handler found for " + pathname);
  }
}

exports.route = route;

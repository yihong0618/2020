

function test(message) {
    console.log("Test" + message)
}

function upload(message) {
    console.log("Upload" + message)
}

function route(pathname, handle, response) {
  console.log("About to route a request for " + pathname);
  if (typeof handle[pathname] === 'function') {
    return handle[pathname](response);
  } else {
      return "no route found"

  }
}

exports.route = route;

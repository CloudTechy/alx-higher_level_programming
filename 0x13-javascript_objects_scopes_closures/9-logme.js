#!/usr/bin/node

function logMe () {
  let args = [];
  
  return function (arg) {
    args.push(arg);
    console.log(`${args.indexOf(arg)}: ${arg}`);
  };
}

module.exports.logMe = logMe();

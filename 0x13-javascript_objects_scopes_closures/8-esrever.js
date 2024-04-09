#!/usr/bin/node

function esrever (list) {
  let i = list.length - 1;
  const nlist = [];
  for (i; i >= 0; i--) {
    nlist.push(list[i]);
  }
  return nlist;
}

module.exports.esrever = esrever;

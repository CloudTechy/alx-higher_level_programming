#!/usr/bin/node

function converter (base) {
  const b = base;

  return function (num) {
    return num.toString(b);
  };
}

module.exports.converter = converter;

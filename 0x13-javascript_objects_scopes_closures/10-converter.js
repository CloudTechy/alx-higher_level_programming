#!/usr/bin/node

const converter = (base) => {
  return (num) => num.toString(base);
};
exports.converter = converter;

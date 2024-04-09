#!/usr/bin/node

const _converter = (base) => {
  return (num) => num.toString(base);
};

let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));
export { _converter as converter };

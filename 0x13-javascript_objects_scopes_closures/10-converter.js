#!/usr/bin/node

const _converter = (base) => {
  return (num) => num.toString(base);
};

let myConverter = _converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

myConverter = _converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));
export { _converter as converter };

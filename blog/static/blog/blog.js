const One = 1;
const theNumber = One;
let yourName = 'Ben';

function print_alert(name, count){
  alert(name + '[' + count + ']')
};

if (theNumber === One) {
  yourName = 'Leo';
  print_alert(yourName + '!', theNumber);
};

print_alert(yourName, theNumber);

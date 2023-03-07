function tempUnit(inpUnit) {
  
  
  if (inpUnit == 1) {
    let Unit = prompt("Enter temperature in Celsius: ") 
    let intUnit = parseInt(Unit)
    let c = intUnit;
    let f = ((9/5)*c)+32
    let k = c + 273.15

    console.log("Select your resulting unit:");
    console.log("2) Press 'f' for fahrenheit.");
    console.log("3) Press 'k' for kelvin.");
    let res = prompt();

    if (res == 'f' || res == "F") {
      console.log("Temperature in Fahrenheit: ",f)
      
    }

    else if (res == 'k' || res == 'K') {
      console.log("Temperature in Kelvin: ",k)
      
    }
       
    
  } 
  
  else if (inpUnit == 2) {
    let Unit = prompt("Enter temperature in Fahrenheit: ")
    let intUnit = parseInt(Unit)
    let f = intUnit;
    let c = (f-32)*(5/9);
    let k = c + 273.15

    console.log("Select your resulting unit:");
    console.log("1) Press 'c' for celsius.");
    console.log("3) Press 'k' for kelvin.");
    let res = prompt();

    if (res == 'c' || res == "C") {
      console.log("Temperature in Celsius: ",c)
      
    }

    else if (res == 'k' || res == 'K') {
      console.log("Temperature in Kelvin: ",k)
      
    }
  }

  else if (inpUnit == 3) {
    let Unit = prompt("Enter temperature in Kelvin: ")
    let intUnit = parseInt(Unit)
    let k = intUnit;
    let c = k - 273.15;
    let f = ((9/5)*c)+32

    console.log("Select your resulting unit:");
    console.log("1) Press 'c' for celsius.");
    console.log("2) Press 'f' for fahrenheit.");
    let res = prompt();

    if (res == 'c' || res == "C") {
      console.log("Temperature in Celsius: ",c)
      
    }

    else if (res == 'f' || res == 'F') {
      console.log("Temperature in Fahrenheit: ",f)
      
    }
    
  }
    
    
}


console.log("Choose your options:");
console.log("1) Press 1 to enter temperature in celsius.");
console.log("2) Press 2 to enter temperauture in fahrenheit.");
console.log("3) Press 3 to enter temperature in Kelvin.");
let inpUnit = prompt();

let endRes = tempUnit(inpUnit);

console.log(endRes);
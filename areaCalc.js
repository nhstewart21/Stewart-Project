function calculateArea(myRadius) {
    
    var myArea = (myRadius * myRadius * 3.14);
    var myArea = myArea.toFixed(1);
    return myArea;
}

function displayArea() {

    var myArea = (myRadius * myRadius * Math.PI);
    var myArea = myArea.toFixed(1);
    alert("A circle with a " + myRadius + " centimeter radius has an area of " + myArea + " square centimeters. " + myRadius + " represents the number entered by the user. " + myArea + " represents circle area based on the user input.");
    

}

var myRadius = parseFloat(prompt("Enter Radius number", ""));

calculateArea(myRadius);

displayArea();
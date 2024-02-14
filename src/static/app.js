const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
let properties = {};
let shapeType=null;

let shapes=[]
// Function to handle mouse clicks on the canvas
canvas.addEventListener('click', function(event) {
    const rect = canvas.getBoundingClientRect();
     mouseX = event.clientX - rect.left;
     mouseY = event.clientY - rect.top;
    createShape(mouseX, mouseY); // Call the createShape function with mouse coordinates
});

function createShape(x, y) {
    if (!shapeType) return; // Exit if the user cancels the prompt

     // Object to store shape properties

    // Prompt the user for shape-specific properties
    switch (shapeType.toLowerCase()) {
        case 'circle':
            properties.radius = parseFloat(prompt('Enter circle radius:'));
            if (!properties.radius) return; // Exit if the user cancels the prompt
            break;
        case 'rectangle':
            properties.width = parseFloat(prompt('Enter rectangle width:'));
            properties.height = parseFloat(prompt('Enter rectangle height:'));
            if (!properties.width || !properties.height) return; // Exit if the user cancels the prompt
            break;
        // Add cases for other shape types as needed
    }
    const currentShape={ ...properties, x, y }
    console.log(currentShape);
    shapes.push(currentShape);
    properties={};
    drawShape(currentShape,shapeType);
    // Send a POST request to the backend API to create the shape
    fetch('http://127.0.0.1:5000/shapes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            type: shapeType,
            properties: currentShape // Include mouse coordinates in shape properties
        })
    })
    .then(response => response.json())
    .then(data => {
        // Draw the shape on the canvas based on the response from the server
        console.log(data);
    })
    .catch(error => console.error('Error creating shape:', error));
}
async function getAllOnReload(){
    try {
        const response=await fetch(`http://localhost:5000/shapes`);
        if(response.status===200){
            const data= await response.json();
            console.log(data.shapes);
            drawAll(data.shapes);
        }
    } catch (error) {
        
    }
}
function setType(type){
    shapeType=type
}
function drawShape(shapeData,shapeType) {
    // Clear the canvas
   // ctx.clearRect(0, 0, canvas.width, canvas.height);
    // Draw the shape based on its type and properties
    switch (shapeType.toLowerCase()) {
        case 'circle':
         //   console.log(mouseX, mouseY, properties.radius, 0, Math.PI * 2);
            ctx.beginPath();
            ctx.arc(shapeData.x, shapeData.y, shapeData.radius, 0, Math.PI * 2);
            ctx.stroke();
            break;
        case 'rectangle':
            ctx.beginPath();
            ctx.rect(shapeData.x, shapeData.y, shapeData.width, shapeData.height);
            ctx.stroke();
            break;
        // Add cases for other shape types as needed
    }
}
function drawAll(allShapeData){
    allShapeData.forEach(shape => {
        drawShape(shape.properties,shape.type);
    });
}
getAllOnReload();
// Initialize canvas
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let gameState = { x: 0, y: 0, score: 0 };

function drawTurtle() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);  // Clear canvas
    ctx.fillStyle = "green";
    ctx.fillRect(gameState.x, gameState.y, 20, 20);  // Draw turtle at the new position
}

function moveTurtle(direction) {
    fetch('/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ direction: direction })
    })
    .then(response => response.json())
    .then(data => {
        gameState = data;  // Update the game state with the new data from Flask
        drawTurtle();  // Redraw the turtle after the move
    });
}

document.addEventListener("keydown", function (event) {
    if (event.key === "ArrowUp") moveTurtle("up");
    if (event.key === "ArrowDown") moveTurtle("down");
    if (event.key === "ArrowLeft") moveTurtle("left");
    if (event.key === "ArrowRight") moveTurtle("right");
});

drawTurtle();  // Initial drawing of the turtle

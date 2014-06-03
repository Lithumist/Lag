/* 
 * runner.js
 * 
 * sets up jaws and starts the game.
 * 
*/ 

function init ()
{
    gCanvas = document.getElementById('canvasGame');
    gContext = gCanvas.getContext('2d');
    
    gContext.fillStyle = "#FF0000";
    gContext.fillRect(0, 0, 640, 480);
}
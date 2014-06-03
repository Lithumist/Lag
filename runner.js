/* 
 * runner.js
 * 
 * sets up jaws and starts the game.
 * 
*/ 

#include "game.js"

jaws.onload = function() {
    jaws.assets.add( "data/gfx/placeholder_1.png" );
    jaws.start( stateGame );
}
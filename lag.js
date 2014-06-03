/* 
 * runner.js
 * 
 * sets up jaws and starts the game.
 * 
*/ 

/*  * game *  * the gameplay state * */ function stateGame (){    this.setup = function ()    {        player = new jaws.Sprite({ image:"data/gfx/placeholder_1.png", x:20, y:20, width:16, height:16 });        player.scaleTo(2);    }        this.update = function ()    {        // move player        if ( jaws.pressed( "up" ) ) player.y -= 4;        if ( jaws.pressed( "down" ) ) player.y += 4;        if ( jaws.pressed( "left" ) ) player.x -= 4;        if ( jaws.pressed( "right" ) ) player.x += 4;    }        this.draw = function ()    {        jaws.clear();        player.draw();    }}
jaws.onload = function() {
    jaws.assets.add( "data/gfx/placeholder_1.png" );
    jaws.start( stateGame );
}
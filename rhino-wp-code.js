var FileReader = java.io.FileReader;
var BufferedReader = java.io.BufferedReader;

function test123(){
    var inix = 46 -1;
    var iniy = 106;
    var xlimit = 77;
    var ylimit = 137;
    var x = inix;
    var y = iniy;
    var index = 0;

    var path = "/home/Documents/mindy/bad_apple/decode-v31" + ".mlog";
    var reader = new BufferedReader(new FileReader(path));
    var lines = [];
    var line;
    while ((line = reader.readLine()) !== null) {
        lines.push(line);
    };
    while (true) {
        x += 1;
        if (x > xlimit){
            x = inix + 1;
            y += 1;
            if (y > ylimit){
                break;
            };
        };
        var tile = Vars.world.tile(x, y);
        if (tile.block() == 'world-processor'){
            index += 1;
            lines[1] = "read indextable processor" + index + " \"proc" + index + "\"";
            tile.build.code=lines.join('\n');
        };
    };
    reader.close();
};

test123();



var FileReader = java.io.FileReader;
var BufferedReader = java.io.BufferedReader;

var index = 1;

function test123(){
    var inix = 46 - 1;
    var iniy = 106;
    var xlimit = 77;
    var x = inix + 1;
    var y = iniy;
    var skip = 1;

    while (true) {
        var path = "/home/Documents/mindy/bad_apple/output/boutput" + index + ".txt";
        var reader = new java.io.BufferedReader(
            new java.io.InputStreamReader(
                new java.io.FileInputStream(path), "UTF-8"
            )
        );
        while (true) {
            x += 1;
            if (x > xlimit){
                x = inix + 1;
                y += 1;
            };
            var tile = Vars.world.tile(x, y);
            if (tile.block() == 'micro-processor'){
                if (skip <= 36){
                    skip += 1;
                } else {
                    tile.build.code ="set a " + reader.readLine();
                    break;
                };
            };
        };
        reader.close();
        index += 1;
        print(index);
        print(tile);
    };
};

test123();



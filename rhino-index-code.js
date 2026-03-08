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
    var iindex = 1;

    var path = "/home/Documents/mindy/bad_apple/output/1proc_index_table.txt";
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
        if (tile.block() == 'micro-processor'){
            if (iindex == 0){
                iindex += 1;
            } else {
                tile.build.code=lines[index];
                print(tile);
                index += 1;
                if (index > 35){
                    break
                };
            };
        };
    };
    reader.close();
};

test123();



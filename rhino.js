var FileReader = java.io.FileReader;
var BufferedReader = java.io.BufferedReader;

var index = 1;

function test123(){
    var inix = 115 - 1;
    var iniy = 90;
    var x = inix;
    var y = iniy;
    while (true) {
        var path = "./output/boutput" + index + ".txt";
        var reader = new BufferedReader(new FileReader(path));
        var line;
        x += 1;
        if (x > 130){
            x = inix + 1;
            y += 1;
        };
        print("index" +index);
        print(x);
        print("  " +y);
        var code = "Vars.world.tile("+x+", "+y+").build.code=` set a \\";
        while ((line = reader.readLine()) != null) {
            line = line.replace(/\\/g, "\\\\");
            line = line.replace(/`/g, "\\`");
            code += line;
        };
        code = code.substring(0, code.length - 1);
        code += "\\\"`";

        eval(code);

        reader.close();
    
        index += 1;
    };
};

test123();



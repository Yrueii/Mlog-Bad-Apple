var index = 1;

function test123(){
    var wpx = 114;
    var wpy = 89;
    var inix = 115 - 1;
    var iniy = 90;
    var ylimit = 100;
    var x = inix;
    var y = iniy;
    while (true) {
        x += 1;
        if (x > 130){
            x = inix + 1;
            y += 1;
        };
        print("index" +index);
        print(x);
        print("  " +y);
        Vars.world.tile(wpx, wpy).build.links.add(new LogicBlock.LogicLink(x, y, "processor" + index, true));

        if (y > ylimit){
            break;
        };
    
        index += 1;
    };
};

test123();



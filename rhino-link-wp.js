var index = 1;
function test123(){
    var inix = 46 - 1;
    var iniy = 106;
    var xlimit = 77;
    var ylimit = 137;
    var x1 = inix;
    var y1 = iniy;
    while (true) {
        var x = inix;
        var y = iniy;
        x1 += 1;
        if (x1 > xlimit){
            x1 = inix + 1;
            y1 += 1;
        };
        var wp = Vars.world.tile(x1, y1);
        if (wp.block() == 'world-processor'){
            print(wp);
            var index = 1;
            while (true) {
                x += 1;
                if (x > xlimit){
                    x = inix + 1;
                    y += 1;
                };
                var tile = Vars.world.tile(x, y);
                if (tile.block() == 'micro-processor'){
                    wp.build.links.add(new LogicBlock.LogicLink(x, y, "processor" + index, true));
                    index += 1;
                };

                if (y > ylimit){
                    break;
                };
            };
        };
    };
};

test123();



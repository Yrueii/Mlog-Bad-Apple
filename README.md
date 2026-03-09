Bleeding edge Mindustry version is needed for this to work properly.  
V8 might work but i haven't tested it yet.  

For schematic file, you can find them in the [Releases](https://github.com/Yrueii/Mlog-Bad-Apple/releases/tag/v2.1).
Otherwise if you want to built it yourself please read below.

Almost everything is hardcoded.  
You would need to input your own bad apple video for the `bad apple to string.py` file.  
video input will be taken from ./input/untitled.mp4  
The video should be the same resolution as the display you're planning to show in Mindustry.  
The python file will convert the video into strings that can be stored in micro processors.  
each strings will be a .txt file in ./output  
each strings should go into 1 micro processor  
these micro processor themself only store frames data to be read by the world processor, using larger processor would not make it faster as it is only a ROM.  

The `generate index.py` is for generating indexes for each workers (world processors).  
the v31 decode version uses parallelization, 36 world processor work together to render each frame, pre computed index is needed so those workers doesn't need to search for their slice of data.  

The .mlog files are code for the world processor itself that reads data from your micro processors ROM and draws them in the display.  
Each micro processors ROM needs to be linked to the world processor in ORDER.  
The postfix (eg, V1) are the decoding method, in the python file there's a variable called `encoding_version`.  
What mlog files you use should match the `encoding_version` in the python file.  
Though version 2 is experimental, and might not work well.  
Version 3 is what you see on the release v1.0  
These code assumes the world processor have access to unconstrained IPT rate, hence the multiple thousands value in `setrate`  
This can be done with a mod, or the console.  
Though with increasing the IPT, you would also need to increase your game FPS to around ~500fps for optimal experience. This is needed because display buffer only allows 1024 draw operations per game frame.  
on release v2.0 and v2.1, each processor now is only at 1000 ipt, though high game fps is still needed for it to be smooth, around ~250 fps, the higher your game fps is generally the better it will be.  

on v31 there's a clock code, this is for a seperate world processor than the workers, and acts as a global clock for the workers, this world processor need to be linked to all workers, inversely all workers need to link the clock processor.  

For console ensure you enable console settings in Settings -> Game -> Enable Console.
on PC press f8 to show the console.
on Mobile there isn't really a button for it, but you can install a mod where it will show the console for you.
to use simpy copy paste the .js file mentioned below to the console and enter.

The rhino.js is for the console in Mindustry to take the strings and put them in your (already built) micro processors.  
Once again most of the variables are hardcoded, the code fills from left to right, top to bottom.  
`inix` and `iniy` should be the coordinates of your first (left and bottom most) processor in your ROM block.  
On line 16 `if (x > 130){` is the width of your ROM block, the `130` should be replaced with the x coordinates of the right most processor in your ROM block.  
it filters by micro-processor only.  

the rhino-link-wp.js is for linking the world processor to your ROM block, its similar to the rhino.js file, most of the variables are harcoded.  
pay attention to the ylimit variable, as this is the variable that exits the code when it reaches a certain point, without this your Mindustry might run the code forever and crash your game.  
`wpx` and `wpy` are your world processor coordinates.  
it filters by world-processor and links to only micro-processor.  

the rhino-wp-code.js is for inserting code into world processors automatically, it filters by world-processor only  
also automatically increment the second line indexes so it fetches the correct index table  

the rhino-index-code.js is for inserting index table code into the first 36 micro-processors.  
on v31 each worker will fetch index table from their approriate micro-processors  


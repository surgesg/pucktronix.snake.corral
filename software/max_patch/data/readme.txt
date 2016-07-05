pucktronix.snake.corral
readme.txt
last modified 02.26.2012

software, text, and images copyright 2012 
greg surges
surgesg@gmail.com
http://www.gregsurges.com/

pucktronix.snake.corral is a computer-controlled dual 8 x 8 analog signal routing matrix. 
Two independent matrices are presented, each with 8 inputs and 8 outputs. Within each matrix,
any input (or summed combination of inputs) can be routed to any output. The device can switch 
and route any type of analog signal within the range of +/- 5V. The main electronic components 
of the pucktronix.snake.corral are a Teensy 2.0 and a pair of Zarlink MT8816 analog switching 
matrix ICs. The MT8816 is a bidirectional 8 x 16 matrix with minimal signal bleed.
Like the USB-Octomod, the pucktronix.snake.corral is powered from the USB bus. 

A Max/MSP patch which allows the user to define and switch between presets and/or 
apply various algorithmic rhythmic effects to the switching matrices has also been developed. 

Using the pucktronix.snake.corral, a modest number of synthesis modules can be used 
to create interesting rhythmic and timbral variety. The ability to rapidly switch or 
reconfigure a large number of signal connections enables a level of rhythmic complexity 
which is difficult to obtain through other means. Sharp cuts between disparate types 
of musical material are made possible, and patches can be stored and quickly recalled. 

The software is available in two forms, a Max 6 collective which can be run using the free 
Max 6 runtime software available from cycling74.com, and a standalone application. Currently,
the standalone is OS X only, but hopefully a volunteer can help compile it for Windows.

On loading the software, the user is presented with two sets of matrix controls and a set of 
serial port controls. The first thing to do is to select the serial port which the snake.corral
device is plugged into, and then click the "open serial" button. 

Matrix connections can be made by clicking cells on the large matrices. If desired, a configuration  
can be saved as a preset by shift-clicking one of the preset slot circles to the right of each matrix.A preset can be recalled by clicking a circle. 

Below the preset selection buttons are a pair of buttons, one for clearing the matrix, and one for
setting up a random automation configuration. The two number boxes below select low and high range
limits for the automation timing. 

Finally, to the far right of each matrix is a rhythmic automation interface. By selecting one of the
tabs labeled "sinusoid", "periodic", "random", or "pucklet", the user can then toggle a given
cell to toggle itself on/off with the corresponding rhythmic type. The number box below selects a 
relevant time value for each automation type. 

Please contact me with suggestions or questions. 

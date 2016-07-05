# pucktronix.snake.corral

Source code for the pucktronix.snake.corral dual 8 x 8 modular switching matrix hardware.

pucktronix.snake.corral is a computer-controlled dual 8 x 8 analog signal routing matrix. 
Two independent matrices are presented, each with 8 inputs and 8 outputs. 
Within each matrix, any input (or summed combination of inputs) can be routed to any output. 
The device can switch and route any type of analog signal within the range of +/- 5V. 
The main electronic components of the pucktronix.snake.corral are a Teensy 2.0 and a pair of Zarlink MT8816
analog switching matrix ICs. The MT8816 is a bidirectional 8 x 16 matrix with minimal signal bleed. 
Like the USB-Octomod, the pucktronix.snake.corral is powered from the USB bus.
A Max/MSP patch which allows the user to define and switch between presets and/or apply various algorithmic 
rhythmic effects to the switching matrices has also been developed.

Using the pucktronix.snake.corral, a modest number of synthesis modules can be used to create interesting 
rhythmic and timbral variety. 
The ability to rapidly switch or reconfigure a large number of signal connections
enables a level of rhythmic complexity which is difficult to obtain through other means. 
Sharp cuts between disparate types of musical material are made possible, and patches can be stored and quickly recalled.

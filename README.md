# Graphics_Design
# Run "graphics.h" in Ubuntu
```
#1. sudo apt-get install build-essential
#2.  sudo apt-get install libsdl-image1.2 libsdl-image1.2-dev guile-1.8 guile-1.8-dev libsdl1.2debian libart-2.0-dev       libaudiofile-dev libesd0-dev libdirectfb-dev libdirectfb-extra libfreetype6-dev libxext-dev x11proto-xext-dev libfreetype6 libaa1 libaa1-dev libslang2-dev libasound2 libasound2-dev
#3. Now download: libgraph.
```
http://computersolutions03.blogspot.com/2013/10/run-graphicsh-in-ubuntu.html
```
Copy libgraph-1.0.2.tar.gz to your home folder. Right click on it and select "Extract Here".
#4.  cd libgraph-1.0.2
#5.  ./configure
#6. sudo make
#7. sudo make install
#8. sudo cp /usr/local/lib/libgraph.* /usr/lib
#9. Create file name:sample.c

/*	sample.c (Graphics program)	*/

#include <stdio.h>
#include <graphics.h>

int main()
{
	int gd=DETECT,gm;
	initgraph(&gd,&gm,NULL);

	line(0,getmaxy()/2,getmaxx(),getmaxy()/2);
	line(getmaxx()/2,0,getmaxx()/2,getmaxy());

	setcolor(BLUE);
	circle(getmaxx()/2,getmaxy()/2,150);

	setcolor(GREEN);
	circle(getmaxx()/2,getmaxy()/2,75);

	setcolor(RED);
	circle(getmaxx()/2,getmaxy()/2,25);

	delay(5000);
	closegraph();
	return 0;
}
#10. gcc sample.c -o sample -lgraph
#11. ./sample
```

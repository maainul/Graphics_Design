# include<stdio.h>
# include<graphics.h>
void main()
{
            int gd=DETECT,gm,xc,yc,r,x,y,Pk;
            initgraph(&gd,&gm,"c:\\turboc3\\bgi");
            printf("*** Bresenham's Circle Drawing Algorithm ***\n");
            printf("Enter the value of Xc\t");
            scanf("%d",&xc);
            printf("Enter the value of yc\t");
            scanf("%d",&yc);
            printf("Enter the Radius of circle\t");
            scanf("%d",&r);
            x=0;
            y=r;
            putpixel(xc+x,yc-y,1);
            Pk=3-(2*r);
            for(x=0;x<=y;x++)
            {
                        if (Pk<0)
                        {
                                    y=y;
                                    Pk=(Pk+(4*x)+6);
                        }
                        else
                        {
                                    y=y-1;
                                    Pk=Pk+((4*(x-y)+10));
                        }
                        putpixel(xc+x,yc-y,7);
                        putpixel(xc-x,yc-y,7);
                        putpixel(xc+x,yc+y,7);
                        putpixel(xc-x,yc+y,7);
                        putpixel(xc+y,yc-x,7);
                        putpixel(xc-y,yc-x,7);
                        putpixel(xc+y,yc+x,7);
                        putpixel(xc-y,yc+x,7);
                        delay(100);

            }
}

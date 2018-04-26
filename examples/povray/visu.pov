#include "colors"

#declare ISOSURFACE=0;
#declare CLOUD=1;

#declare INTERPOLATE=1;
#declare NBX=32;
#declare NBY=32;
#declare NBZ=64;
#declare ISOLEVEL=0.7;



global_settings {
  assumed_gamma 1.0
}

camera {perspective location  <0.0, 20.0, -25.0> look_at <0.0,0.0,0.0> angle 45}
//camera {perspective location  <0.0, 0.0, -25.0> look_at <0.0,0.0,0.0> angle 45}


light_source
{
  <0,20,0>
  colour rgb <1.0,1.0,1.0>
  parallel
  point_at <0,0,0>
}

light_source
{
  <0,0,-20>
  colour rgb <1.0,1.0,1.0>
  parallel
  point_at <0,0,0>
}


// ------------------<<< Raster macro
#macro Raster(RScale, RLine)
pigment{
   gradient x scale RScale
   color_map{
     [0.000   color rgbt<0,0,0,0>]
     [0+RLine color rgbt<0,0,0,0>]
     [0+RLine color rgbt<1,1,1,1>]
     [1-RLine color rgbt<1,1,1,1>]
     [1-RLine color rgbt<0,0,0,0>]
     [1.000   color rgbt<0,0,0,0>]
            }
       } // end of pigment
#end// of "Raster(RScale, RLine)"

// -------------------<<<< Grid macro
#macro Grid(RasterScale,
            RasterHalfLine,
            Background_pigment)
plane{<0,1,0>, 0
       //layered textures!!!!
      texture{ Background_pigment
             } //  base color
      texture{ Raster(RasterScale,
                      RasterHalfLine)
             } // 2nd layer
      texture{ Raster(RasterScale,
                      RasterHalfLine)
               rotate<0,90,0>
             } // 3rd layer
     } // end of plane
#end // end of macro "Grid(...)"
// -----------------------------------



#macro Axis_( AxisLen,
              RedTexture,
              WhiteTexture)
union{
 cylinder{<0,-AxisLen,0>,<0,AxisLen,0>,0.05
          texture{checker
                  texture{RedTexture  }
                  texture{WhiteTexture}
                  translate<0.1,0,0.1>}}
 cone{<0,AxisLen,0>,0.2,<0,AxisLen+0.7,0>,0
           texture{RedTexture}}
} // end of union "Axis"
#end // of macro Axis (AxisLen)
#macro Axis2_( AxisLen,
              RedTexture,
              WhiteTexture)
union{
 cylinder{<0,0,0>,<0,AxisLen,0>,0.05
          texture{checker
                  texture{RedTexture  }
                  texture{WhiteTexture}
                  translate<0.1,0,0.1>}}
 cone{<0,AxisLen,0>,0.2,<0,AxisLen+0.7,0>,0
           texture{RedTexture}}
} // end of union "Axis"
#end // of macro Axis (AxisLen)
//-----------------------------------------
#macro AxisXYZ(AxisLX,AxisLY,AxisLZ,
               TexRed,TexWhite)
//-- drawing 3 axes -- 3 Achsen zeichnen --
union{
object{Axis2_(AxisLX,TexRed,TexWhite)
       rotate< 0,0,-90>}// x-Axis
object{Axis_(AxisLY,TexRed,TexWhite)
       rotate< 0,0,  0>}// y-Axis
object{Axis_(AxisLZ,TexRed,TexWhite)
       rotate<90,0,  0>}// z-Axis

text{ttf"arial.ttf",  "z",  0.01,  0
     texture{TexRed} 
     scale 1.2 translate <AxisLX+0.05,0.7,-0.12>}
text{ttf"arial.ttf",  "y",  0.01,  0  
     texture{TexRed} 
     scale 1.2 translate <-0.85,AxisLY+0.50,-0.05>}
text{ttf"arial.ttf",  "x",  0.01,  0
     texture{TexRed} 
     scale 1.2 translate <-0.75,0.2,AxisLZ+0.50>}
} // end of union
#end// of macro "AxisXYZ(...)"  -----------
//-- drawing the axis -- Achsen zeichnen --
#declare Tex_Dark =
texture{pigment{color rgb<1,0.3,0>}
        finish{ phong 1}}
#declare Tex_White =
texture{pigment{color rgb<1,1,1>}
        finish{ phong 1}}






background
{
  rgb <0,0,0,0>
}


object
{
 AxisXYZ(20.0,5.0,5.0, Tex_Dark,Tex_White)
 translate <-10.0,0,0>
}

intersection
{
object{
Grid(1.00,0.035,
pigment{color rgb<1,1,1>*0.4})
}
box {<-10.0,-1.0,-5.0><10.0,1.0,5.0>}
rotate -90*x
translate 8*z
}

intersection
{
object{
Grid(1.00,0.035,
pigment{color rgb<1,1,1>*0.4})
}
box {<-10.0,-1.0,-5.0><10.0,1.0,5.0>}
translate -8*y
}




/*
box {<-1.5,-2,-1><1.5,-1,1>
pigment { checker
         color rgbf <0.5 ,0.5 ,0.5 ,0.0>
         color rgbf <0.01,0.01,0.01,0.0>
         scale 0.5
         }
}



box {<-1.5,-1,1><1.5,1,2>
pigment { checker
         color rgbf <0.5 ,0.5 ,0.5 ,0.0>
         color rgbf <0.01,0.01,0.01,0.0>
         scale 0.5
         }
}
*/



#if (ISOSURFACE)
// isosurface
#declare F=function{
pattern{
density_file df3 "example.df3"

#if (INTERPOLATE=0)
  interpolate 0
#else
// mesh : 32*32*64
  scale<NBX/(NBX-1),NBY/(NBY-1),NBZ/(NBZ-1)>
  interpolate INTERPOLATE
#end

translate <-0.5,-0.5,-0.5>
}
}

isosurface {
function { ISOLEVEL-F(x,y,z) }
max_gradient 35
contained_by { box { -1, 1 } }
pigment { color rgbf <1,0,0,0>}
scale <10,10,20>
rotate y*90
}
#end








#if (CLOUD)
box
{
 <0,0,0><1,1,1>
 hollow
 pigment
 {
  rgbf 1
 }
 interior
 {
  media
  {
   emission 0.7
   absorption 1.0
   intervals 10
   density
   {
    density_file df3 "example.df3"

#if (INTERPOLATE=0)
  interpolate 0
#else
// mesh : 32*32*64
  scale<NBX/(NBX-1),NBY/(NBY-1),NBZ/(NBZ-1)>
  interpolate INTERPOLATE
#end

    color_map
    {
     [0.0   rgb <0.0,0.0,0.0>]
     [0.1   rgb <0.0,0.0,2.0>]
     [1.0   rgb <1.0,1.0,1.0>]
    } 
   }
  }
 }
 scale <10,10,20>
 translate <-5,-5,-10>
 rotate y*90
}
#end









/*
// boite transparente
box
{
 <-1.0,-1.0,-1.0><1.0,1.0,1.0>
 pigment
 {
  color rgbt <1.0,1.0,1.0,0.7>
 }
 scale <5,5,5>
 rotate y*90
}
*/


// trait de la legende "2 fm"
box
{
 <-10.2,-8,-4><-10.3,-8.01,-5>
 pigment{color rgb <1,1,1>}
}

// texte de la legende "2 fm"
text
{
 ttf "arial.ttf", "2 fm",  0.01,  0
 pigment{color rgb <1,1,1>}
 rotate x*90
 rotate y*-90
 scale 0.8
 translate <-10.6,-8,-5>
}




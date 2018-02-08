camera
{
  location <1,4,-5>
  look_at <0,1,0>
  angle 45
}

// 00

background
{
  rgb <1,1,1>
}

// 01

/*
plane
{
  <0,1,0>, 0
}
*/

// 02

light_source
{
  <-2,7,-3>
  color rgb <1,1,1>
}

// 03

object
{
  plane
  {
    <0,1,0>
    0
    pigment
    {
      checker
      color rgb <0.7,0.7,0.8>
      color rgb <0.5,0.5,0.5>
      scale 2
    }
  }
}

// 04

/*
object
{
  box
  {
    <-1,0,-1>, <1,2,1>
  }
  pigment
  {
    color rgb <1.0,0.0,0.0>
  }
}
*/

// 05

/*
object
{
  sphere
  {
    <0,1,0>, 0.2
  }
  pigment
  {
    color rgb <0.0,1.0,0.0>
  }
  finish
  {
    phong 1.0
    reflection 0.2
  }
}
*/

// 06

/*
object
{
  torus
  {
    0.8, 0.2
  }
  pigment
  {
    color rgb <0,0,1>
  }
  finish
  {
    phong 1.0
    reflection 0.2
  }
  rotate <90,0,0>
  translate <0,1,0>
}
*/

// 07

/*
object
{
  cylinder
  {
    <0,0,0>
    <0,2,0>
    1
  }
  pigment
  {
    color rgb <1,1,0>
  }
  finish
  {
    phong 1.0
    reflection 0.2
  }
}
*/

/*
object
{
  cone
  {
    <0,0,0>
    1
    <0,2,0>
    0.1
  }
  pigment
  {
    color rgb <1,0,1>
  }
  finish
  {
    phong 1.0
    reflection 0.2
  }
}
*/

/*
object
{
  lathe
  {
    cubic_spline
    6,
    <1,0>, <1,0>, <1,2>, <0.3,2>, <0.3,0>, <0.3,0>
  }
  pigment
  {
    color rgb <0,1,1>
  }
  finish
  {
    phong 1.0
    reflection 0.2
  }
}
*/

/*
object
{
  prism
  {
    linear_spline
    0, 2, 10,
    <-1,-1>, <-1,1>, <1,1>, <1,-1>, <-1,-1>,
    <-0.8,-0.8>, <-0.8,0.8>, <0.8,0.8>, <0.8,-0.8>, <-0.8,-0.8>
  }
  pigment
  {
    color rgb <1,0,0>
  }
  finish
  {
    phong 1.0
    reflection 0.2
  }
}
*/

/*
object
{
  blob
  {
    threshold 0.6
    sphere { <.75, 0, 0>, 1, 1 }
    sphere { <-.375, .64952, 0>, 1, 1 }
    sphere { <-.375, -.64952, 0>, 1, 1 }
    rotate <90,0,0>
    translate <0,1,0>
    scale 1.2
  }
  pigment
  {
    color rgb <0,1,0>
  }
  finish
  {
    phong 1.0
    reflection 0.2
  }
}
*/

/*
object
{
  text
  {
    ttf "timrom.ttf" "ENSIIE"
    0.3,
    0
    translate <-1.6,-0.35,-0.15>
    scale 1.0
    translate <0,1,0>
  }
  pigment
  {
    agate
    color_map {
      [0.00 color rgb <1,0,0>]
      [0.25 color rgb <1,1,0>]
      [0.50 color rgb <0,1,0>]
      [0.75 color rgb <0,1,1>]
      [1.00 color rgb <0,0,1>]
    }
    scale 2.0
  }
  finish
  {
    phong 1.0
    reflection 0.2
  }
}
*/

/*
object
{
  text
  {
    ttf "timrom.ttf" "ENSIIE"
    0.3,
    0
    translate <-1.6,-0.35,-0.15>
    scale 1.0
    translate <0,1,0>
  }
  pigment
  {
    rgbf <1,0,0,0.9>
  }
  finish
  {
    phong 1.0
    reflection 0.2
    ambient 0.1
    diffuse 0.5
    specular 0.5
  }
}
*/

/*
object
{
  union
  {
    box
    {
      <-1,0,-1>, <1,2,1>
    }
    sphere
    {
      <0,2,0>, 1.0
    }
    scale 0.7
  }
  pigment
  {
    color rgb <0,1,0>
  }
  finish
  {
    phong 1.0
    reflection 0.2
  }
}
*/

/*
object
{
  intersection
  {
    box
    {
      <-1,0,-1>, <1,2,1>
    }
    sphere
    {
      <0,2,0>, 1.0
    }
    scale 0.7
  }
  pigment
  {
    color rgb <0,0,1> // pure blue
  }
  finish
  {
    phong 1.0
    reflection 0.2
  }
}
*/

/*
object
{
  difference
  {
    box
    {
      <-1,0,-1>, <1,2,1>
    }
    sphere
    {
      <0,2,0>, 1.0
    }
    scale 0.7
  }
  pigment
  {
    color rgb <1,0,0> // pure red
  }
  finish
  {
    phong 1.0
    reflection 0.2
  }
}
*/

/*
object
{
  merge
  {
    box
    {
      <-1,0,-1>, <1,2,1>
    }
    sphere
    {
      <0,2,0>, 1.0
    }
    scale 0.7
  }
  pigment
  {
    color rgb <1,1,0> // pure yellow
  }
  finish
  {
    phong 1.0
    reflection 0.2
  }
}
*/

/*
object
{
  union
  {
    box
    {
      <-1,0,-1>, <1,2,1>
    }
    sphere
    {
      <0,2,0>, 1.0
    }
    scale 0.7
  }
  pigment
  {
    color rgbf <1,0,0,0.9> // transparent red
  }
  finish
  {
    phong 1.0
    reflection 0.2
  }
}
*/

/*
#declare fn_Hills = function
{
  pigment
  {
    bumps
    warp
    {
      turbulence 0.5
    }
    scale 0.2
  }
}

object
{
  height_field
  {
    function 16, 16
    {
      fn_Hills (x, y, z).red
    }
  }
  pigment
  {
    gradient y
    color_map
    {
      [0.0 color rgb <1,1,1>]
      [0.5 color rgb <1,1,1>]
      [1.0 color rgb <1,0,0>]
    }
  }
  finish
  {
    phong 1.0
    reflection 0.2
  }
  translate <-0.5, -0.5, -0.5>
  scale <2, 0.5, 2>
  translate <0,1,0>
}
*/

object
{
  box
  {
    <-1,-1,-1>, <1,1,1>
    hollow
  }
  pigment
  {
    color rgbf <1,1,1,1>
  }
  interior
  {
    media
    {
      emission 0.75
      scattering {1, 0.5}
      density
      {
        spherical
        color_map
        {
          [0.0 rgb <0,0,0.5>]
          [0.5 rgb <0.8, 0.8, 0.4>]
          [1.0 rgb <1,1,1>]
        }
      }
    }
  }
  translate <0,1.001,0>
}


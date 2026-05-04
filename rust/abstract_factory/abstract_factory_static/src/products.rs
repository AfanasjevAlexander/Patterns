pub trait Shape {
    fn draw(&self);
}

pub struct Rectangle {}

impl Shape for Rectangle {
    fn draw(&self) {
        println!("draw a rectangle!");
    }
}


pub struct Circle {}

impl Shape for Circle {
    fn draw(&self) {
        println!("draw a circle!");
    }
}
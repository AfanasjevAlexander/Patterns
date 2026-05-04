mod factory;
mod products;

use factory::{StaticShapeFactory, ShapeType};

use crate::products::Shape;


fn main() {
    let shape = StaticShapeFactory::new_shape(&ShapeType::Circle);
    shape.draw(); // output: draw a circle!

    let shape = StaticShapeFactory::new_shape(&ShapeType::Rectangle);
    shape.draw(); // output: draw a rectangle!
}

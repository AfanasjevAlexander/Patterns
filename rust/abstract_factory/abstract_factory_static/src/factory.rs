use crate::products::{Shape, Circle, Rectangle};

pub enum ShapeType {
    Circle,
    Rectangle,
}

pub enum StaticShape {
    Rectangle(Rectangle),
    Circle(Circle),
}

impl Shape for StaticShape {
    fn draw(&self) {
        match self {
            StaticShape::Rectangle(sh) => sh.draw(),
            StaticShape::Circle(sh) => sh.draw(),
        }
    }
}

pub struct StaticShapeFactory;
impl StaticShapeFactory {
    pub fn new_shape(s: &ShapeType) -> StaticShape {
        match s {
            ShapeType::Rectangle => StaticShape::Rectangle(Rectangle {}),
            ShapeType::Circle => StaticShape::Circle(Circle {}),
        }
    }
}
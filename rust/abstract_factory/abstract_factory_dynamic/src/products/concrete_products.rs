use super::{Button, Checkbox};

pub struct DarkButton;
pub struct DarkCheckbox;

pub struct LightButton;
pub struct LightCheckbox;

impl Button for DarkButton {
    fn render(&self) {
        println!("I am a dark button");
    }
}

impl Button for LightButton {
    fn render(&self) {
        println!("I am a light button");
    }
}

impl Checkbox for DarkCheckbox {
    fn render(&self) {
        println!("I am a dark checkbox");
    }
}

impl Checkbox for LightCheckbox {
    fn render(&self) {
        println!("I am a light checkbox")
    }
} 
// relitive path
use crate::{Button, Checkbox, GuiFactory};

pub struct WindowsButton;

impl Button for WindowsButton {
    fn press(&self) {
        println!("Windows button has pressed!");
    }
}

pub struct WindowsCheckbox;

impl Checkbox for WindowsCheckbox {
    fn switch(&self) {
        println!("Windows checkbox has swithed!");
    }
}

pub struct WindowsFactory;

impl GuiFactory for WindowsFactory {
    type B = WindowsButton;
    type C = WindowsCheckbox;

    fn create_button(&self) -> Self::B {
        WindowsButton
    }

    fn create_checkbox(&self) -> Self::C {
        WindowsCheckbox
    }
}

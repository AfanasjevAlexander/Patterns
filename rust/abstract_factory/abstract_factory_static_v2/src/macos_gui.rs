//absolute path
use crate::{ Button, Checkbox, GuiFactory};

pub struct MacOSButton;

impl Button for MacOSButton {
    fn press(&self) {
        println!("Mac OS button has pressed!");
    }
}

pub struct MacOSCheckbox;

impl Checkbox for MacOSCheckbox {
    fn switch(&self) {
        println!("Mac OS button checkbox has switched!");
    }
}

pub struct MacOSFactory;

impl GuiFactory for MacOSFactory {
    type B = MacOSButton;
    type C = MacOSCheckbox;

    fn create_button(&self) -> Self::B {
        MacOSButton
    }
    fn create_checkbox(&self) -> Self::C {
        MacOSCheckbox
    }
}
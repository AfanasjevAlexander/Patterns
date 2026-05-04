/// This is another Concrete Creator

use crate::gui::{Button, Dialog};

pub struct WindowsButton;

impl Button for WindowsButton {
    fn render(&self) {
        println!("Drawing a Window button");
        self.on_click();
    }

    fn on_click(&self) {
        println!("Click! Hello, Windows!");
    }
}

pub struct WindowsDialog;

impl Dialog for WindowsDialog {
    // Creates a windows button
    fn create_button(&self) -> Box<dyn Button> {
        Box::new(WindowsButton)
    }
}
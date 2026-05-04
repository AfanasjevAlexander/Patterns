use super::{ThemeFactory, Button, Checkbox, DarkButton, DarkCheckbox, LightButton, LightCheckbox};

pub struct DarkFactory;
pub struct LightFactory;

impl ThemeFactory for DarkFactory {
    fn create_button(&self) -> Box<dyn Button> {
        Box::new(DarkButton)
    }
    fn create_checkbox(&self) -> Box<dyn Checkbox> {
        Box::new(DarkCheckbox)
    }
}

impl ThemeFactory for LightFactory {
    fn create_button(&self)->Box<dyn Button> {
        Box::new(LightButton)
    }
    fn create_checkbox(&self)->Box<dyn Checkbox> {
        Box::new(LightCheckbox)
    }
}
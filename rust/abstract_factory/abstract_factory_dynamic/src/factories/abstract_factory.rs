use super::super::products::abstract_products::{Button, Checkbox};

pub trait ThemeFactory {
    fn create_button(&self) -> Box<dyn Button>;
    fn create_checkbox(&self) -> Box<dyn Checkbox>;
}
mod factories;
mod products;

use crate::factories::{abstract_factory::ThemeFactory, concrete_factories::{DarkFactory, LightFactory}};
use crate::products::abstract_products::{Button, Checkbox};

fn render_ui(factory: &dyn ThemeFactory) {
    let button: Box<dyn Button> = factory.create_button();
    let checkbox: Box<dyn Checkbox> = factory.create_checkbox();

    button.render();
    checkbox.render();
    checkbox.toggle_check();
}

fn main() {
    let dark_factory: Box<dyn ThemeFactory> = Box::new(DarkFactory);
    let light_factory: Box<dyn ThemeFactory> = Box::new(LightFactory);

    println!("Rendering dark theme:");
    render_ui(&*dark_factory);

    println!("\nRendering light theme:");
    render_ui(&*light_factory);
}

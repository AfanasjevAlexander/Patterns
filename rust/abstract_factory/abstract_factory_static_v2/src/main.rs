mod gui_abstract;
pub use gui_abstract::{Button, Checkbox, GuiFactory};

mod macos_gui;
use macos_gui::MacOSFactory;

mod windows_gui;
use windows_gui::WindowsFactory;


fn render(factory: &impl GuiFactory) {
    let button = factory.create_button();
    let checkbox = factory.create_checkbox();

    button.press();
    checkbox.switch();
}


fn main() {
    let windows = true;

    if windows {
        render(&WindowsFactory);
    } else {
        render(&MacOSFactory);
    }
}

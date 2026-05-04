pub trait Button {
    fn render(&self);
}

pub trait Checkbox {
    fn render(&self);
    fn toggle_check(&self) {
        println!("Togled")
    }
}
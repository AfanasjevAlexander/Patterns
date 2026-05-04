use crate::{adaptee::SpecificTarget, Target};

/// Converts  adaptee's specific interface to a compatible 'Target' output
pub struct TargerAdapter {
    adaptee: SpecificTarget,
}

impl TargerAdapter {
    pub fn new(adaptee: SpecificTarget) -> Self {
        Self { adaptee }
    }
}

impl Target for TargerAdapter {
    fn request(&self) -> String {
        // Here's the "adaptation" of a specific interface to a compatible output
        self.adaptee.specific_request().chars().rev().collect()
    }
}
/*
Dialog Rendering
This example illustrates how to organize a GUI framework into independent modules using dynamic dispatch:

1) The gui module defines interfaces for all the components. 
   It has no external dependencies.

2) The html_gui module provides HTML implementation of the base GUI.
   Depends on gui.

3) The windows_gui module provides Windows implementation of the base GUI.
    Depends on gui.

    The app is a client application that can use several implementations of the GUI framework, 
    depending on the current environment or configuration. 
    However, most of the app code doesn't depend on specific types of GUI elements. 
    All client code works with GUI elements through abstract interfaces defined by the gui module.
*/
mod gui;
mod html_gui;
mod windows_gui;
mod init;

use init::initialize;

fn main() {
    // The rest of the code doesn't depend on specific dialog types, because
    // it works with all dialog objects via the abstract `Dialog` trait
    // which is defined in the `gui` module.

    let dialog = initialize();
    dialog.render();
    dialog.refresh();
}

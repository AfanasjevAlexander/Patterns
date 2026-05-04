/*
There is a practical example in Rust's standard library for input/output operations.
A buffered reader decorates a vector reader adding buffered behavior.

let mut input = BufReader::new(Cursor::new("Input data"));
input.read(&mut buf).ok();
*/

use std::io::{BufReader, Cursor, Read};

fn main() {
    let mut buf = [0u8; 10];

    // A buffered reader decorates a vector reader which wraps input data
    let mut input = BufReader::new(Cursor::new("Input data"));

    input.read(&mut buf).ok();

    println!("Read from a buffered reader: ");

    for byte in buf {
        print!("{}", char::from(byte));
    }

    println!();
}

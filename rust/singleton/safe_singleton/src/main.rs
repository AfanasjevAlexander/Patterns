// установление "глобальной" переменной через аргумент функции флаг
fn change(global_state: &mut u32) {
    *global_state += 1;
}

fn main() {
    let mut global_state = 0_u32;

    change(&mut global_state);

    println!("Final state: {}", global_state);
}

//Working on remaking this project in Rust, hence the second 
use std::collections::HashMap;

fn main(){
    let call_key = key_map();
    println!("{}", call_key.get(&).unwrap());
}
fn key_map(){
    let mut keyboard_map = HashMap::new();
    let keyboard = "1234567890qwertyuiopasdfghjklzxcvbnm";
    let mut temp: u8 = 2;
    const OFFSET: u8 = 34;
    for i in keyboard.chars(){
        keyboard_map.insert(temp + OFFSET, i.to_string());

        if [2, 4, 7, 9, 11].contains(&(temp % 12)) {
            
            temp = temp + 1;
            keyboard_map.insert(temp + OFFSET, format!("shift + {}", i.to_string()));
        }
        temp = temp + 1;
    }
    keyboard_map

}

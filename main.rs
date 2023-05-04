//Working on remaking this project in Rust, hence the second 
use std::collections::HashMap;

fn main(){
    let mut keyboard_map = HashMap::new();
    let keyboard = "1234567890qwertyuiopasdfghjklzxcvbnm";
    let mut temp: u8 = 2;
    for i in keyboard.chars(){
        keyboard_map.insert(temp + 34, i.to_string());

        if [2, 4, 7, 9, 11].contains(&(temp % 12)) {
            
            temp = temp + 1;
            keyboard_map.insert(temp + 34, format!("shift + {}", i.to_string()));
        }
        temp = temp + 1;
    }
    for (key,value) in keyboard_map.into_iter(){
        println!("{} / {}", key, value);
    }
    // println!("{}", keyboard_map.get(&38).unwrap())
}

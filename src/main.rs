use friendly_zoo::Zoo;
use std::fs;
use std::io;

fn main() -> io::Result<()> {
    let dir_name = Zoo::default().generate();
    let mut path = std::env::temp_dir();
    path.push(dir_name);
    fs::create_dir(&path)?;

    eprintln!("cd {:?}", path);
    println!("cd {:?}", path);

    Ok(())
}

#[derive(Clone, Debug)]
struct Prototype {
    data: String,
}

impl Prototype {
    fn new(data: &str) -> Self {
        Prototype {
            data: data.to_string(),
        }
    }

    fn clone(&self) -> Self {
        Prototype {
            data: self.data.clone(),
        }
    }
}
// IMPORTANT
// there are 2 kinds of copying
// shallow - 2 objects may share something by internal reference
// deep - 2 objects can't share anything internaly
pub fn prototype_main() {
    // Creating a prototype instance.
    let original_prototype = Prototype::new("Original Data");

    // Cloning the prototype to create a new instance.
    let cloned_prototype = original_prototype.clone();

    // Modifying the data in the cloned prototype.
    let mut modified_cloned_prototype = cloned_prototype.clone();
    modified_cloned_prototype.data = "Modified Data".to_string();

    // Displaying the data of the original, cloned, and modified cloned prototypes.
    println!("Original Prototype Data: {}", original_prototype.data);
    println!("Cloned Prototype Data: {}", cloned_prototype.data);
    println!(
        "Modified Cloned Prototype Data: {}",
        modified_cloned_prototype.data
    );
}

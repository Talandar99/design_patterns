struct Singleton {
    data: String,
}

impl Singleton {
    fn new(data: &str) -> Self {
        Singleton {
            data: data.to_string(),
        }
    }

    fn get_instance(&self) -> &str {
        &self.data
    }
}

pub fn singleton_main() {
    let instance = Singleton::new("Singleton Instance");
    function_using_singleton(&instance);
    another_function_using_singleton(&instance);
}

fn function_using_singleton(instance: &Singleton) {
    println!("Function using Singleton: {}", instance.get_instance());
}

fn another_function_using_singleton(instance: &Singleton) {
    println!(
        "Another function using Singleton: {}",
        instance.get_instance()
    );
}

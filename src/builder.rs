// Defining a Product struct that will be built.
struct Product {
    part1: String,
    part2: String,
}

impl Product {
    // A method to display the parts of the product.
    fn show(&self) {
        println!("Part 1: {}", self.part1);
        println!("Part 2: {}", self.part2);
    }
}

// The Builder trait defines the steps needed to create a Product.
trait Builder {
    // Method to build the first part of the product.
    fn build_part1(&mut self);

    // Method to build the second part of the product.
    fn build_part2(&mut self);

    // Method to get the final product.
    fn get_product(&self) -> &Product;
}

// ConcreteBuilder implements the Builder trait to create a specific type of product.
struct ConcreteBuilder {
    product: Product,
}

impl ConcreteBuilder {
    // Creating a new ConcreteBuilder with an empty Product.
    fn new() -> Self {
        ConcreteBuilder {
            product: Product {
                part1: String::new(),
                part2: String::new(),
            },
        }
    }
}

// Implementation of the Builder trait for ConcreteBuilder.
impl Builder for ConcreteBuilder {
    // Building the first part of the product.
    fn build_part1(&mut self) {
        self.product.part1 = "Part 1 built".to_string();
    }

    // Building the second part of the product.
    fn build_part2(&mut self) {
        self.product.part2 = "Part 2 built".to_string();
    }

    // Getting the final product.
    fn get_product(&self) -> &Product {
        &self.product
    }
}

// The Director orchestrates the building process using a Builder.
struct Director {
    builder: Box<dyn Builder>,
}

impl Director {
    // Creating a new Director with a given Builder.
    fn new(builder: Box<dyn Builder>) -> Self {
        Director { builder }
    }

    // Instructing the Director to construct the product.
    fn construct(&mut self) {
        self.builder.build_part1();
        self.builder.build_part2();
    }
}

fn main() {
    // Creating a ConcreteBuilder instance.
    let builder = Box::new(ConcreteBuilder::new());

    // Creating a Director with the ConcreteBuilder.
    let mut director = Director::new(builder);

    // Instructing the Director to construct the product.
    director.construct();

    // Getting the final product from the builder.
    let product = director.builder.get_product();

    // Displaying the constructed product's parts.
    product.show();
}

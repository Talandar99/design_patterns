//! Factory method creational design pattern allows creating objects without
//! having to specify the exact type of the object that will be created.

// Definition of the `Shape` trait, which contains a single method `draw()`.
trait Shape {
    fn draw(&self);
}

// Enum `ShapeType` defines possible shape types.
enum ShapeType {
    Rectangle,
    Circle,
    Triangle,
}

// Definition of the `Rectangle` struct, which doesn't have any fields, as in this example
// there's no need to store additional shape information.
struct Rectangle {}
// Implementation of the `Shape` trait for the `Rectangle` struct.
impl Shape for Rectangle {
    fn draw(&self) {
        println!("draw a rectangle!");
    }
}

// Definition of the `Circle` struct, similar to the `Rectangle` struct, doesn't store any additional information.
struct Circle {}
// Implementation of the `Shape` trait for the `Circle` struct.
impl Shape for Circle {
    fn draw(&self) {
        println!("draw a circle!");
    }
}

// My example
struct Triangle {}
impl Shape for Triangle {
    fn draw(&self) {
        println!("draw a triangle")
    }
}

// Definition of the `ShapeFactory` struct, which will contain the factory method `new_shape`.
struct ShapeFactory;

// Implementation of the `new_shape` method for the `ShapeFactory` struct, which creates `Shape` instances based on the provided `ShapeType`.
impl ShapeFactory {
    fn new_shape(s: &ShapeType) -> Box<dyn Shape> {
        match s {
            ShapeType::Circle => Box::new(Circle {}),
            ShapeType::Rectangle => Box::new(Rectangle {}),
            ShapeType::Triangle => Box::new(Triangle {}),
        }
    }
}

// The `factory_main` function represents the main entry point of the program.
pub fn factory_main() {
    // Creating a shape instance (in this case, a circle) using the factory.
    let shape = ShapeFactory::new_shape(&ShapeType::Circle);
    shape.draw(); // Calling the `draw()` method on the created object - output: "draw a circle!"

    // Creating a shape instance (in this case, a rectangle) using the factory.
    let shape = ShapeFactory::new_shape(&ShapeType::Rectangle);
    shape.draw(); // Calling the `draw()` method on the created object - output: "draw a rectangle!"

    let shape = ShapeFactory::new_shape(&ShapeType::Triangle);
    shape.draw();
}

trait Shape {
    fn draw(&self);
}

// Concrete implementations of the simple shapes
struct Circle;
impl Shape for Circle {
    fn draw(&self) {
        println!("Draw a circle!");
    }
}

struct Rectangle;
impl Shape for Rectangle {
    fn draw(&self) {
        println!("Draw a rectangle!");
    }
}

struct Triangle;
impl Shape for Triangle {
    fn draw(&self) {
        println!("Draw a triangle!");
    }
}

// Complex implementations of the shapes
struct ComplexCircle;
impl Shape for ComplexCircle {
    fn draw(&self) {
        println!("Draw a complex circle!");
    }
}

struct ComplexRectangle;
impl Shape for ComplexRectangle {
    fn draw(&self) {
        println!("Draw a complex rectangle!");
    }
}

struct ComplexTriangle;
impl Shape for ComplexTriangle {
    fn draw(&self) {
        println!("Draw a complex triangle!");
    }
}
// Abstract Factory trait
trait ShapeFactory {
    fn create_circle(&self) -> Box<dyn Shape>;
    fn create_rectangle(&self) -> Box<dyn Shape>;
    fn create_triangle(&self) -> Box<dyn Shape>;
}

// Concrete Factory for SimpleShapes
struct SimpleShapeFactory;

impl ShapeFactory for SimpleShapeFactory {
    fn create_circle(&self) -> Box<dyn Shape> {
        Box::new(Circle {})
    }

    fn create_rectangle(&self) -> Box<dyn Shape> {
        Box::new(Rectangle {})
    }

    fn create_triangle(&self) -> Box<dyn Shape> {
        Box::new(Triangle {})
    }
}

// Concrete Factory for ComplexShapes
struct ComplexShapeFactory;

impl ShapeFactory for ComplexShapeFactory {
    fn create_circle(&self) -> Box<dyn Shape> {
        Box::new(ComplexCircle {})
    }

    fn create_rectangle(&self) -> Box<dyn Shape> {
        Box::new(ComplexRectangle {})
    }

    fn create_triangle(&self) -> Box<dyn Shape> {
        Box::new(ComplexTriangle {})
    }
}

// Rest of the code remains the same...

pub fn abstract_factory_main() {
    // Creating SimpleShapes using SimpleShapeFactory
    let simple_factory: Box<dyn ShapeFactory> = Box::new(SimpleShapeFactory);

    let simple_circle = simple_factory.create_circle();
    simple_circle.draw(); // Output: "draw a circle!"

    let simple_rectangle = simple_factory.create_rectangle();
    simple_rectangle.draw(); // Output: "draw a rectangle!"

    let simple_triangle = simple_factory.create_triangle();
    simple_triangle.draw(); // Output: "draw a triangle"

    // Creating ComplexShapes using ComplexShapeFactory
    let complex_factory: Box<dyn ShapeFactory> = Box::new(ComplexShapeFactory);

    let complex_circle = complex_factory.create_circle();
    complex_circle.draw(); // Output: "draw a complex circle!"

    let complex_rectangle = complex_factory.create_rectangle();
    complex_rectangle.draw(); // Output: "draw a complex rectangle!"

    let complex_triangle = complex_factory.create_triangle();
    complex_triangle.draw(); // Output: "draw a complex triangle"
}

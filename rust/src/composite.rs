// Component trait that defines the common interface for leaf nodes and composite nodes.
trait Graphic {
    fn draw(&self);
}

// Leaf node: Represents a simple ellipse graphic object.
struct Ellipse;

impl Graphic for Ellipse {
    fn draw(&self) {
        println!("Drawing an ellipse");
    }
}

// Leaf node: Represents a simple rectangle graphic object.
struct Rectangle;

impl Graphic for Rectangle {
    fn draw(&self) {
        println!("Drawing a rectangle");
    }
}

// Leaf node: Represents a simple triangle graphic object.
struct Triangle;

impl Graphic for Triangle {
    fn draw(&self) {
        println!("Drawing a triangle");
    }
}

// Composite node: Represents a group of graphic objects.
struct Picture {
    graphics: Vec<Box<dyn Graphic>>,
}

impl Graphic for Picture {
    fn draw(&self) {
        for graphic in &self.graphics {
            graphic.draw();
        }
    }
}

pub fn composite_main() {
    // Create individual graphic objects.
    let ellipse = Box::new(Ellipse);
    let rectangle = Box::new(Rectangle);
    let triangle = Box::new(Triangle);

    // Create a composite graphic object (picture) containing ellipse, rectangle, and triangle.
    let mut picture = Picture {
        graphics: vec![ellipse, rectangle, triangle],
    };

    // Draw the composite graphic object.
    picture.draw();
}

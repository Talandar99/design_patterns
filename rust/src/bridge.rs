// Define a trait representing a geometric shape.
trait Shape {
    fn draw(&self); // Method to draw the shape.
}

// Define a struct for Circle implementing the Shape trait.
struct Circle;
impl Shape for Circle {
    fn draw(&self) {
        println!("Drawing a circle");
    }
}

// Define a struct for Square implementing the Shape trait.
struct Square;
impl Shape for Square {
    fn draw(&self) {
        println!("Drawing a square");
    }
}

// Define a trait representing a colored shape.
// Extends the Shape trait and adds a method to set the color.
trait ColorShape: Shape {
    fn set_color(&mut self, color: String); // Method to set the color.
}

// Define a struct for a red-colored shape that implements the ColorShape trait.
// It composes an inner shape and holds the color information.
struct Red<T: Shape> {
    shape: T,
    color: String,
}

impl<T: Shape> ColorShape for Red<T> {
    fn set_color(&mut self, color: String) {
        self.color = color;
    }
}

impl<T: Shape> Shape for Red<T> {
    fn draw(&self) {
        println!("Drawing a {} {:?}", self.color, self.shape.draw());
    }
}

// Define a struct for a blue-colored shape that implements the ColorShape trait.
// It composes an inner shape and holds the color information.
struct Blue<T: Shape> {
    shape: T,
    color: String,
}

impl<T: Shape> ColorShape for Blue<T> {
    fn set_color(&mut self, color: String) {
        self.color = color;
    }
}

impl<T: Shape> Shape for Blue<T> {
    fn draw(&self) {
        println!("Drawing a {} {:?}", self.color, self.shape.draw());
    }
}

pub fn bridge_main() {
    // Create a red-colored circle using the Red struct.
    let red_circle = Red {
        shape: Circle,
        color: "Red".to_string(),
    };

    // Create a blue-colored square using the Blue struct.
    let blue_square = Blue {
        shape: Square,
        color: "Blue".to_string(),
    };

    // Draw the red circle and blue square.
    red_circle.draw();
    blue_square.draw();
}

mod abstract_factory;
mod builder;
mod factory;
mod prototype;

fn main() {
    println!("\nFactory example\n----------------------------");
    crate::factory::factory_main();
    println!("\nAbstract factory example\n----------------------------");
    crate::abstract_factory::abstract_factory_main();
    println!("\nBuilder example\n----------------------------");
    crate::builder::builder_main();
    println!("\nprototype example\n----------------------------");
    crate::prototype::prototype_main();
}

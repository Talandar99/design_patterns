mod abstract_factory;
mod adapter;
mod bridge;
mod builder;
mod composite;
mod decorator;
mod factory;
mod prototype;
mod singleton;

fn main() {
    println!("\nCreational Patterns\n========================================================");
    println!("\nFactory example\n----------------------------");
    crate::factory::factory_main();
    println!("\nAbstract factory example\n----------------------------");
    crate::abstract_factory::abstract_factory_main();
    println!("\nBuilder example\n----------------------------");
    crate::builder::builder_main();
    println!("\nPrototype example\n----------------------------");
    crate::prototype::prototype_main();
    println!("\nSingleton example\n----------------------------");
    crate::singleton::singleton_main();
    println!("\nStructural Patterns\n========================================================");
    println!("\nAdapter example\n----------------------------");
    crate::adapter::adapter_main();
    println!("\nBridge example\n----------------------------");
    crate::bridge::bridge_main();
    println!("\nComposite example\n----------------------------");
    crate::composite::composite_main();
    println!("\nDecorator example\n----------------------------");

    println!("\nFacade example\n----------------------------");
    println!("\nFlyweight example\n----------------------------");
    println!("\nProxy example\n----------------------------");
    println!("\nBehavioral Patterns\n========================================================");
    println!("\nChain of responsibility example\n----------------------------");
    println!("\nCommand example\n----------------------------");
    println!("\nIterator example\n----------------------------");
    println!("\nMediator example\n----------------------------");
    println!("\nMemento example\n----------------------------");
    println!("\nObserver example\n----------------------------");
    println!("\nState example\n----------------------------");
    println!("\nStrategy example\n----------------------------");
    println!("\nTemplate Method example\n----------------------------");
    println!("\nVisitor example\n----------------------------");
    println!("\nInterpreter example\n----------------------------");
}

// Adaptee - The existing component with a different interface.
struct LegacyComponent {
    legacy_data: String,
}

impl LegacyComponent {
    fn new(legacy_data: &str) -> Self {
        LegacyComponent {
            legacy_data: legacy_data.to_string(),
        }
    }

    fn get_legacy_data(&self) -> &str {
        &self.legacy_data
    }
}

// Target - The desired interface that the client expects.
trait NewComponent {
    fn get_new_data(&self) -> &str;
}

// Adapter - Adapts the Adaptee's interface to the Target's interface.
struct LegacyToNewAdapter {
    legacy_component: LegacyComponent,
}

impl LegacyToNewAdapter {
    fn new(legacy_component: LegacyComponent) -> Self {
        LegacyToNewAdapter { legacy_component }
    }
}

impl NewComponent for LegacyToNewAdapter {
    fn get_new_data(&self) -> &str {
        self.legacy_component.get_legacy_data()
    }
}

pub fn adapter_main() {
    // Using the LegacyComponent directly.
    let legacy_component = LegacyComponent::new("Legacy Data");
    println!(
        "Legacy Component Data: {}",
        legacy_component.get_legacy_data()
    );

    // Using the LegacyToNewAdapter to adapt the LegacyComponent to the NewComponent interface.
    let adapted_component = LegacyToNewAdapter::new(legacy_component);
    println!(
        "Adapted Component Data: {}",
        adapted_component.get_new_data()
    );
}
